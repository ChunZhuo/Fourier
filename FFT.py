import numpy as np
import matplotlib.pyplot as plt

### period
L = 2 *np.pi

### integral
dx = 0.0001
x = np.arange( -L, L,dx )
n = len(x)

### number of repetition
k_size = 1000

#### line to approximate ####
def hat_function(x, a, b, c):
    return np.piecewise(x, [x < a, (x >= a) & (x <= b), (x > b) & (x <= c), x > c],
                        [0, lambda x: (x - a) / (b - a), lambda x: (c - x) / (c - b), 0])
y = hat_function(x, -4,0, 4 )
#############################


##################
### Fourier series
k = np.expand_dims(np.arange(1,k_size + 1,1),1)
Cos = np.cos(k * np.pi * x / L) 
Sin = np.sin(k * np.pi * x / L) 
A0 = np.sum(y * dx)/(2 * L)
A = np.sum(y * Cos * dx, axis = 1) * (1/L) 
B = np.sum(y * Sin * dx, axis = 1) * (1/L)

F = A0 + np.matmul(A,Cos) + np.matmul(B,Cos)

### Plot
fig,ax = plt.subplots()
ax.plot(x,y,'-',color = 'k')
ax.plot(x,F, '-')
plt.savefig('FFT.png')

