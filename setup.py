from setuptools import setup, find_packages

setup(
    name= "app",
    version= "1.0.0",
    packages= find_packages(),
    install_requires= [
        "streamlit"
    ]
)