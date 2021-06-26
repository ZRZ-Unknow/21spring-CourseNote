# HW4

*181220076 周韧哲*

### Problem1

1. $\rho=1.5$时，可计算得到$k=\frac{n^2}{\rho(2n+1)}\approx 85$。

2. matlab代码如下：

   ```matlab
   image = double(imread('./lena.bmp'));
   [U,S,V] = svd(image);
   k = 85;
   n = 256;
   image_ = U(:, 1:k)*S(1:k,1:k)*V(:, 1:k).';
   subplot(1, 2, 1); imshow(uint8(image)); title('原图');
   subplot(1, 2, 2); imshow(uint8(image_)); title('压缩后');
   mse = norm(image-image_,'fro')^2/(n*n)
   psnr = 20*log10((2^8-1)/sqrt(mse))
   ```

   计算得到$\text{mse} = 10.9722$，$\text{psnr} = 37.7279$。图像如下图所示：

   <img src="pics\hw4p1.jpg"/>

### Problem2

matlab代码如下：

```matlab
lena = double(imread('./lena.bmp'));
cameraman = double(imread('./cameraman.tif'));
alpha = [0.1, 0.5];
subplot(2, 3, 1); imshow(uint8(lena)); title('原始图像');
subplot(2, 3, 4); imshow(uint8(cameraman)); title('水印图像');
for i=1:length(alpha)
    [U,S,V] = svd(lena);
    L = S + alpha(i)*cameraman;
    [U1,S1,V1] = svd(L);
    P = U*S1*V.';
    [Up,Sp,Vp] = svd(P);
    F = U1*Sp*V1.';
    W = (F - S)/alpha(i);
    subplot(2, 3, i+1); imshow(uint8(P));
    title(['加入水印后图像，alpha=',mat2str(alpha(i))]);
    subplot(2, 3, i+4); imshow(uint8(W));
    title(['检测水印图像，alpha=',mat2str(alpha(i))]);
end
```

图像如下图所示：

<img src="pics\hw4p2.jpg" />

### Problem3

使用matlab进行计算：

```matlab
H = [1+i,3+i,7;5-0.1i,4+i,8-i;2+3i,6-i,1+3i];
x = [1,2,3].';
[U,S,V] = svd(H);
prefiltering = V
postfiltering = U'
equal_gain = diag(S).'
```

可以得到pre-filtering矩阵，post-filtering矩阵，等效增益如下：

```matlab
prefiltering =
  -0.4206 + 0.0000i   0.2913 + 0.0000i  -0.8592 + 0.0000i
  -0.4477 - 0.1281i  -0.1901 + 0.7843i   0.1547 + 0.3286i
  -0.7614 - 0.1629i  -0.0723 - 0.5086i   0.3482 - 0.0927i
postfiltering =
  -0.5074 + 0.1743i  -0.7299 + 0.1063i  -0.2862 + 0.2935i
  -0.2672 + 0.1884i  -0.2001 + 0.1837i   0.2860 - 0.8588i
   0.7607 + 0.1632i  -0.5827 - 0.2064i   0.0732 - 0.0849i
equal_gain =
   13.7272    5.8734    2.2530
```

等效传输模型图如下图所示：

<img src="pics\hw4p3.PNG" style="zoom: 33%;" />

