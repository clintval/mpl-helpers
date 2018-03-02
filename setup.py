from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
    long_description = long_description.replace('\r', '')
except (ImportError, OSError):
    import io
    with io.open('README.md', encoding='utf-8') as f:
        long_description = f.read()


setup(
    name='mpl_helpers',
    packages=['mpl_helpers'],
    version='0.1.0',
    description='A Python 3.6 library for tweaking matplotlib figures.',
    long_description=long_description,
    author='clintval',
    author_email='valentine.clint@gmail.com',
    url='https://github.com/clintval/mpl-helpers',
    download_url='https://github.com/clintval/mpl-helpers/archive/v0.1.0.tar.gz',
    py_modules=['mpl_helpers'],
    install_requires=[
        'matplotlib',
        'numpy',
    ],
    extras_require={
        'ci': ['nose', 'codecov'],
        'fancytest': ['nose', 'nose-progressive', 'coverage'],
    },
    license='MIT',
    zip_safe=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ]
)
