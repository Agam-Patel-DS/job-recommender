from setuptools import setup, find_packages

# Read the contents of requirements.txt
with open("requirements.txt", "r") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("-e")]

setup(
    name="job-recommender",
    version="0.1.0",
    author="Your Name",
    author_email="your_email@example.com",
    description="A modular job recommendation system using machine learning and NLP.",
    long_description="A detailed job recommendation project.",
    long_description_content_type="text/plain",
    url="https://github.com/yourusername/job-recommender",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
