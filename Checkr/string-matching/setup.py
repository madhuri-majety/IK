from setuptools import setup, find_packages

setup(
        name='string_matching',
        version='0.1',
        description='Name Matching APIs',
        packages=find_packages(),
        py_modules=[
            'string_matching'
        ],
        install_requires=[
                'redis'
        ]
)

