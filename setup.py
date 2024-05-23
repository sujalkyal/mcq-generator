from setuptools import setup,find_packages

setup(
    name='MCQGenerator',
    author='Sujal Kyal',
    version='0.0.1',
    author_email='sujalkyal2704@gmail.com',
    install_requires=['openai','langchain','streamlit','python-dotenv','PyPDF2'],
    packages=find_packages()
)