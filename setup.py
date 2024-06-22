from setuptools import setup, find_packages

setup(
    name='mcqgen',
    version='0.1',
    author='Tapas Das',
    author_email='tapas.bosta@gmail.com',
    packages=find_packages(),
    install_requires=[
        'openai',
        'langchain',
        'python-dotenv',
        'streamlit',
        'PyPDF2'
    ],
)
