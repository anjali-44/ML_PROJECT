from setuptools import find_packages, setup

def get_requirements(file_path):
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-e')]
    return requirements

setup(
    name='ML_Project',
    version='0.0.1',
    author='Anjali',
    author_email='anjalisharmarbt@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
