import setuptools
from pvs_smtplib.__version__ import __version__
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='pvs_smtplib',
    version=__version__,
    author="Peel Valley Software",
    author_email="info@peelvalley.com.au",
    description="A custom wrapper for SMTP",
    keywords='smtp',
    url='https://github.com/peelvalley/pvs_smtplib',
    project_urls={
        'Bug Tracker': 'https://github.com/peelvalley/pvs_smtplib/issues',
        'Source Code': 'https://github.com/peelvalley/pvs_smtplib',
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
