import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymenu-console",
    version="0.2.1",
    author="luanws",
    author_email="luan.w.silveira@gmail.com",
    description="Python console menu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luanws/pymenu",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'termcolor',
        'readchar'
    ],
    python_requires='>=3.7',
)
