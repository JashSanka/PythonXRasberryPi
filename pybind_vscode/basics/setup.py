from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import pybind11


ext_modules = [
Extension(
"example",
["example.cpp"],
include_dirs=[pybind11.get_include()],
language="c++",
extra_compile_args=["-std=c++17"],
),
]


setup(
name="example",
version="0.0.1",
ext_modules=ext_modules,
cmdclass={"build_ext": build_ext},
zip_safe=False,
)