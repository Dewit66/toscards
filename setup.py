from setuptools import find_packages, setup

setup(
    name='toscards',
    packages=find_packages(include=['toscards']),
    version='0.1.0',
    description='My first Python library',
    author='Tobin Clouser',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
