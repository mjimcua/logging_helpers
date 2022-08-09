import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="loggin_helpers",
    version="1.0.0b1",
    author="Miguel Ángel Jiménez Cuadrillero",
    author_email="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.miguelangel.ai",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['colorama'],
    python_requires='~=3.6'
)
