from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='area_calculation',
    version='0.0.1',
    author='gdemasha',
    author_email='maryrainwood@gmail.com',
    description='Library for calculating areas of geometrical figures',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/gdemasha/area_calculation.git',
    packages=find_packages(),
    install_requires=[
        'structlog>=25.3.0',
        'pytest>=8.3.5'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.10.14',
    ],
    keywords='geometry calculation area figures ',
    project_urls={
        'GitHub': 'https://github.com/gdemasha/area_calculation.git'
    },
    python_requires='>=3.10.14'
)
