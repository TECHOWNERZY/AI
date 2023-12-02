import numpy as np

print("Enter board state")
tictac = np.empty((3, 3), dtype=str)
count = 0
for i in range(3):
    for j in range(3):
        tictac[i][j] = input()
        if tictac[i][j] == "X":
            count += 1

print(count)
vector = np.zeros(9, dtype=int)
if abs(count - 3) == 1:
    k = 0
    for i in range(3):
        for j in range(3):
            if tictac[i][j] == "X":
                vector[k] = 1
            elif tictac[i][j] == "O":
                vector[k] = 2
            else:
                vector[k] = 0
            k += 1

    new_arr = np.arange(8, -1, -1)
    sum_val = np.dot(vector, np.power(3, new_arr))
    list_form=vector.tolist()
    print(list_form)
    print(sum_val)

