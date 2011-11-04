from setuptools import setup, find_packages

version = "0.0.0"

setup(
    name = 'django-cms-pictures',
    version = version,
    description = 'Django CMS Pictures Plugins',
    author = 'Pablo Saavedra',
    author_email = 'pablo.saavedra@treitos.com',
    url = 'http://github.com/psaavedra/django-cms-pictures',
    packages = find_packages(),
    package_data={
        'cms_pictures_polaroid': [
            'templates/cms_pictures_polaroid/*.html',
        ],
        'cms_pictures_slider': [
            'templates/cms_pictures_slider/*.html',
        ],
    },
    zip_safe=False,
    install_requires=[
        "django-cms>=2.1",
    ]
)
