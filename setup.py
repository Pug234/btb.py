from setuptools import setup

with open("README.md", "r") as f:
  readme = f.read()

setup(
  name = 'btbpython',
  packages = ['btbpython'],
  version = '2.1.1',
  license='MIT',
  description = 'A feature rich API to interact with the BttesToBits API',
  author = 'Corbin McKEe',
  author_email = 'corbin.mckee.ryan@gmail.com',
  url = 'https://github.com/Pug234/btb.py',
  keywords = ['API', 'BtbAPI', 'py', 'python', 'APIWrapper', 'btb.py', 'btb', 'BytesToBits'],
  long_description=readme,
  long_description_content_type="text/markdown",
  install_requires=[
          'requests',
          'Pillow',
      ],
  classifiers=[
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9'
  ],
)
