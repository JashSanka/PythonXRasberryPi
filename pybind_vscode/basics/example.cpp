#include <pybind11/pybind11.h>
namespace py = pybind11;


int add(int a, int b) {
return a + b;
}


PYBIND11_MODULE(example, m) {
m.doc() = "example module built with pybind11";
m.def("add", &add, "Add two integers");
}