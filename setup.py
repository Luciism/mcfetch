from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mcfetch",
    version="1.0.0",
    author="oDepleted",
    author_email="contact@statalytics.net",
    description="Modified version of mcuuid - fetches Minecraft"
                "player information from the Mojang API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oDepleted/mcfetch",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'requests>=2.0.0'
    ],
)
