import numpy as np
import matplotlib.pyplot as plt
import time



def tdma(A, F):
    beta, y, x = [], [], []
    for i in range(F.shape[0]-1):
        if i==0:
            beta.append(A[i][i+1]/A[i][i])
        else:
            beta.append(A[i][i+1]/(A[i][i]-A[i][i-1]*beta[-1]))
    for i in range(F.shape[0]):
        if i==0:
            y.append(F[i]/A[i][i])
        else:
            y.append((F[i]-A[i][i-1]*y[-1])/(A[i][i]-A[i][i-1]*beta[i-1]))
    for i in range(F.shape[0]-1, -1, -1):
        if i==F.shape[0]-1:
            x.append(y[i])
        else:
            x.append(y[i]-beta[i]*x[-1])
    return np.array(x[::-1])

def calc(x, fx, M, target):
    global h
    res = []
    for t in target:
        for i in range(x.shape[0]-1, -1, -1):
            if t==x[i]:
                res.append(fx[i])
                break
            if t > x[i]:
                assert i!=x.shape[0]-1
                S = M[i]*(x[i+1]-t)**3/(6*h) + M[i+1]*(t-x[i])**3/(6*h) +\
                    (fx[i]-M[i]*h**2/6)*(x[i+1]-t)/h + (fx[i+1]-M[i+1]*h**2/6)*(t-x[i])/h
                res.append(S)
                break
    return np.array(res)

x = np.arange(0.2, 2.2, 0.2) 
fx = np.array([1.11398,1.24177,1.42303,1.51860,1.36437,1.13202,1.07845,0.98431,0.63207,0.34783])
h = 0.2
mu = 0.5
lam = mu

def q1():
    start_time = time.time()
    diff2 = []
    d = []
    m0, mn = 0.0, 0.0
    for i in range(x.shape[0]-1):
        diff2.append((fx[i+1]-fx[i])/h)
    for i in range(x.shape[0]-2):
        d.append(6*(diff2[i]-diff2[i+1])/(x[i]-x[i+2]))

    A = np.zeros((x.shape[0]-2,x.shape[0]-2))
    for i in range(A.shape[0]):
        A[i][i] = 2
        if i==0:
            A[i][i+1] = lam
        elif i==A.shape[0]-1:
            A[i][i-1] = mu
        else:
            A[i][i-1] = mu
            A[i][i+1] = lam
    d = np.array(d)
    d[0] = d[0] - mu*m0
    d[1] = d[1] - lam*mn
    M = tdma(A, d)
    M = np.insert(M, [0], 0)
    M = np.append(M, [0], 0)
    Sx = calc(x, fx, M, np.array([0.2*i+0.1 for i in range(1,10)]))
    end_time = time.time()
    print("="*35, "q1", "="*35)
    print("M:\n", M)
    print("S(x):\n", Sx)
    plot_x = np.array([0.2+0.001*i for i in range(1,1800)])
    plot_y = calc(x, fx, M, plot_x)
    plt.plot(plot_x, plot_y, label='q1')
    return end_time-start_time

def q2():
    start_time = time.time()
    diff2 = []
    d = []
    d_fx0, d_fxn = 0.20271, 1.55741
    for i in range(x.shape[0]-1):
        diff2.append((fx[i+1]-fx[i])/h)
    d.append(6/h*(diff2[0]-d_fx0))
    for i in range(x.shape[0]-2):
        d.append(6*(diff2[i]-diff2[i+1])/(x[i]-x[i+2]))
    d.append(6/h*(d_fxn-diff2[-1]))

    A = np.zeros((x.shape[0],x.shape[0]))
    for i in range(A.shape[0]):
        A[i][i] = 2
        if i==0:
            A[i][i+1] = 1
        elif i==A.shape[0]-1:
            A[i][i-1] = 1
        else:
            A[i][i-1] = mu
            A[i][i+1] = lam
    d = np.array(d)
    M = tdma(A, d)
    Sx = calc(x, fx, M, np.array([0.2*i+0.1 for i in range(1,10)]))
    end_time = time.time()
    print("="*35, "q2", "="*35)
    print("M:\n", M)
    print("S(x):\n", Sx)
    plot_x = np.array([0.2+0.001*i for i in range(1,1800)])
    plot_y = calc(x, fx, M, plot_x)
    plt.plot(plot_x, plot_y, label='q2')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('S(x)')
    plt.title("Problem 1")
    return end_time-start_time


t1 = q1()
t2 = q2()
print(f"Question1 CPU Time Cost: {t1} s")
print(f"Question2 CPU Time Cost: {t2} s")
plt.show()