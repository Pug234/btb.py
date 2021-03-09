from setuptools import setup

setup(
   name='btb.pug',
   version='1.0',
   description='A python wrapper for the BytesToBits API',
   author="Corbin McKee",
   author_email='corbin.mckee.ryan@gmail.com',
   packages=['btb.pug', 'btb.py'],
   install_requires=['requests', 'pillow'],
)
