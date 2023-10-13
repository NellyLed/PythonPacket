#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
from setuptools import find_packages, setup
def find_requires():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open("{0}/requirements.txt".format(dir_path), 'r') as reqs:
        requirements = reqs.readlines()
    return requirements
if __name__ == "__main__":
    setup(
        name='package',
        version='0.0.1',
        description="Дата создания:11.10.2023",
        long_description="""Содержит 6 модельных функций, файл для прочтения и с файл со списком пакетов.Имеются операции
сложения,вычитания,умножения,деления,вывода словочосетания и нахождение числа Фиббоначи. """,
        classifiers=[
            "Development Status :: 4 - Beta",
            "Programming Language :: Python"
        ],
        packages=find_packages(),
        install_requires=find_requires(),
        data_files=[],
        include_package_data=True,
        entry_points={
            "console_scripts": [
                "idnfilter = ds_idnfilter.idn_filter:main"
            ],
        },
    )