from setuptools import setup, find_packages

setup(
    name="viscpm",
    version="0.0.0",
    author="OpenBMB",
    author_email="openbmb@gmail.com",
    description="viscpm model for vision-language understanding and generation",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "torch>=1.10",
        "bmtrain>=0.2.0",
        "jieba",
        "tqdm",
        "tensorboard",
        "numpy>=1.21.0",
        "diffusers>=0.15.0",
        "jieba>=0.42.1",
        "matplotlib>=3.7.1",
        "numpy>=1.22.3",
        "opencv_python>=4.7.0.72",
        "pandas>=2.0.0",
        "Pillow>=9.5.0",
        "psutil>=5.9.0",
        "pydantic>=1.10.7",
        "scipy>=1.10.1",
        "setuptools>=65.5.0",
        "timm>=0.4.12",
        "torch>=1.13.1",
        "torchscale>=0.2.0",
        "torchvision>=0.14.1",
        "tqdm>=4.64.1",
        "transformers>=4.28.0",
        "typing_extensions>=4.5.0",
        "bminf",
    ],
    package_data={
        "viscpm": ["cpm_tokenizers/vocabs/*.txt"],
        "config": ["*.json"]
    },
    include_package_data=True
)
