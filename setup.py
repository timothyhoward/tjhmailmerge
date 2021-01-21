import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tjhmailmerge",
    version="1.0.0",
    author="Timothy Howard",
    author_email="timothyhoward@outlook.com",
    description="Flexible mail merge script to merge records from a spreadsheet into Outlook email form.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/timothyhoward/tjhmailmerge",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)