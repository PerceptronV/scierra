import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scierra",
    version="0.1",
    author="PerceptronV",
    author_email="neutrinovs@gmail.com",
    description="A Simulated C++ Interpreter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PerceptronV/scierra",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts':[
            'scierra = scierra.scierra:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Interpreters",
        "Development Status :: 4 - Beta",
        "Natural Language :: English"
    ],
    python_requires='>=3.3',
)