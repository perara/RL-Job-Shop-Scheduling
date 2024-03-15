from setuptools import setup, find_packages

setup(
    name='JSS',  # Package name
    version='0.1.0',  # Version number
    author='Per-Arne Andersen',  # Your name
    author_email='per.andersen@uia.no',  # Your email
    description='A brief description of JSS package',  # A short description
    packages=find_packages(),  # Automatically find package directories
    install_requires=[  # List of dependencies
        # 'numpy>=1.18.1',
        # 'pandas>=1.0.3',
    ],
    classifiers=[  # Classifiers help users find your project
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',  # Minimum version requirement of the package
)
