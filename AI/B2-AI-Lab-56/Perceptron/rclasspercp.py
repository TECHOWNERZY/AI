T = [[0.1,0.1,-1,1],
     [0.2,0.1,-1,1],
     [0.5,0.1,-1,2],
     [0.6,0.1,-1,2],
     [0.3,0.3,-1,3],
     [0.4,0.3,-1,3]]

w = [[-0.1,0.15,0.2],
     [-0.2,0.11,0.17],
     [0.17,0.16,0.11]]

d = [[1,-1,-1],
     [-1,1,-1],
     [-1,-1,1]]
e = [1,1,1]
counter = 0
c=1
def sgn(net):
    if(net>0):
        return 1
    else:
        return -1
error  =1

while(counter<100 or error==0):
    e=[0,0,0]
    for k in range(6):
      o = [0,0,0]
      for i in range (3):
        sum = 0
        for j in range (3):
          net=T[k][j]*w[i][j]
          sum = sum + net
        o[i]=sgn(sum)
      for l in range (3):
         s=T[k][3]-1
         for m in range (3):
           w[l][m] = w[l][m] + 0.5*((d[s][l])-(o[m]))*(T[k][m])       
         e[l] = e[l] + 0.5*((d[s][l]) - o[l])*((d[s][l]) - o[l]) 
         error = e[0] + e[1] + e[2] 
         
      # print(f"updated weights for epoch {counter+1} input vector {k+1} is \n {w}")
    print(f"error \n {error}")
    counter = counter + 1
    print(f"epoch {counter}")
    print("===============================")
print(f"updated weights for epoch 100 is \n {w}")
    
       
       
        
          
    