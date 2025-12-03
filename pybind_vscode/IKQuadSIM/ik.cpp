#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <cmath>
#include <utility>

namespace py = pybind11;

// 2-DOF IK function
std::pair<double, double> ik_2dof(double x, double y, double L1, double L2) {
    // Distance from hip to foot
    double dist = std::sqrt(x*x + y*y);

    // Law of cosines for knee angle
    double cos2 = (dist*dist - L1*L1 - L2*L2) / (2 * L1 * L2);
    cos2 = std::clamp(cos2, -1.0, 1.0);
    double theta2 = std::acos(cos2);

    // Hip angle
    double k1 = L1 + L2 * std::cos(theta2);
    double k2 = L2 * std::sin(theta2);
    double theta1 = std::atan2(y, x) - std::atan2(k2, k1);

    return {theta1, theta2}; // in radians
}

// Expose module to Python
PYBIND11_MODULE(ik_module, m) {
    m.doc() = "2-DOF IK solver for quadruped leg";

    m.def("ik_2dof", &ik_2dof, "Solve 2-DOF IK",
          py::arg("x"), py::arg("y"), py::arg("L1"), py::arg("L2"));
}
