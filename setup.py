from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mcfetch",
    version="2.1.3",
    author="clerie, Lucism",
    author_email="contact@lucism.dev",
    description=
        "Modified version of mcuuid - fetches Minecraft "
        "player information from the Mojang API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Luciism/mcfetch",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'requests>=2.31.0',
        'aiohttp>=3.9.4',
        'aiohttp_client_cache>=0.8.1'
    ]
)
