from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.2',
    description='Code, used for cleaning and sorting objects inside your messy folder',
    url='https://github.com/Plvrnnk/Sorting-data-objects-inside-your-folder-part-2-.git',
    author='Plvrnnk',
    author_email='polina.lavrynenko2005@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    data_files=['clean.py'],
    include_package_data=True,
    entry_points= {'console_scripts': ['clean-folder=clean_folder.clean:run']}
)
