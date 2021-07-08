from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()
  
long_description = 's3util package'
  
setup(
        name ='s3util',
        version ='0.0.1',
        author ='Karan Pratap Singh',
        author_email ='karanpratapsingh43@gmail.com',
        url ='https://github.com/karannaoh/s3util',
        description ='s3util.',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                's3util = s3util.main:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords ='s3util s3',
        install_requires = requirements,
        zip_safe = False
)