from setuptools import setup, Extension
import pybind11

# C++ extension
ext_modules = [
    Extension(
        "ik_module",                # Python module name
        ["ik.cpp"],                 # Source file
        include_dirs=[pybind11.get_include()],  # pybind11 headers
        language="c++",
        extra_compile_args=["-std=c++17"]       # C++17 standard
    )
]

setup(
    name="ik_module",
    version="0.1",
    ext_modules=ext_modules
)
