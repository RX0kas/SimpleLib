from setuptools import find_packages, setup

setup(
    name='SimpleLib',
    packages=find_packages(include=['SimpleLib']),
    version='0.1.0',
    description='A library to facilitate the python development',
    author='ninjaoku4560',
    license='MIT',
    install_requires=["json"], 
    setup_requires=['pytest-runner'], 
    tests_require=['pytest==4.4.1'], 
)
