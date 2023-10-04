from setuptools import setup, find_packages

setup(
    name='pyrrencies',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={},
    author='Yurii Plets',
    author_email='de.jure.software@gmail.com',
    description='Comfortable work with currencies and currencies exchange rates',
    license='MIT',
    keywords='currency currencies exchange rates',
    url='https://github.com/de-jure/pyrrencies',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
