from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="uptodateai",
    version="0.1.0",
    author="Isaak Kamau",
    author_email="isaakmwangi2018@gmail.com",
    description="UpToDateAI is a Python package designed to fetch and provide the latest documentation about recently released programming frameworks to AI models. This package helps bridge the gap between AI model training cut-off dates and the latest developments in the programming world.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IsaakKamau/UpToDateAI",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "scrapy",
        "newspaper3k",
        "markdown",
        "beautifulsoup4",
        "html2text",
        "python-slugify",
    ],
)