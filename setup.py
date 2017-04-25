from setuptools import setup

setup(
    name='webdriver-chauffeur',
    version='0.1.1',
    description='Convenience functions for using Selenium Webdriver',
    url='https://github.com/codyc4321/webdriver_chauffeur',
    author='codyc4321',
    author_email='cchilder@mail.usf.edu',
    license='MIT',
    packages=['webdriver_chauffeur'],
    install_requires=[
        'bs4', 'selenium'
    ],
    zip_safe=False,
)
