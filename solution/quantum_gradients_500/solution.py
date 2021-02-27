#! /usr/bin/python3
import sys
import pennylane as qml
from pennylane import numpy as np
from pennylane.templates.broadcast import wires_ring
from semantic_version.base import validate

# DO NOT MODIFY any of these parameters
a = 0.7
b = -0.3
dev = qml.device("default.qubit", wires=3)


def natural_gradient(params):
    """Calculate the natural gradient of the qnode() cost function.

    The code you write for this challenge should be completely contained within this function
    between the # QHACK # comment markers.

    You should evaluate the metric tensor and the gradient of the QNode, and then combine these
    together using the natural gradient definition. The natural gradient should be returned as a
    NumPy array.

    The metric tensor should be evaluated using the equation provided in the problem text. Hint:
    you will need to define a new QNode that returns the quantum state before measurement.

    Args:
        params (np.ndarray): Input parameters, of dimension 6

    Returns:
        np.ndarray: The natural gradient evaluated at the input parameters, of dimension 6
    """

    def fubu_mat(params,orig, i,j):
        shifted=params.copy()
        u_i = np.zeros(len(params))
        u_i[i]=1
        u_j =np.zeros(len(params)) 
        u_j[j]=1

        pp_1=prob(shifted+np.pi/2*(u_i+u_j))
        p_1=np.dot(orig,pp_1.conjugate())
        p_1= p_1.real**2 + p_1.imag**2

        pp_2=prob(shifted+np.pi/2*(u_i-u_j))
        p_2=np.dot(orig,pp_2.conjugate())
        p_2= p_2.real**2 + p_2.imag**2

        pp_3 =prob(shifted+np.pi/2*(-u_i+u_j))
        p_3=np.dot(orig,pp_3.conjugate())
        p_3= p_3.real**2 + p_3.imag**2
        
        pp_4 =prob(shifted-np.pi/2*(u_i+u_j))
        p_4=np.dot(orig,pp_4.conjugate())
        p_4= p_4.real**2 + p_4.imag**2
        
        return 0.125 * ( -p_1 +p_2 +p_3-p_4)

    natural_grad = np.zeros(6)
    # gradient = np.zeros([6], dtype=np.float64)

    # for i in range(len(params)):
    #     f,b=parameter_shift_term(params, i)
    #     gradient[i] = 0.5 *(f-b)

    gradient =qml.grad(qnode, argnum=0)(params)
    # print(qml.metric_tensor(qnode,diag_approx=True)(params))
    f_mat = np.zeros([6, 6], dtype=np.float64)
    orig=prob(params)
    for i in range(len(params)):
        for j in range(len(params)):
            f_mat[i,j]=fubu_mat(params,orig,i,j)

    f_inv= np.linalg.pinv(f_mat)
    for i in range(len(params)):
        natural_grad[i]=np.dot(f_inv[i],gradient)

    # QHACK #

    # QHACK #

    return natural_grad


def non_parametrized_layer():
    """A layer of fixed quantum gates.

    # DO NOT MODIFY anything in this function! It is used to judge your solution.
    """
    qml.RX(a, wires=0)
    qml.RX(b, wires=1)
    qml.RX(a, wires=1)
    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[1, 2])
    qml.RZ(a, wires=0)
    qml.Hadamard(wires=1)
    qml.CNOT(wires=[0, 1])
    qml.RZ(b, wires=1)
    qml.Hadamard(wires=0)


def variational_circuit(params):
    """A layered variational circuit composed of two parametrized layers of single qubit rotations
    interleaved with non-parameterized layers of fixed quantum gates specified by
    ``non_parametrized_layer``.

    The first parametrized layer uses the first three parameters of ``params``, while the second
    layer uses the final three parameters.

    # DO NOT MODIFY anything in this function! It is used to judge your solution.
    """
    non_parametrized_layer()
    qml.RX(params[0], wires=0)
    qml.RY(params[1], wires=1)
    qml.RZ(params[2], wires=2)
    non_parametrized_layer()
    qml.RX(params[3], wires=0)
    qml.RY(params[4], wires=1)
    qml.RZ(params[5], wires=2)


@qml.qnode(dev)
def qnode(params):
    """A PennyLane QNode that pairs the variational_circuit with an expectation value
    measurement.

    # DO NOT MODIFY anything in this function! It is used to judge your solution.
    """
    variational_circuit(params)
    return qml.expval(qml.PauliX(1))

@qml.qnode(dev)
def prob(params):
    variational_circuit(params)
    return qml.state()


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block

    # Load and process inputs
    params = sys.stdin.read()
    params = params.split(",")
    params = np.array(params, float)

    updated_params = natural_gradient(params)

    print(*updated_params, sep=",")
