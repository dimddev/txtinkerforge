from setuptools import setup

setup(name='txtinkerforge',
      version='0.1',
      description='Python Async API (Twisted based) Bindings for Tinkerforge Bricks and Bricklets',
      license='CC0 1.0 Universal',
      author='dimd',
      author_email='dimd@gmail.com',
      url='https://github.com/dimddev/txtinkerforge',
      packages=['txtinkerforge', 'txtinkerforge.txapi'],
      platforms = 'Any',
      install_requires=['Twisted', 'tinkerforge'],
)