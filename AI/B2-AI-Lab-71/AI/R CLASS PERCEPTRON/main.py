import numpy as np
import copy


c = 1 # ! Learning rate is 1


def signum(value):
    if value > 0:
        return 1
    else:
        return -1


T = [
    [0.1, 0.1, -1, 1],
    [0.2, 0.1, -1, 1],
    [0.5, 0.1, -1, 2],
    [0.6, 0.1, -1, 2],
    [0.3, 0.3, -1, 3],
    [0.4, 0.3, -1, 3]
    ]

input_vector = np.array(T)

D = [
    [1, -1, -1],
    [-1, 1, -1],
    [-1, -1, 1]
]

W = [[-0.1, 0.15, 0.2],
    [-0.2, 0.11, 0.17],
    [0.17, 0.16, 0.11]
    ]


dimension = 2

def calculateNet(x, w):
    net = 0
    for i in range(len(x)):
        net += x[i] * w[i]
    return net


for i in range(len(T)):
    _input = input_vector[i]
    d = _input[dimension + 1]
    _input = _input[: dimension + 1]

    o = []
    for j in range(len(W)):
        _W = W[j]
        net = calculateNet(_input, _W)
        output = signum(net)
        o.append(output)

    temp = []  # ! Array to store the index of the update weight vectors 
    _w = []
    count = 0
    for k in range(len(o)):
        flag = np.array(W[count]) + c * (d - o[k]) * np.array(_input)
        _w.append(flag)
        count = count + 1
    print(_w)
    
        
            



            


    print(o)
    print("-------------------------------------------")
        







    



