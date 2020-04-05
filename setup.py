from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='b_dist',
version='0.4',
 description='Gaussian distributions',
 packages=['b_dist'],
 author='Abideen Bello',
 author_email='abideen.datascienceofficial@gmail.com',
 long_description=long_description,
    long_description_content_type='text/markdown'
 ,zip_safe=False)
