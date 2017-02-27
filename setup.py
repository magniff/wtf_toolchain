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
            'wtf=bin.wtf:main',
            'wtf_capture_specification=bin.wtf_capture_specification:main',
            'wtf_compile=bin.wtf_compile:main',
            'wtf_build_vm=bin.wtf_build_vm:main',
        ]
    },
    zip_safe=False,
)
