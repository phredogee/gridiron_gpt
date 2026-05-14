from setuptools import setup
setup(
    name='zodiac',
    version='1.0.0',
    packages=['zodiac'],
    entry_points={
        'console_scripts': [
        'zodiac = zodiac.zodiac_cli:run_cli',
        ],
     },
    author='phred',
    description='🧧 Chinese Zodiac CLI with emoji-tiered feedback and interactive prompts',
)

install_requires=[
    "requests>=2.0.0",
    # Add others as needed
],

package_data={
    "zodiac": ["data/*.json"]
},
include_package_data=True,
python_requires='>=3.7',
