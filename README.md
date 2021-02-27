# Qhack challenge 문제풀이 
이번 년도 2월에 pennylane에서 양자컴퓨팅challenge가([Qhack](https://github.com/XanaduAI/QHack)) 시작했습니다 \
총 12문제로 양자컴퓨팅과 관련된 문제로 구성되어 있었습니다 \
저는 그중 8문제를 풀었고 전체에서 148등을 기록을 하였습니다
![socreboard](./images/scoreboard.png)
여기서 문제에 대한 해답을 공유할려고 합니다
| 문제이름      | 풀이여부       |
| ----------- | ----------- |
| Simple Circuits 20 | :white_check_mark:|
| Simple Circuits 30 | :white_check_mark:|
| Simple Circuits 50 | :white_check_mark:|
| Circuit Training 100 | :white_check_mark:|
| Circuit Training 200 | :white_check_mark:|
| Circuit Training 500 | :x:|
| Quantum Gradients 100 | :white_check_mark:|
| Quantum Gradients 200 | :white_check_mark:|
| Quantum Gradients 500 | :white_check_mark:|
| VQE 100 | :x:|
| VQE 200 | :x:|
| VQE 500 | :x:|
각 문제들은 다음과 같이 실행을 하면 출력이 됩니다 
~~~shell
python solution.py < 1.in
~~~
모든 문제풀이는 [PennyLane](https://pennylane.ai/)을 참고해서 했습니다 
# 후기
진짜 양자컴을 이용하는 건 아니지만 가상으로 양자컴을 시뮬레이션 할 수 있는 라이브러리가 있어서 좋았습니다 \
처음에는 PennyLane api 탐구하는라 삽질한게 좀 많았습니다 \
양자컴퓨팅 머신러닝 다큐먼트가 잘 기술되어 있어서 이해하기 쉬었지만 api 다큐먼트는 불친절한 느낌은 있었습니다 \
앞으로 이걸로 여러 회로들을 시뮬레이션 해봐야 할 것 같습니다 
~~조금만 더 했으면 vqe까지 했을 텐데 아쉽네요~~

