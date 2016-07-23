from setuptools import setup, find_packages

with open('README.md') as readme:
    desc = readme.read()

setup(
    name="myfantasyleague",
    version="0.1",
    packages=find_packages(),
    install_requires=['requests'],
    author="Matthew Raspberry",
    author_email="nixalot@nixalot.com",
    description="Python wrapper for the MyFantasyLeague.com API",
    long_description=desc,
    url="https://github.com/nixalot/python-myfantasyleague",
    license="BSD",
    keywords="myfantasyleague mfl",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)