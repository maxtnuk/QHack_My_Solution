# 문제풀이
이와 같이 회로를 구성하면 됩니다
```python
@qml.qnode(device,interface=None)
def circit(angle):
    qml.RY(angle,wires=0)
    return qml.expval(qml.PauliX(wires=0))
```
그리고 실행하면 됩니다 
