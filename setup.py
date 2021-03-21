import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

install_requires = [
    "abjad",
]

keywords = [
    "abjad",
    "music composition",
    "music notation",
    "lilypond",
]

setuptools.setup(
    name="a_rua_dos_cataventos",
    version="0.1",
    author="Davi Raubach Tuchtenhagen",
    author_email="raubachdavi@gmail.com",
    description="for ensemble",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DaviRaubach/a_rua_dos_cataventos",
    install_requires=install_requires,
    keywords=", ".join(keywords),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
