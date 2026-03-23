import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='Web_Scrapping_Tool',
    version='1.0.47',
    author="Richard Raphael Banak",
    description="Robot Specialist Library for Robot Process Automation",
    url="https://github.com/Richardbnk/Web_Scrapping_Tool",
    packages=['web_scrapping',],
    
    py_modules = ['selenium'],
    
    
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[required],
)
