import setuptools

setuptools.setup(
    name="mypackage",
    version="0.1.0",

    author="Mihai Criveti",

    description="An template for Python packages",
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),
    scripts=['bin/mypackage_cmd'],

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.6',
    ],
)
