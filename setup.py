import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="esprsim",
    version="1.0.0", # see https://semver.org/ for how to version properly
    author="Achim Geissler",
    author_email="achim.geissler@fhnw.ch",
    description="Simulation scripts for running ESP-r",
    long_description=long_description,
    long_description_content_type="text/markdown",
#    url="https://gitlab.fhnw.ch/gebopt/code/sia380",
    project_urls={ },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    package_data={},
    include_package_data=False,
    python_requires=">=3.8",
    install_requires=[
        "humanfriendly",
        "pandas",
        "matplotlib",
        "pathlib"
    ]
)
