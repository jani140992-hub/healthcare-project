from setuptools import setup, find_packages

setup(
    name="carepulse-ehr",
    version="2.4.0",
    description="Enterprise Healthcare Information System and Electronic Health Record Platform",
    author="CarePulse Health Technologies",
    author_email="engineering@carepulse.health",
    license="Proprietary",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "fastapi>=0.110.0",
        "uvicorn>=0.28.0",
        "pydantic>=2.6.0",
        "sqlalchemy>=2.0.28",
        "cryptography>=42.0.0"
    ],
    extras_require={
        "test": [
            "pytest>=8.0.0"
        ]
    },
    entry_points={
        "console_scripts": [
            "carepulse-server=scripts.run_server:main",
            "carepulse-seed=scripts.seed_database:seed",
            "carepulse-loc=scripts.count_loc:main"
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ]
)
