import io
from setuptools import setup, find_packages

README = io.open('README.md', encoding='utf-8').read()
REQUIREMENTS = [i.strip() for i in open('requirements.txt').readlines()]

setup(
    name='pythai_scb',
    version='1.0.1',
    packages=find_packages(),
    description='Unofficial SCB Bank Account Balance Check',
    long_description=README,
    long_description_content_type='text/markdown',
    license='MIT License',
    author='Krittaboon Tantikarun',
    author_email='krittaboon.t@gmail.com',
    url='https://github.com/ktantikarun/pythai-scb-unofficial',
    install_requires=REQUIREMENTS,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Information Technology",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries"
    ],
    python_requires='>=3.6',
    keywords=', '.join([
        'scb', 'investing-api', 'accounting-data',
        'financial-data', 'accountbalance'
    ]),
    project_urls={
        'Bug Reports & Feature Request': 'https://github.com/ktantikarun/pythai-scb-unofficial/issues',
        'Source': 'https://github.com/ktantikarun/pythai-scb-unofficial',
    },
)