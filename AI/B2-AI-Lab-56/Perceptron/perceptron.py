import numpy as np

c = 1  # Define the global variable c

def signum(sum_val):
    if sum_val > 0:
        return 1
    return -1

def netFunc(X, d, W):
    global e, c, cycle  # Declare c as a global variable
    e = np.inf
    while e > 0:
        i = 0
        O = 0
        e = 0
        for i in range(3):
            sum_val = np.dot(W, X[i]) #multiplying input and weight
            O = signum(sum_val) #defining signum
            e += abs(d[i] - O)
            for k in range(len(W)):
                W[k] += c * (d[i] - O) * X[i][k] #formula for weight change
            print(W)
        print(e)
        cycle += 1

if __name__ == "__main__":
    cycle = 1

    X = np.array([[1, -2, 1.5, 0], [1, -0.5, -2, -1.5], [0, 1, -1, 1.5]])
    d = [1, -1, 1]
    W = [1, -1, 0, 0.5]

    netFunc(X, d, W)
