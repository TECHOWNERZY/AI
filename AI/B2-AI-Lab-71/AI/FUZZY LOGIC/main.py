import numpy as np

import matplotlib.pyplot as plt

def assignMembership(value):
    if value == 0:
        return 1
    elif value < 1 and value > 0:
        return 1 - value
    else :
        return 0



def distance(x, y):
    return np.sqrt((0.5 - x)**2 + (0.5 - y)**2)

def membership():
    values = []
    x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    y = [0.1, 0.1, 0.3, 0.3, 0.1, 0.1]

    for i in range(len(x)):
        for j in range(len(y)):
            values.append(assignMembership(distance(x[i], y[j])))
    

    print("The memebership values are :")
    for i in values:
        print(i)
    
    plt.plot(values, marker = 'o')
    plt.markersize = 10
    plt.show()

membership()
    





