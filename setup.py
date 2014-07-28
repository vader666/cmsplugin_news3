from setuptools import setup, find_packages

setup(
    name='cmsplugin_news3',
    version='0.0.2',
    packages=find_packages(),
    url='https://github.com/vader666/cmsplugin_news3',
    license='',
    author='Anton Chertikovtzev',
    author_email='anton.chertikovtcev@gmail.com',
    description='News plugin and application for Django-CMS 3.x',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'easy-thumbnails >= 2.0',
        'django-filer',
    ]
)

