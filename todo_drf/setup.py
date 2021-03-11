from setuptools import setup, find_packages

setup(
    name             = 'doro16rest',
    version          = '1.0.0',
    description      = 'practice',
    # long_description = open('README.md').read(),
    author           = 'doro16',
    author_email     = 'doro16@dtaas.co.kr',
    url              = 'https://github.com/doro16/rest',
    download_url     = 'https://github.com/doro16/rest/#files',
    install_requires = ['djangorestframework', 'requests', 'django-allauth', 'django-rest-auth'],
    packages         = find_packages(exclude = ['docs', 'example']),
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)