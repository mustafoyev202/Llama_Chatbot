"""
Setup script for Llama 4 Chat Interface
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="llama-chat-interface",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A modern web interface for running Llama 4 locally",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/llama-chat-interface",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.28.0",
        "huggingface_hub>=0.16.0",
        "hf_transfer>=0.1.0",
        "psutil>=5.9.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "llama-chat=app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml"],
    },
    keywords="llama, ai, chat, local, inference, streamlit",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/llama-chat-interface/issues",
        "Source": "https://github.com/yourusername/llama-chat-interface",
        "Documentation": "https://github.com/yourusername/llama-chat-interface#readme",
    },
) 