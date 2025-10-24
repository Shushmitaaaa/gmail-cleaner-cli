from setuptools import setup, find_packages

setup(
    name='gmail-cleaner',
    version='0.1',
    py_modules=['main'],
    packages=find_packages(),
    install_requires=[
        'click',
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib',
        'python-dotenv',
        'google-generativeai',
    ],
    entry_points={
        'console_scripts': [
            'gmailcleaner=main:cli',
        ],
    },
)
