__author__ = 'dimd'

import inspect
from twisted.internet.threads import deferToThread


class TxMapper(object):
    """

    """

    maps = ['device', 'connection']

    def __init__(self, uid=None, ip_con=None):

        """

        :param uid:
        :param ip_con:
        :return:
        """

        super(TxMapper, self).__init__()

        self.__uid = uid
        self.__ip_con = ip_con

        try:

            getattr(self, 'device')

        except Exception:

            try:

                getattr(self, 'connection')

            except Exception:

                raise LookupError('subclass not present the connection attribute...')

            else:
                self.map(getattr(self, 'connection'))

        else:
            self.map(getattr(self, 'device'))

    def map(self, map_object):

        """

        :param map_object:
        :return:
        """

        if self.__uid and self.__ip_con:
            object_map = map_object(self.__uid, self.__ip_con)
        else:
            object_map = map_object()

        methods = [(k, getattr(object_map, k)) for k in map_object.__dict__ if inspect.ismethod(
            getattr(object_map, k))
        ]

        attributes = [(k, map_object.__dict__[k]) for k in map_object.__dict__.keys() if not inspect.ismethod(
            getattr(object_map, k))
        ]

        map(lambda method: setattr(self, method[0], self.__to_defer(method[1])), methods)
        map(lambda attr: setattr(self, attr[0], attr[1]), attributes)

    def __to_defer(self, func):

        """

        :param func:
        :return:
        """

        def response(*args):

            if len(inspect.getargspec(func).args) == 1:
                return deferToThread(func)

            else:
                return deferToThread(func, *args)

        return response
