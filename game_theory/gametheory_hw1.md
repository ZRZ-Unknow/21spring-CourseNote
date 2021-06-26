# HW1

181220076 周韧哲

### Problem 1 

 容易得到$b_1(l)=e,b_2(e)=l$，故pure strategy NE只有$(e, l)$。

### Problem 2

令齐威王的策略为$\{a_i|i=1,\cdots,6\}$，对应的概率为$\{x_i|i=1,\cdots,6\}$，田忌的策略为$\{b_i|i=1,\cdots,6\}$，对应的概率为$\{y_i|i=1,\cdots,6\}$。容易得到齐威王的各策略expectation payoff：
$$
\begin{align*}
U_1(a_1,p_2)&=3y_1+y_2+y_3+y_4-y_5+y_6\\
U_1(a_2,p_2)&=y_1+3y_2+y_3+y_4+y_5-y_6\\
U_1(a_3,p_2)&=y_1-y_2+3y_3+y_4+y_5+y_6\\
U_1(a_4,p_2)&=-y_1+y_2+y_3+3y_4+y_5+y_6\\
U_1(a_5,p_2)&=y_1+y_2+y_3-y_4+3y_5+y_6\\
U_1(a_6,p_2)&=y_1+y_2-y_3+y_4+y_5+3y_6\\
\end{align*}
$$
由NE推导出上面六式相等，由于$\sum_{i=1}^6y_i=1$，得到各$y_i$都等于$\frac{1}{6}$。类似的，可以得到各$x_i$都等于$\frac{1}{6}$。从而MNE的$p_1=(\frac{1}{6},\frac{1}{6},\frac{1}{6},\frac{1}{6},\frac{1}{6},\frac{1}{6})$，$p_2=(\frac{1}{6},\frac{1}{6},\frac{1}{6},\frac{1}{6},\frac{1}{6},\frac{1}{6})$，齐威王的expected payoff为$6\times(\frac{1}{6}\times\frac{1}{6}\times(3+1+1+1+1-1))=1$，田忌的expected payoff为$6\times(\frac{1}{6}\times\frac{1}{6}\times(-3-1-1-1-1+1))=-1$。

### Problem 3

令$A,B,C$三者的策略概率分别为$(\pi_1,1-\pi_1),(\pi_2,1-\pi_2),(\pi_3,1-\pi_3)$，得到
$$
\begin{align*}
U_1(a,p_{-1})&=-4(1-\pi_2)\pi_3+3\pi_2(1-\pi_3)+(1-\pi_2)(1-\pi_3)\\
U_1(b,p_{-1})&=\pi_2\pi_3+2(1-\pi_2)\pi_3-4\pi_2(1-\pi_3)\\
U_2(x,p_{-2})&=-4(1-\pi_1)\pi_3+3\pi_1(1-\pi_3)+4(1-\pi_1)(1-\pi_3)\\
U_2(y,p_{-2})&=\pi_1\pi_3+2(1-\pi_1)\pi_3-4\pi_1(1-\pi_3)\\
U_3(L,p_{-3})&=2\pi_1(1-\pi_2)+2(1-\pi_1)\pi_2-2(1-\pi_1)(1-\pi_2)\\
U_3(R,p_{-3})&=-2\pi_1\pi_2+2\pi_1(1-\pi_2)+2(1-\pi_1)\pi_2\\
\end{align*}
$$
由$U_1(a,p_{-1})=U_1(b,p_{-1}),U_2(x,p_{-2})=U_2(y,p_{-2}),U_3(L,p_{-3})=U_3(R,p_{-3})$得到
$$
\begin{align*}
1+6\pi_2-7\pi_3-\pi_2\pi_3&=0\\
1+6\pi_1-7\pi_3-\pi_1\pi_3&=0\\
\pi_1+\pi_2&=1\\
\end{align*}
$$
解出$\pi_1=\pi_2=\frac{1}{2},\pi_3=\frac{8}{15}$。从而MNE：$p_1=(\frac{1}{2},\frac{1}{2}),p_2=(\frac{1}{2},\frac{1}{2}),p_3=(\frac{8}{15},\frac{7}{15})$。

### Problem 4

由$U_1(a_1,p_{2})=U_1(a_2,p_{2}),U_2(b_1,p_{1})=U_2(b_2,p_{1})$以及下式
$$
\begin{align*}
U_1(a_1,p_{2})&=a\pi_2+e(1-\pi_2)\\
U_1(a_2,p_{2})&=b\pi_2+f(1-\pi_2)\\
U_2(b_1,p_{1})&=c\pi_1+d(1-\pi_1)\\
U_2(b_2,p_{1})&=g\pi_1+h(1-\pi_1)\\
\end{align*}
$$
可解出$\pi_1=\frac{h-d}{c-d-g+h},\pi_2=\frac{f-e}{a-e-b+f}$，对应便可得到MNE为
$$
p_1=(\frac{h-d}{c-d-g+h},\frac{c-g}{c-d-g+h}),\quad p_2=(\frac{f-e}{a-e-b+f},\frac{a-b}{a-e-b+f})
$$

### Problem 5

设$p_1=(q_1,q_2,q_3,q_4),p_2=(h_1,h_2,h_3,h_4)$，经过观察可以发现对于Player2 y占优于z，故可令$h_3=0$，从而对于Player1来说$q_1=q_4=0$，从而$h_1=0$。则
$$
\begin{align*}
U_1(b,p_2)&=5h_2+3h_4\\
U_1(c,p_2)&=6h_2+2h_4\\
U_2(y,p_1)&=5q_2+2q_3\\
U_2(z,p_1)&=2q_2+3q_3\\
\end{align*}
$$
由$U_1(\cdot,p_2),U_2(\cdot,p_1)$分别相等以及$\sum_{i=1}^4q_i=1,\sum_{i=1}^4h_i=1$可解出$h_2=h_4=\frac{1}{2},q_2=\frac{1}{4},q_3=\frac{3}{4}$。从而$p_1=(0,\frac{1}{4},\frac{3}{4},0),p_2=(0,\frac{1}{2},0,\frac{1}{2})$。

### Problem 6

使用Kakutani Fixed Point Theorem定理证明。首先，定义
$$
\begin{align*}
B(p)&=(B_1(p_{-1}),B_2(p_{-2}),\cdots,B_N(p_{-N}))\\
B(p)&:\Delta(A_1)\times\cdots\times\Delta(A_N)\rightarrow\Delta(A_1)\times\cdots\times\Delta(A_N)
\end{align*}
$$

+ 证明$\Delta(A_1)\times\cdots\times\Delta(A_N)$为凸紧集：

  令$n=|A_i|$，则$\Delta(A_i)=\{(x_1,\cdots,x_n):x_i\in[0,1],\sum_{i=1}^n x_i=1\}$为n-1维的单纯形，所以$\Delta(A_i)$为凸紧集，从而$\Delta(A_1)\times\cdots\times\Delta(A_N)$为非空的凸紧集。

+ 证明$B(p)$非空：令$f(x)=U_i(x,p_{-i})=\sum_k x_k U_i(p_{-i},a_k)$，$f(x)$连续且$\Delta(A_i)$为紧集，由Weierstrass定理，$f(x)$在$\Delta(A_i)$中有最大值，从而$B_i(p_{-i})=\arg\max_{p_i'}U_i(p_i',p_{-i})=\arg\max_{x}f(x)$为非空，从而$B(p)$也非空。

+ 证明$B(p)$为凸集：
  对于任意$\lambda\in[0,1]$与$p_i',p_i''\in B_i(p_{-i})$，有$U_i(p_i',p_{-i})\geq U_i(p_i^*,p_{-i}),U_i(p_i'',p_{-i})\geq U_i(p_i^*,p_{-i}),\text{ for }p_i^*\in\Delta(A_i)$，
  $$
  \begin{align*}
  &\quad U_i(\lambda p_i'+(1-\lambda)p_i'',p_{-i})\\&=\lambda U_i(p_i',p_{-i})+(1-\lambda)U_i(p_i'',p_{-i})\\
  &\geq\lambda U_i(p_i^*,p_{-i})+(1-\lambda) U_i(p_i^*,p_{-i})\\&=U_i(p_i^*,p_{-i})
  \end{align*}
  $$
  从而$\lambda p_i'+(1-\lambda)p_i''\in B_i(p_{-i})$，故$B_i(p_{-i})$为凸集，从而$B(p)$也为凸集。

+ 证明$B(p)$有一个closed graph：

  假设$(p^n,\hat{p}^n)\rightarrow(p,\hat{p}),\hat{p}^n\in B(p^n),\text{but }\hat{p}\notin B(p)$。则至少存在一个$\hat{p}^i\notin B_i(p_{-i})$，也即存在$\overline{p}_i$与$\epsilon>0$使得$U_i(\overline{p}_i,p_{-i})\geq U_i(\hat{p}_i,p_{-i})+3\epsilon$。对于连续的$U_i,p_{-i}^n\rightarrow p_{-i}$与$(\hat{p}_i^n,p_{-i}^n)\rightarrow(\hat{p}_i,p_{-i})$，有
  $$
  \begin{align*}
  U_i(\overline{p}_i,p_{-i}^n)&> U_i(\overline{p}_i,p_{-i})-\epsilon\\
  U_i(\hat{p}_i,p_{-i})&> U_i(\hat{p}_i^n,p_{-i}^n)-\epsilon
  \end{align*}
  $$
  有$U_i(\overline{p}_i,p_{-i}^n)> U_i(\hat{p}_i^n,p_{-i}^n)+\epsilon$，从而$\hat{p}^n\notin B_i(p_{-i}^n)$，与假设矛盾。从而$(p^n,\hat{p}^n)\rightarrow(p,\hat{p}),\hat{p}^n\in  B(p^n),\text{then }\hat{p}\in B(p)$，得证。

综上，由Kakutani Fixed Point Theorem定理可知存在$p\in \Delta(A_1)\times\cdots\times\Delta(A_N)$使得$p\in B(p)$，从而$p$便是Nash Equilibrium。

### Problem 7

+ 必要性：设$p$为MNE，$a$为$p_i$中具有正概率的纯策略。假设$a$不是对$p_{-i}$的最优反应，即存在$a'$，使得$U_i(a',p_{-i})>U_i(a,p_{-i})$。则对player i可构造新的混合策略$p_i'$，$p_i'$将原$p_i$中$a$概率与$a'$交换，容易得到$U_i(p_i',p_{-i})>U_i(p_i,p_{-i})$，与条件矛盾。从而所有概率为正的纯策略都是$p_{-i}$的最优反应。

+ 充分性：设$a_1^*,\cdots,a_m^*$为$p_i$中具有正概率的纯策略，则对任意$a\in A_i$，$U_i(a_j^*, p_{-i})\geq U_i(a, p_{-i})$，$j=1,\cdots, m$，所以$U_i(a_1^*,p_{-i})=\cdots=U_i(a_m^*,p_{-i})$，则
  $$
  U_i(p_{i},p_{-i})=\sum_{j=1}^m x_j U_i(a_j^*,p_{-i})=U_i(a_1^*,p_{-i})\sum_{j=1}^m x_j=U_i(a_1^*,p_{-i})
  $$
  

  那么对于任意$p_{i}'=(y_1,\cdots,y_n)\in\Delta(A_i),\sum_{j=1}^n y_j=1$，有
  $$
  \begin{align*}
  U_i(p_i,p_{-i})&=U_i(a_1^*,p_{-i})\\
  &=U_i(a_1^*,p_{-i})\sum_{j=1}^n y_j\\
  &=\sum_{j=1}^n y_jU_i(a_1^*,p_{-i})\\
  &\geq\sum_{j=1}^n y_jU_i(a_j,p_{-i})\\
  &=U_i(p_i',p_{-i})
  \end{align*}
  $$
  

  从而对于任意$i$与任意$p_i'$，$U_i(p_i,p_{-i})\geq U_i(p_i',p_{-i})$，可知$p$为MNE。

