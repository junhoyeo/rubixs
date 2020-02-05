import setuptools

with open('README.md', 'r') as file_handler:
  long_description = file_handler.read()

setuptools.setup(
  name='rubixs',
  packages=['rubixs'],
  version='0.0.1',
  license='MIT',
  description='Implementation of Rubix\'s cube in Python3',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Junho Yeo',
  author_email='hanaro0704@gmail.com',
  url='https://github.com/junhoyeo/rubixs',
  download_url='https://github.com/junhoyeo/rubixs/archive/v_0.0.1.tar.gz',
  keywords=[
    'rubix',
    'cube',
  ],
  install_requires=[],
  classifiers=[
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Topic :: Education',
    'Topic :: Games/Entertainment :: Puzzle Games',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.0',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3 :: Only',
  ],
  python_requires='>=3',
)
