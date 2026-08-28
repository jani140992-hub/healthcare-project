from setuptools import setup, find_packages

setup(
    name="carepulse-ehr",
    version="2.4.0",
    description="Enterprise Healthcare Information System and Electronic Health Record Platform (HL7 FHIR R4, ICD-10, LOINC, RxNorm, HIPAA Compliant)",
    author="CarePulse Health Technologies",
    author_email="engineering@carepulse.health",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        # Zero required external dependencies for core engine
    ],
    extras_require={
        "prod": [
            "fastapi>=0.110.0",
            "uvicorn[standard]>=0.28.0",
            "pydantic>=2.6.0",
            "sqlalchemy>=2.0.28"
        ],
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
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ]
)
