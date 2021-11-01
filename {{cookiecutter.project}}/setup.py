from setuptools import setup, find_packages

setup(
    name="{{cookiecutter.project_slug}}",
    version="0.0.1",
    packages=find_packages(exclude=(['tests*'])),
    description="{{cookiecutter.description}}",
    author='Lloyd Hamilton',
    author_email='lloyd.lm.hamilton@gmail.com'
)
