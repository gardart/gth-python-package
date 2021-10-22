from setuptools import setup, find_packages

setup(
    name="gth-timechecker",
    version="0.0.9",
    author="Garðar Þorsteinsson",
    author_email="gardart@gmail.com",
    url="https://example.com",
    description="An aplication that informs you of the time in different locations and timezones",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "pytz"],
    entry_points={"console_scripts": ["timechecker = src.main:main"]},
)
