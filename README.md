![image](https://github.com/ChunZhuo/Fourier/assets/118121876/ebb3d7ea-bedd-4e9d-b410-9b025989c11d)
____________________
**Fourier series** 

$$f(x) = A_0 + \sum_{k = 1}^{\infty}A_k\cdot\cos(\frac{k\pi x}{L}) + \sum_{k = 1}^{\infty} B_k \cdot\sin(\frac{k\pi x}{L})$$

$$A_0 = \frac{1}{2L}\cdot\int_{-L}^{L} f(x)\mathrm{d}x$$

$$A_n = \frac{1}{L}\cdot\int_{-L}^{L} f(x)\cos(\frac{k\pi x}{L})\mathrm{d}x$$

$$B_n = \frac{1}{L}\cdot\int_{-L}^{L} f(x)\sin(\frac{k\pi x}{L})\mathrm{d}x$$

NB. Fourier series are periodic  
___________________
**Euler's formula**

$$\mathrm{e}^{ix} = \cos(x) + isin(x)$$

**include complex number**

$$f(x) = \sum_{k = {-\infty}}^{\infty}C_k \mathrm{e}^{\frac{ik{\pi}x}{L}}$$

$$C_{k} = \frac{1}{2L}\int_{-L}^{L}f(x)\mathrm{e}^{-\frac{ik{\pi}x}{L}}\mathrm{d}x$$

**Gibbs Phenomena**:
For the discrete point of the function, the fourier approximation is oscillating
Since we truncate the formula by define the K.
If K goes infinite, then the oscillation goes away

![image](https://github.com/ChunZhuo/Fourier/assets/118121876/8481f818-aa73-4d2c-8a33-89e384fbcdba)

If K >= n/2, them the phenomena is derived.
Because the plot we made is actually a bunch of points.
So keep K the same, if we double n, then the Gibbs Phen. comes back.

![image](https://github.com/ChunZhuo/Fourier/assets/118121876/30015f1c-fc9f-4d1c-b5c1-0dcd075b2533)
_____________________
**Fourier transform**
 Approximate a function without periodicity
 
$$\omega_{k} = \frac{k\pi}{L} = k\Delta\omega$$

$$\lim_{\Delta\omega\to\infty}\sum_{k = {-\infty}}^{\infty}\frac{\Delta\omega}{2\pi}\int_{-\infty}^{\infty} f(\xi)\mathrm{e}^{-ik\Delta\omega\xi}\mathrm{d}\xi\mathrm{e}^{ik\Delta\omega {x}}$$

**Which is:**

$$\int_{-\infty}^{\infty}\frac{1}{2\pi}\int_{-\infty}^{\infty} f(\xi)\mathrm{e}^{-i\omega\xi}\mathrm{d}\xi\mathrm{e}^{i\omega{x}}\mathrm{d}\omega$$

___________________

$$\hat{f}(w) = \mathcal{F}(f(x)) = \int_{-\infty}^\infty f(x)\mathrm{e}^{-iwx}\mathrm{d}x$$

$$f(x) = \mathcal{F}^{-1}(\hat{f}(w)) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{f}(w)\mathrm{e}^{iwx}\mathrm{d}w$$

___________________

**Fourier transform and derivatives**

$$\mathcal{F}\left({\frac{\mathrm d}{\mathrm d x}}f(x)\right) = \int_{-\infty}^{\infty}\frac{\mathrm{d}f}{\mathrm{d}x}\mathrm{e}^{-iwx}\mathrm{d}x $$

$$=\lbrack f(x) \mathrm{e}^{-iwx}\rbrack_{-\infty}^{\infty} - \int_{-\infty}^{\infty} f(x) \left({-i\omega\mathrm{e}^{-iwx}}\right)\mathrm{d}x$$

**require: （which is a restriction for fourier transform)**  

$$f(x) = 0 ||( x \to\infty | x \to -\infty)$$

**Then:**

$$={i\omega}\int_{-\infty}^{\infty} f(x) \left({-i\omega\mathrm{e}^{-iwx}}\right)\mathrm{d}x$$

$$\mathcal{F}\left({\frac{\mathrm d}{\mathrm d x}}f(x)\right)=i\omega\mathcal{F}\left({\frac{\mathrm d f}{\mathrm d x}}\right)$$

_________________

**FT and convolution**\

What is convolution?

$$f\cdot g = \int_{-\infty}^{\infty}f(x-\xi)g(\xi)\mathrm{d}\xi$$

So

$$\mathcal{F}(f*g) = \mathcal{F}(f)\mathcal{F}(g) = \hat{f}\hat{g}$$

$$\mathcal{F}^{-1}({\hat{f}\hat{g}})(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{f}(w)\hat{g}(w)\mathrm{e}^{iwx}\mathrm d w$$

$$=\frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{f}(w)(\int_{-\infty}^{\infty}g(y)\mathrm{e}^{-iwy}\mathrm d y)\mathrm{e}^{iwx}\mathrm d w$$

$$=\frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{f}(w)\int_{-\infty}^{\infty}g(y)\mathrm{e}^{iw(x-y)} \mathrm d y \mathrm d w$$

$$= \int_{-\infty}^{\infty}f(x-y)g(y)\mathrm d y$$

___________

$$\mathcal{F}(\alpha f(x) \beta g(x)) = \alpha \mathcal{F}(f) + \beta \mathcal{F}(g)$$

__________
**Parseval's Theorem**

$$\int_{-\infty}^{\infty} |\hat{f}(w)|^2\mathrm{d}w =2\pi \int_{-\infty}^{\infty}|f(x)|^2\mathrm{d}x$$

___________
**FT for PDE (an example)**

heat_equation

$$U_{t} = \alpha ^ {2} U_{xx}$$ 

FT：

ODE

$$\frac{\mathrm{d}\hat{U}}{\mathrm{d} t} = -w^{2}\alpha^{2}\hat{U}$$

Then: 
$$\hat{U}(w,t) = \mathrm{e}^{-w^2\alpha^2t}\hat{U}(w,0)$$

$$U(x,t) = \mathcal{F}^{-1}(\mathrm{e}^{-w^2\alpha^2t})*U(x,0)$$

Gaussian

$$\mathcal{F}^{-1}(\mathrm{e}^{-w^2\alpha^2t})$$
__________
**Discrete Fourier Transform**
$$\hat{f_k} = \sum_{j = 0}^{n-1} f_{j}\mathrm{e}^{wjk}\\
f_{k} = (\sum_{j = 0}^{n-1} \hat{f_{j}}\mathrm{e}^{-wjk})\frac{1}{n}$$

$$\mathcal{w}=\mathrm{e}^{\frac{-2\pi i}{n}}$$


$$\begin{bmatrix} \hat{f_{0}} 
\\
\hat{f_{1}}
\\
\vdots
\\
\hat{f_{n}}\end{bmatrix} = \begin{bmatrix}1 & 1 & 1 & \cdots & 1
\\
1 & w_{n} & w_{n}^{2} & \cdots & w_{n}^{n-1}
\\
1 & w_{n}^{2} & w_{n}^{4} & \cdots & w_{n}^{2(n-1)}
\\
\vdots & \vdots & \vdots & \ddots & \vdots 
\\
1 & w_{n}^{n-1} & w_{n}^{2(n-1)} & \cdots& w_{n}^{(n-1)^2} \end{bmatrix} 
\begin{bmatrix} f_{0}
\\
\hat{f_{1}}
\\
\vdots
\\
\hat{f_{n}}
\end{bmatrix}$$
___________
**Fast Fourier Transform**

$$\mathcal{O}(nlog{n})$$
___________
**Laplace transform**
$$\mathrm{F}(t) = f(t)\mathrm{e}^{-\gamma t}\mathrm{H}(t)$$
![image](https://github.com/ChunZhuo/Fourier/assets/118121876/c3b4b187-272a-4b83-afca-234cfb30ecc1)

Some functions are badly represented using fourier transform, e.g. $y = e^{\lambda t}$
![image](https://github.com/ChunZhuo/Fourier/assets/118121876/82d5963c-2e26-4aa1-9a3a-4b0ed705e199)

![image](https://github.com/ChunZhuo/Fourier/assets/118121876/1220cece-67b2-4414-87c9-8b8f0aaffaa9)




