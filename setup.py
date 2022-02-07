import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='vectors2d',
    packages=setuptools.find_packages(),
    version='1.0.2',
    license='MIT',
    description='A small but useful module that allows to work with vectors in the 2-dimensional space.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Dmytro Popov',
    author_email='thedmitryp@ukr.net',
    url='https://github.com/MitryP/vectors',
    download_url='https://github.com/MitryP/vectors/archive/1.0.2.tar.gz',
    keywords=['vectors', '2-dimensional', 'flat', 'coordinates', 'open-source'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)
