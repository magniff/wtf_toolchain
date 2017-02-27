import setuptools


classifiers = [
    (
        'Programming Language :: Python :: %s' % x
    )
    for x in '3.1 3.2 3.3 3.4 3.5'.split()
]


setuptools.setup(
    name='bfpypy',
    description='description',
    version='0.1.0',
    license='MIT license',
    platforms=['unix', 'linux', 'osx', 'win32'],
    keywords=[],
    author='magniff',
    url='https://github.com/magniff/bfpypy',
    classifiers=classifiers,
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'wtf_compile=bin.wtf_compile:main',
        ]
    },
    zip_safe=False,
)
