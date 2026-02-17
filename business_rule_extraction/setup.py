#!/usr/bin/env python3
"""
Setup script for Business Rule Extraction module
"""

from setuptools import setup, find_packages

setup(
    name="business-rule-extraction",
    version="1.0.0",
    description="Business Rule Extraction for IBM i AS400 Code",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="AS400 Parser Team",
    author_email="natarajanahilan@gmail.com",
    url="https://github.com/ahilasree/as400parser",
    packages=find_packages(),
    install_requires=[
        "antlr4-python3-runtime>=4.13.0",
        "reportlab>=4.0.0",
        "flask>=3.1.0",
        "flask-cors>=4.0.0",
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-flask>=1.2.0",
        ],
        "production": [
            "gunicorn>=21.0.0",
            "waitress>=3.0.0",
        ]
    },
    python_requires=">=3.11",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Code Generators",
        "Topic :: System :: Systems Administration",
    ],
    entry_points={
        "console_scripts": [
            "bre-demo=business_rule_extraction.bre.demo:main",
            "bre-analyze=business_rule_extraction.bre.extractor:main",
        ],
    },
)
