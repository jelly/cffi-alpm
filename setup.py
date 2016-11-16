from setuptools import setup

setup(
    name = 'cffi-alpm',
    version = '0.0.0',
    packages = ['alpm'],

    license = 'ISC',

    author = 'Johannes Löthberg',
    author_email = 'johannes@kyriasis.com',

    setup_requires = ['cffi >= 1.0.0'],
    install_requires = ['cffi >= 1.0.0'],
    cffi_modules=['alpm/build.py:ffibuilder'],

    classifiers = [
        "Development Status :: 3 - Alpha",
        'Topic :: System :: Archiving :: Packaging',
        'License :: OSI Approved :: ISC License (ISCL)',
    ],
)
