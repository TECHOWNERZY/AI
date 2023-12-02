import numpy as np

# Define the algorithm parameters
c = 1
max_epochs = 10000

# Input data
T = np.array([
    [0.1, 0.1, -1, 1],
    [0.2, 0.1, -1, 1],
    [0.5, 0.1, -1, 2],
    [0.6, 0.1, -1, 2],
    [0.3, 0.3, -1, 3],
    [0.4, 0.3, -1, 3]
])

# Desired outputs for each class
D = np.array([
    [1, -1, -1],
    [-1, 1, -1],
    [-1, -1, 1]
])

# Initial weight matrix
W = np.array([
    [-0.1, 0.15, 0.2],
    [-0.2, 0.11, 0.17],
    [0.17, 0.16, 0.11]
])

def signum(value):
    if value > 0:
        return 1
    else :
        return -1

# Training loop
for _ in range(max_epochs):
    p = 1
    E = 0

    for p in range(1, len(T) + 1):
        temp = T[p - 1][-1]
        yp = T[p - 1][:-1]
        if(temp == 1):
            dp = D[0]
        elif (temp == 2):
            dp = D[1]
        else :
            dp = D[2]
        # print(np.dot(W, yp))
        
        oi = []

        for k in range(len(W)):
            net = signum(np.dot(W[k], yp))
            oi.append(net)
        print(oi)

        

        for i in range(len(W)):
            for j in range(len(W)):
                print("This is dpi - oi", dp[i] - oi[i])
                print(0.5 * c * (dp[i] - oi[i]) * yp[j])
                W[i][j] += 0.5 * c * (dp[i] - oi[i]) * yp[j]
        # Update weights for each component
        # for i in range(len(W)):
        #     W[i] += (1 / 2) * c * (dp[i] - oi[i]) * yp


        # print W
        print("This is W")
        print(W)

        # Update error

        E += 0.5 * np.sum((dp - oi)**2)
        print("Error for this epoch", E)
    if E == 0:
        print(f"Training converged at epoch {_ + 1}")
        break

    if p == len(T):
        p = 0

if E != 0:
    print("Training reached the maximum number of epochs")

# Print the trained weights
print("Trained Weights:")
print(W)
