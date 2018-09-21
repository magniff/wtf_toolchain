import setuptools


classifiers = [
    (
        'Programming Language :: Python :: %s' % x
    )
    for x in '3.1 3.2 3.3 3.4 3.5'.split()
]


setuptools.setup(
    name='wtf_toolchain',
    description='JIT powered BF interpreter and a custom compiler.',
    version='0.1.0',
    license='MIT license',
    platforms=['unix', 'linux'],
    keywords=['brainfuck', 'jit'],
    author='magniff',
    url='https://github.com/magniff/wtf_toolchain',
    classifiers=classifiers,
    packages=setuptools.find_packages(),
    install_requires=[
        'watch', 'funcparserlib', 'pytest', 'click',
    ],
    entry_points={
        'console_scripts': [
            'wtf_compile=bin.wtf_compile:main',
        ]
    },
    zip_safe=False,
)

