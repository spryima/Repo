from setuptools import setup

setup(
        name='clean_folder',
        version='1.0.2',
        description='Script to sort your files and clean one folder',
        url='http://github.com/dummy_user/useful',
        author='Sergii Pryima',
        packages=['clean_folder'],
        entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']}
    )
    