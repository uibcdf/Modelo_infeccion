from setuptools import setup, find_packages
from numpy.distutils.core import setup

extensions_list=[]

setup(
    name='modelo_infeccion',
    version='0.0.1',
    author='UIBCDF Lab',
    author_email='uibcdf@gmail.com',
    package_dir={'modelo_infeccion': 'modelo_infeccion'},
    packages=find_packages(),
    ext_modules=extensions_list,
    package_data={'modelo_infeccion': []},
    scripts=[],
    url='http://uibcdf.org',
    download_url ='https://github.com/uibcdf/Modelo_infeccion',
    license='MIT',
    description="---",
    long_description="---",
)
