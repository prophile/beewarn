import ez_setup
ez_setup.use_setuptools()

from setuptools import setup

with open('README.md') as f:
    description = f.read()

from beewarn import VERSION

setup(name='beewarn',
      version=VERSION,
      description='Utility for warning about bees',
      author='Alistair Lynn',
      author_email='arplynn@gmail.com',
      license='MIT',
      long_description=description,
      url='https://github.com/prophile/beewarn',
      zip_safe=True,
      packages=['beewarn'])

