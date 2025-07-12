from setuptools import setup, find_packages

setup(
    name="hauswerk",
    version="0.1",
    description="Modular visual toolkit for media plugins (PyQt6)",
    author="Jouw Naam",
    packages=find_packages(),
    install_requires=[
        "PyQt6",
        "opencv-python",
        "Pillow",
        "numpy",
        "ffmpeg-python"
    ],
    entry_points={
        "console_scripts": [
            "hauswerk=__main__:main"
        ]
    },
    include_package_data=True,
)
