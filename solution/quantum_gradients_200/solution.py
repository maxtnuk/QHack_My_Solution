#! /usr/bin/python3

import sys
import pennylane as qml
import numpy as np


def gradient_200(weights, dev):
    r"""This function must compute the gradient *and* the Hessian of the variational
    circuit using the parameter-shift rule, using exactly 51 device executions.
    The code you write for this challenge should be completely contained within
    this function between the # QHACK # comment markers.

    Args:
        weights (array): An array of floating-point numbers with size (5,).
        dev (Device): a PennyLane device for quantum circuit execution.

    Returns:
        tuple[array, array]: This function returns a tuple (gradient, hessian).

            * gradient is a real NumPy array of size (5,).

            * hessian is a real NumPy array of size (5, 5).
    """
    def parameter_shift_term(qnode, params, i):
        shifted = params.copy()
        shifted[i] += np.pi/2
        forward = qnode(shifted)  # forward evaluation

        shifted[i] -= np.pi
        backward = qnode(shifted) # backward evaluation

        return forward, backward


    def parameter_second(qnode, params,grads,orig, i,j):
        shifted=params.copy()
        u_i = np.zeros(len(params))
        u_i[i]=1
        u_j =np.zeros(len(params)) 
        u_j[j]=1
        f,b = grads
        if i==j:
            return 0.5 * (b[i]- 2*orig+ f[i])
        else:
            i_1=qnode(shifted+np.pi/2*(u_i+u_j))
            i_4=qnode(shifted-np.pi/2*(u_i+u_j))
            i_2=qnode(shifted+np.pi/2*(-u_i+u_j))
            i_3=qnode(shifted+np.pi/2*(u_i-u_j))
            return  0.25 * (i_1 - i_2 - i_3 + i_4)
        

    @qml.qnode(dev)
    def circuit(w):
        for i in range(3):
            qml.RX(w[i], wires=i)

        qml.CNOT(wires=[0, 1])
        qml.CNOT(wires=[1, 2])
        qml.CNOT(wires=[2, 0])

        qml.RY(w[3], wires=1)

        qml.CNOT(wires=[0, 1])
        qml.CNOT(wires=[1, 2])
        qml.CNOT(wires=[2, 0])

        qml.RX(w[4], wires=2)

        return qml.expval(qml.PauliZ(0) @ qml.PauliZ(2))

    gradient = np.zeros([5], dtype=np.float64)
    hessian = np.zeros([5, 5], dtype=np.float64)
    
    # i - pi/2
    forwards=[]
    # i + pi/2
    backwards=[]

    for i in range(len(weights)):
        f,b=parameter_shift_term(circuit, weights, i)
        forwards.append(f)
        backwards.append(b)
        gradient[i] = 0.5 *(f-b)

    orig=circuit(weights)
    for i in range(len(weights)):
        for j in range(i,len(weights)):
            val=parameter_second(circuit, weights,(forwards,backwards),orig, i,j)
            hessian[i,j]=float(val)
            if i!=j:
                hessian[j,i]=float(val)
    # QHACK #

    # QHACK #

    return gradient, hessian, circuit.diff_options["method"]


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    weights = sys.stdin.read()
    weights = weights.split(",")
    weights = np.array(weights, float)

    dev = qml.device("default.qubit", wires=3)
    gradient, hessian, diff_method = gradient_200(weights, dev)

    print(
        *np.round(gradient, 10),
        *np.round(hessian.flatten(), 10),
        dev.num_executions,
        diff_method,
        sep=","
    )
