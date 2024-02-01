from setuptools import setup, find_packages

setup(
    name='tkwinterm',
    version='0.1.0',
    author='Scott Peterman',
    author_email='scottpeterman@gmail.com',
    description='''A fully functional terminal emulator application for Windows, built on Python, Tkinnter and Pyte''',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/scottpeterman/tkwinterm',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[

        'pywinpty>=2.0.12',
        'sv-ttk>=2.6.0',
        'pyte>=0.8.2',
        'wcwidth>=0.2.13'
    ],
    entry_points={
        'console_scripts': [
            'tkwinterm=tkwinterm.main_winpty:run'
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    # You can specify package data files and directories
    package_data={
        # Include any *.txt or *.rst files found in your package:
        '': ['*.txt', '*.rst'],
    },
)
