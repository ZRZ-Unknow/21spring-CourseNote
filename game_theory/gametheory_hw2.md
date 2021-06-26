# HW2

*181220076 周韧哲*  

### Problem1

令$p_1=(x_1,x_2,x_3),p_2=(y_1,y_2,y_3)$，则需要求解的MNE为$\max_{p_1}\min_{p_2}p_1Mp_2^T,\min_{p_2}\max_{p_1}p_1Mp_2^T$，线性规划式子如下：
$$
\begin{aligned}
 \max&\quad v\\
 s.t.&\quad -2x_2+x_3\geq v\\
 &\quad 2x_1-3x_3\geq v\\
 &\quad -x_1+3x_2\geq v\\
 &\quad x_1,x_2,x_3\geq 0\\
 &\quad x_1+x_2+x_3=1 \\
 \end{aligned}\\
 \begin{aligned}
 \min&\quad v\\
 s.t.&\quad 2y_2-y_3\leq v\\
 &\quad -2y_1+3y_3\leq v\\
 &\quad y_1-3y_2\leq v\\
 &\quad y_1,y_2\geq 0\\
 &\quad y_1+y_2+y_3=1 \\
 \end{aligned}\\
$$

### Problem2

令$p_1=(x_1,x_2,x_3,x_4),p_2=(y_1,y_2,y_3,y_4)$，则需要求解的MNE为$\max_{p_1}\min_{p_2}p_1Mp_2^T,\min_{p_2}\max_{p_1}p_1Mp_2^T$，线性规划式子如下：
$$
\begin{aligned}
 \max&\quad v\\
 s.t.&\quad x_1+3x_2-2x_3-5x_4\geq v\\
 &\quad -x_1-2x_2-4x_3+2x_4\geq v\\
 &\quad 2x_1+4x_2-5x_3+6x_4\geq v\\
 &\quad -2x_1-2x_2+7x_3+3x_4\geq v\\
 &\quad x_1,x_2,x_3,x_4\geq 0\\
 &\quad x_1+x_2+x_3+x_4=1 \\
 \end{aligned}\\
 \begin{aligned}
 \min&\quad v\\
 s.t.&\quad y_1-y_2+2y_3-2y_4\leq v\\
 &\quad 3y_1-2y_2+4y_3-2y_4\leq v\\
 &\quad -2y_1-4y_2-5y_3+7y_4\leq v\\
 &\quad -5y_1+2y_2+6y_3+3y_4\leq v\\
 &\quad y_1,y_2,y_3,y_4\geq 0\\
 &\quad y_1+y_2+y_3+y_4=1 \\
 \end{aligned}\\
$$

### Problem3

令$p_1=(x_1,x_2,x_3,x_4),p_2=(y_1,y_2,y_3,y_4)$，则需要求解的MNE为$\max_{p_1}\min_{p_2}p_1Mp_2^T,\min_{p_2}\max_{p_1}p_1Mp_2^T$，线性规划式子如下：
$$
\begin{aligned}
 \max&\quad v\\
 s.t.&\quad x_1+2x_2-3x_3+8x_4\geq v\\
 &\quad -2x_1-7x_2+4x_3+3x_4\geq v\\
 &\quad 6x_1+2x_2-4x_3-2x_4\geq v\\
 &\quad -4x_1+4x_2-3x_3+3x_4\geq v\\
 &\quad x_1,x_2,x_3,x_4\geq 0\\
 &\quad x_1+x_2+x_3+x_4=1 \\
 \end{aligned}\\
 \begin{aligned}
 \min&\quad v\\
 s.t.&\quad y_1-2y_2+6y_3-4y_4\leq v\\
 &\quad 2y_1-7y_2+2y_3+4y_4\leq v\\
 &\quad -3y_1+4y_2-4y_3-3y_4\leq v\\
 &\quad -8y_1+3y_2-2y_3+3y_4\leq v\\
 &\quad y_1,y_2,y_3,y_4\geq 0\\
 &\quad y_1+y_2+y_3+y_4=1 \\
 \end{aligned}\\
$$

### Problem4

若$(p^*,q^*)$为MNE，则
$$
U_1(p^*,q^*)\geq U_1(p,q^*)\text{ for all }p\in\Delta_1 \\
U_2(p^*,q^*)\geq U_2(p^*,q)\text{ for all }q\in\Delta_2 
$$
因为$U_1=-U_2$，所以$(p^*,q^*)$为NE当且仅当 $U(p,q^*)\leq U(p^*,q^*)\leq U(p^*,q)$当且仅当$U(p,q^*)\leq U(p^*,q)$。所以只需要证明$U(p,q^*)\leq U(p^*,q)$当且仅当$\max_p\min_q U(p,q)=\min_q\max_p U(p,q)$。

+ 充分性：易知$U(p,q^*)\leq \max_{p}U(p,q^*)=\min_q\max_p U(p,q)$，且$U(p^*,q)\geq\min_q U(p^*,q)=\max_p\min_q U(p,q)$，又因为$\max_p\min_q U(p,q)=\min_q\max_p U(p,q)$，所以$U(p,q^*)\leq U(p^*,q)$。
+ 必要性：由于$U(p,q^*)\leq U(p^*,q)$，可以推出$\max_pU(p,q^*)\leq\min_q U(p^*,q)$，再由$p^*,q^*$的定义可得$\min_q\max_p U(p,q)\leq\max_p\min_q U(p,q)$，又因为$\min_q\max_p U(p,q)\geq\max_{p}\min_q U(p,q)$一定成立，所以$\max_p\min_q U(p,q)=\min_q\max_p U(p,q)$。

### Problem5

令$f(p,q)=pMq^T$，则$f(\theta x+(1-\theta)y,q)=(\theta x+(1-\theta)y)Mq^T=\theta xMq^T+(1-\theta)yMq^T=\theta f(x,q)+(1-\theta)f(y,q)\leq \theta f(x,q)+(1-\theta)f(y,q)$，所以对于所有固定的q，$f(p,q)$对p是凹的，同理对于所有固定的p，$f(p,q)$对q是凸的，所以$\max_p\min_q f(p,q)=\min_q\max_p f(p,q)$，即$max_p\min_q pMq^T=\min_q\max_p pMq^T$。

### Problem6

PNE是$b_1\in[v_1,v_2],b_2=b_1$。显然可以看出当处于这种策略时，两Player都不能单方面改变$b_1,b_2$以获得更大payoff，所以这是一个PNE。假设有其他的PNE，若某个PNE中Player2中标，则$b_2>b_1$，此时：如果$b_2>v_2$，Player2会使得$b_2\leq b_1$；如果$b_2\leq v_2$，则有$b_1<b_2\leq v_2<v$，Player1会提高$b_1$来中标，故PNE中只有Player1中标。若PNE中$b_1<v2$，则Player2可以提高$b_2$至$(b_1,v_2)$使得其payoff提高，同理若PNE中$b_1>v_1$则Player1可降低$b_1$至小于$b_2$来提高Payoff。故只有那一个PNE。

### Problem7

PNE为$q_1=q_2=c$，显然当处于这一NE时两家公司都无法单方面改变策略来获得高的payoff，例如若$q_1<q_2=c$则$u_1<0$，反之$q_1>q_2=c,u_1=0$。接下来证明没有其他的PNE。若在某PNE中$q_1\neq q_2$，不妨讨论如下情况：$q_1>q_2$，则$u_1(q_1,q_2)=0,u_2(q_1,q_2)=(q_2-c)(a-q_2)$，若$q_1>c$则公司1可以减少$q_1$来使得其payoff提高，若$q_2<q_1\leq c$，则公司2可以降低$q_2$来获得更高payoff。所以$q_1=q_2$。再假设$q_1=q_2\neq c$，若$q_2>c$则公司2可以降低$q_2$至$(c,q_1)$以使得其payoff提高；若$q_1<c$则公司1将提高$q_1$至大于$q_2$来使得其payoff提高。所以只有那一个PNE。