![image](https://github.com/ChunZhuo/Fourier/assets/118121876/ebb3d7ea-bedd-4e9d-b410-9b025989c11d)

**Fourier series** 
$$f(x) = A_0 + \sum_{k = 1}^{\infty}A_k\cdot\cos(\frac{k\pi x}{L}) + \sum_{k = 1}^{\infty} B_k \cdot\sin(\frac{k\pi x}{L})$$
$$A_0 = \frac{1}{2L}\cdot\int_{-L}^{L} f(x)\mathrm{d}x$$
$$A_n = \frac{1}{L}\cdot\int_{-L}^{L} f(x)\cos(\frac{k\pi x}{L})\mathrm{d}x$$
$$B_n = \frac{1}{L}\cdot\int_{-L}^{L} f(x)\sin(\frac{k\pi x}{L})\mathrm{d}x$$
NB. Fourier series are periodic  
**Eler's formula**
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

**Fourier transform**
Approximate a function without periodicity
$$\omega_{k} = \frac{k\pi}{L} = k\Delta\omega$$
$$\lim_{\Delta\omega\to\infty}\sum_{k = {-\infty}}^{\infty}\int_{-\infty}^{\infty}  $$
$$\hat{f}(w) = \mathcal{F}(f(x)) = \int_{-\infty}^\infty f(x)\mathrm{e}^{-iwx}\mathrm{d}x$$
$$f(x) = \mathcal{F}^{-1}(\hat{f}(w)) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{f}(w)\mathrm{e}^{siwx}\mathrm{d}w$$
