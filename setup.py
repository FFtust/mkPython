import setuptools 
from mkPython import mkPython_version

setuptools.setup(name='mkPython',
      version=mkPython_version,
      description='python lib for makeblock',
      url='https://github.com/FFtust/mkPython',
      author='FFtust',
      author_email='fanfei@makeblock.com',
      license='MIT',
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
)
