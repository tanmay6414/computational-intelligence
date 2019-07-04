#----------------------------------------------------------------
#Name : Tanmay Pramod Varade
#Roll No: 36
#Block : B5
#Purpose : CI Lab Assignment 6 (Back Propagation Algoritm)
#Created : 20-03-2019
#----------------------------------------------------------------


import math

#defining all necessary matrices and variables
i1=[]
i2=[]
O=[]
Ol = [[0,0],[0,0]]
V  = [[0,0],[0,0]]
Vt  = [[0,0],[0,0]]
W  = [[0,0],[0,0]]
Ih = [[0,0],[0,0]]
Io = [[0,0],[0,0]]
Oh = [[0,0],[0,0]]
Wt = [[0,0],[0,0]]
y = [[0,0],[0,0]]
dW = [[0,0],[0,0]]
dV = [[0,0],[0,0]]
e = [[0,0],[0,0]]
dstar =  [[0,0],[0,0]]
dstart =  [[0,0],[0,0]]
X =  [[0,0],[0,0]]

#taking inputs for training set
num = input("Enter no. of inputs: ")
for i in range (num):
    i1num=input("Enter input for i1: ")
    i1.append(i1num)
print"I1: ", i1

for i in range (num):
    i2num=input("Enter input for i2: ")
    i2.append(i2num)
print "I2: ",i2

for i in range (num):
    Onum=input("Enter corresponding output: ")
    O.append(Onum)
print "O: ",O

#input for initial weights
n = input("Enter number of hidden neurons: ")

for i in range (n):
    for j in range (n):
        w = input("Enter weight (from input to hidden layer): ")
        V[i][j] = w
print "V: ",V

for i in range (n):
    w = input("Enter weight (from hidden layer to output): ")
    W[i][0] = w
print "W: ",W

#loop runs until all the inputs from training sers are over
for a in range (num):
    print "Epoch ",a+1," : "
    print "================"
    Ol[0][0] = i1[a]
    Ol[1][0] = i2[a]

    print "Ol: ",Ol

    for i in range(len(V)):
       for j in range(len(V[0])):
           Vt[j][i] = V[i][j]

    print "Vt: ",Vt

    for i in range(len(Vt)):
       for j in range(len(Ol[0])):
           for k in range(len(Ol)):
               Ih[i][j] += Vt[i][k] * Ol[k][j]
               Ih[i][j] = round(Ih[i][j],4)

    print "Ih: ",Ih

    for i in range (len(Ih)):
        for j in range (len(Ih[0])):
            if Ih[i][j] != 0:
                Oh[i][j] = 1/(1+ math.exp(-(Ih[i][j])))
                Oh[i][j] = round(Oh[i][j],4)
            else:
                Oh[i][j] = 0

    print "Oh: ", Oh

    for i in range(len(W)):
       for j in range(len(W[0])):
           Wt[j][i] = W[i][j]

    print "Wt: ", Wt

    for i in range(len(Wt)):
       for j in range(len(Oh[0])):
           for k in range(len(Oh)):
               Io[i][j] += Wt[i][k] * Oh[k][j]
               Io[i][j] = round(Io[i][j],4)

    print "Io: ",Io

    for i in range (len(Io)):
        for j in range (len(Io[0])):
            if Io[i][j] != 0:
                Oo = 1/(1+ math.exp(-(Io[i][j])))

    Oo = round(Oo,4)
    print "Oo: ",Oo

    Error = pow((O[a] - Oo),2)
    Error = round(Error,4)
    print "Error: ",Error

    d = ((O[a] - Oo)*(Oo)*(1 - Oo))
    d = round(d,4)
    print "d: ",d

    for i in range(len(Oh)):
       for j in range(len(Oh[0])):
           y[i][j] = Oh[i][j] * d
           y[i][j] = round(y[i][j],4)

    print "y: ",y

    for i in range(len(dW)):
       for j in range(len(dW[0])):
           dW[i][j] = y[i][j] * 0.6
           dW[i][j] = round(dW[i][j],4)

    print "dW: ",dW

    for i in range(len(e)):
       for j in range(len(e[0])):
           e[i][j] = W[i][j] * d
           e[i][j] = round(e[i][j],4)

    print "{e}: ",e

    for i in range(len(y)):
       for j in range(len(y[0])):
           dstar[i][j] = e[i][j] * y[i][j]
           dstar[i][j] = round(dstar[i][j],4)

    print "d*: ",dstar

    for i in range(len(dstar)):
       for j in range(len(dstar[0])):
           dstart[j][i] = dstar[i][j]

    for i in range(len(Ol)):
       for j in range(len(dstart[0])):
           for k in range(len(dstart)):
               X[i][j] += Ol[i][k] * dstart[k][j]
               X[i][j] = round(X[i][j],4)
    print "X: ",X

    for i in range(len(dV)):
       for j in range(len(dV[0])):
           dV[i][j] = X[i][j] * 0.6
           dV[i][j] = round(dV[i][j],4)
    print"dV: ",dV

    for i in range(len(V)):
       for j in range(len(V[0])):
           V[i][j] = V[i][j] + dV[i][j]
           V[i][j] = round(V[i][j],4)
    print "V: ",V

    for i in range(len(W)):
       for j in range(len(V[0])):
           W[i][j] = W[i][j] + dW[i][j]
           W[i][j] = round(W[i][j],4)
    print "W: ",W
    print "-----------------------------------------------"


#Output
'''
>>>
I1:  [0.4, 0.3, 0.6, 0.2, 0.1]
I2:  [-0.7, -0.5, 0.1, 0.4, -0.2]
O:  [0.1, 0.05, 0.3, 0.25, 0.12]
V:  [[0.1, 0.4], [-0.2, 0.2]]
W:  [[0.2, 0], [-0.5, 0]]
Epoch  1  :
================
Ol:  [[0.4, 0], [-0.7, 0]]
Vt:  [[0.1, -0.2], [0.4, 0.2]]
Ih:  [[0.18, 0.0], [0.02, 0.0]]
Oh:  [[0.5449, 0], [0.505, 0]]
Wt:  [[0.2, -0.5], [0, 0]]
Io:  [[-0.1435, 0.0], [0.0, 0.0]]
Oo:  0.4642
Error:  0.1326
d:  -0.0906
y:  [[-0.0494, -0.0], [-0.0458, -0.0]]
dW:  [[-0.0296, -0.0], [-0.0275, -0.0]]
{e}:  [[-0.0181, -0.0], [0.0453, -0.0]]
d*:  [[0.0009, 0.0], [-0.0021, 0.0]]
X:  [[0.0004, -0.0008], [-0.0006, 0.0015]]
dV:  [[0.0002, -0.0005], [-0.0004, 0.0009]]
V:  [[0.1002, 0.3995], [-0.2004, 0.2009]]
W:  [[0.1704, 0.0], [-0.5275, 0.0]]
-----------------------------------------------
Epoch  2  :
================
Ol:  [[0.3, 0], [-0.5, 0]]
Vt:  [[0.1002, -0.2004], [0.3995, 0.2009]]
Ih:  [[0.3103, 0.0], [0.0394, 0.0]]
Oh:  [[0.577, 0], [0.5098, 0]]
Wt:  [[0.1704, -0.5275], [0.0, 0.0]]
Io:  [[-0.3141, 0.0], [0.0, 0.0]]
Oo:  0.4221
Error:  0.1385
d:  -0.0908
y:  [[-0.0524, -0.0], [-0.0463, -0.0]]
dW:  [[-0.0314, -0.0], [-0.0278, -0.0]]
{e}:  [[-0.0155, -0.0], [0.0479, -0.0]]
d*:  [[0.0008, 0.0], [-0.0022, 0.0]]
X:  [[0.0006, -0.0015], [-0.001, 0.0026]]
dV:  [[0.0004, -0.0009], [-0.0006, 0.0016]]
V:  [[0.1006, 0.3986], [-0.201, 0.2025]]
W:  [[0.139, 0.0], [-0.5553, 0.0]]
-----------------------------------------------
Epoch  3  :
================
Ol:  [[0.6, 0], [0.1, 0]]
Vt:  [[0.1006, -0.201], [0.3986, 0.2025]]
Ih:  [[0.3506, 0.0], [0.2989, 0.0]]
Oh:  [[0.5868, 0], [0.5742, 0]]
Wt:  [[0.139, -0.5553], [0.0, 0.0]]
Io:  [[-0.5514, 0.0], [0.0, 0.0]]
Oo:  0.3655
Error:  0.0043
d:  -0.0152
y:  [[-0.0089, -0.0], [-0.0087, -0.0]]
dW:  [[-0.0053, -0.0], [-0.0052, -0.0]]
{e}:  [[-0.0021, -0.0], [0.0084, -0.0]]
d*:  [[0.0, 0.0], [-0.0001, 0.0]]
X:  [[0.0006, -0.0016], [-0.001, 0.0026]]
dV:  [[0.0004, -0.001], [-0.0006, 0.0016]]
V:  [[0.101, 0.3976], [-0.2016, 0.2041]]
W:  [[0.1337, 0.0], [-0.5605, 0.0]]
-----------------------------------------------
Epoch  4  :
================
Ol:  [[0.2, 0], [0.4, 0]]
Vt:  [[0.101, -0.2016], [0.3976, 0.2041]]
Ih:  [[0.2902, 0.0], [0.46, 0.0]]
Oh:  [[0.572, 0], [0.613, 0]]
Wt:  [[0.1337, -0.5605], [0.0, 0.0]]
Io:  [[-0.8185, 0.0], [0.0, 0.0]]
Oo:  0.3061
Error:  0.0031
d:  -0.0119
y:  [[-0.0068, -0.0], [-0.0073, -0.0]]
dW:  [[-0.0041, -0.0], [-0.0044, -0.0]]
{e}:  [[-0.0016, -0.0], [0.0067, -0.0]]
d*:  [[0.0, 0.0], [-0.0, 0.0]]
X:  [[0.0006, -0.0016], [-0.001, 0.0026]]
dV:  [[0.0004, -0.001], [-0.0006, 0.0016]]
V:  [[0.1014, 0.3966], [-0.2022, 0.2057]]
W:  [[0.1296, 0.0], [-0.5649, 0.0]]
-----------------------------------------------
Epoch  5  :
================
Ol:  [[0.1, 0], [-0.2, 0]]
Vt:  [[0.1014, -0.2022], [0.3966, 0.2057]]
Ih:  [[0.3407, 0.0], [0.4586, 0.0]]
Oh:  [[0.5844, 0], [0.6127, 0]]
Wt:  [[0.1296, -0.5649], [0.0, 0.0]]
Io:  [[-1.0889, 0.0], [0.0, 0.0]]
Oo:  0.2518
Error:  0.0174
d:  -0.0248
y:  [[-0.0145, -0.0], [-0.0152, -0.0]]
dW:  [[-0.0087, -0.0], [-0.0091, -0.0]]
{e}:  [[-0.0032, -0.0], [0.014, -0.0]]
d*:  [[0.0, 0.0], [-0.0002, 0.0]]
X:  [[0.0006, -0.0016], [-0.001, 0.0026]]
dV:  [[0.0004, -0.001], [-0.0006, 0.0016]]
V:  [[0.1018, 0.3956], [-0.2028, 0.2073]]
W:  [[0.1209, 0.0], [-0.574, 0.0]]
-----------------------------------------------
>>>
'''

