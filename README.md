![image](https://github.com/ChunZhuo/Fourier/assets/118121876/ebb3d7ea-bedd-4e9d-b410-9b025989c11d)
____________________
**Fourier series** 
$$f(x) = A_0 + \sum_{k = 1}^{\infty}A_k\cdot\cos(\frac{k\pi x}{L}) + \sum_{k = 1}^{\infty} B_k \cdot\sin(\frac{k\pi x}{L})  \tag{1}$$
$$A_0 = \frac{1}{2L}\cdot\int_{-L}^{L} f(x)\mathrm{d}x$$
$$A_n = \frac{1}{L}\cdot\int_{-L}^{L} f(x)\cos(\frac{k\pi x}{L})\mathrm{d}x$$
$$B_n = \frac{1}{L}\cdot\int_{-L}^{L} f(x)\sin(\frac{k\pi x}{L})\mathrm{d}x$$
NB. Fourier series are periodic  
___________________
**Euler's formula**
$$\mathrm{e}^{ix} = \cos(x) + isin(x)$$
**include complex number**
$$f(x) = \sum_{k = {-\infty}}^{\infty}C_k \mathrm{e}^{\frac{ik{\pi}x}{L}}  \tag{2}$$
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
$$\int_{-\infty}^{\infty}\frac{1}{2\pi}\int_{-\infty}^{\infty} f(\xi)\mathrm{e}^{-i\omega\xi}\mathrm{d}\xi\mathrm{e}^{i\omega{x}}\mathrm{d}\omega  $$
___________________
$$\hat{f}(w) = \mathcal{F}(f(x)) = \int_{-\infty}^\infty f(x)\mathrm{e}^{-iwx}\mathrm{d}x \tag{3}$$

$$f(x) = \mathcal{F}^{-1}(\hat{f}(w)) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{f}(w)\mathrm{e}^{iwx}\mathrm{d}w   \tag{4}$$
___________________
**Fourier transform and derivatives**
$$\mathcal{F}\left({\frac{\mathrm d}{\mathrm d x}}f(x)\right) = \int_{-\infty}^{\infty}\frac{\mathrm{d}f}{\mathrm{d}x}\mathrm{e}^{-iwx}\mathrm{d}x $$
$$=\lbrack f(x) \mathrm{e}^{-iwx}\rbrack_{-\infty}^{\infty} - \int_{-\infty}^{\infty} f(x) \left({-i\omega\mathrm{e}^{-iwx}}\right)\mathrm{d}x$$
**require: $$f(x) = 0  ||( x \to\infty | x \to -\infty)$$**
**Then:**
$$={i\omega}\int_{-\infty}^{\infty} f(x) \left({-i\omega\mathrm{e}^{-iwx}}\right)\mathrm{d}x$$
$$\mathcal{F}\left({\frac{\mathrm d}{\mathrm d x}}f(x)\right)=i\omega\mathcal{F}\left({\frac{\mathrm d f}{\mathrm d x}}\right) \tag{5}$$
_________________
**FT and convolution**\
What is convolution?
$$f\cdot g = \int_{-\infty}^{\infty}f(x-\xi)g(\xi)\mathrm{d}\xi$$
So
$$\mathcal{F}(f*g) = \mathcal{F}(f)\mathcal{F}(g) = \hat{f}\hat{g} \tag{6}$$
$$\mathcal{F}^{-1}({\hat{f}\hat{g}})(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{f}(w)\hat{g}(w)\mathrm{e}^{iwx}\mathrm d w$$
$$=\frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{f}(w)(\int_{-\infty}^{\infty}g(y)\mathrm{e}^{-iwy}\mathrm d y) \mathrm{e}^{iwx}\mathrm d w$$
$$=\frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{f}(w)\int_{-\infty}^{\infty}g(y)\mathrm{e}^{iw(x-y)} \mathrm d y \mathrm d w$$
$$= \int_{-\infty}^{\infty}f(x-y)g(y)\mathrm d y$$
___________
$$\mathcal{F}(\alpha f(x) \beta g(x)) = \alpha \mathcal{F}(f) + \beta \mathcal{F}(g) \tag{7}$$
__________
**Parseval's Theorem**
$$\int_{-\infty}^{\infty} |\hat{f}(w)|^2\mathrm{d}w =2\pi \int_{-\infty}^{\infty}|f(x)|^2\mathrm{d}x \tag{8}$$
