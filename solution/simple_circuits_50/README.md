# 문제풀이
이와 같이 회로를 구성하면 됩니다
```python
@qml.qnode(device,interface=None)
def circit(angle):
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0,1])
    qml.RY(angle,wires=0)
    return qml.expval(qml.PauliZ(0) @  qml.PauliZ(1))
```
그리고 실행하면 됩니다 
