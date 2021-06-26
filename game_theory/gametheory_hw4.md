# HW4

*181220076 周韧哲*  

### Problem1

容易得到单次博弈的NE为$\{L,NN\}$，$P_1,P_2$都可选择$\{H,YY\},\{H,NY\}$来获得更高收益。则：

+ 对于$P_1$，在$t$时刻时，若历史策略$h_t=(a_1,\cdots,a_t)$中都为$\{H,YY\}$或$\{H,NY\}$，则选择$H$，否则选择$L$。
+ 对于$P_2$，在$t$时刻时，若历史策略$h_t=(a_1,\cdots,a_t)$中都为$\{H,YY\}$或$\{H,NY\}$，则选择$YY$或$NY$，否则选择$YN$或$NN$。

$P_1$不能再得到更高的收益，所以$\delta_1\geq 0$。$P_2$选择$\{H,NN\}$可得更高收益，当选择合作时有$5+5\delta_2+\cdots=\frac{5}{1-\delta_2}$，否则有$6+\delta_2+\delta_2^2+\cdots=6+\frac{\delta_2}{1-\delta_2}$，令$\frac{5}{1-\delta_2}\geq 6+\frac{\delta_2}{1-\delta_2}$，解得$\delta_2\geq\frac{1}{5}$，从而$\delta\geq\max(\delta_1,\delta_2)=\frac{1}{5}$。所以$\delta\geq\frac{1}{5}$时上述策略为SPNE。

### Problem2

容易得到单次博弈NE为$\{c,c\}$且收益都为$0$。当$q_1<q_2$时，对于$P_1$，$u_1$在$q_1=\frac{a+c}{2}$处得到最大值$\frac{(a-c)^2}{4}$，对于$P_2$同理。当$q_1=q_2$时，对于$P_1$，$u_1$在$q_1=\frac{a+c}{2}$处得到最大值$\frac{(a-c)^2}{8}$，对于$P_2$同理。所以：

+ 对于$P_1$，在$t$时刻时，若历史策略$h_t=((\frac{a+c}{2},\frac{a+c}{2}),\cdots,(\frac{a+c}{2},\frac{a+c}{2}))$，则选择$\frac{a+c}{2}$，否则选择$c$。
+ 对于$P_2$，在$t$时刻时，若历史策略$h_t=((\frac{a+c}{2},\frac{a+c}{2}),\cdots,(\frac{a+c}{2},\frac{a+c}{2}))$，则选择$\frac{a+c}{2}$，否则选择$c$。

令$\frac{(a-c)^2}{8}(1+\delta++\delta^2+\cdots)\geq\frac{(a-c)^2}{4}$，得到$\delta\geq\frac{1}{2}$。所以$\delta\geq\frac{1}{2}$时上述策略为SPNE。