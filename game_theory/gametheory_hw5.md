# HW5

*181220076 周韧哲*  

### Problem1

+ 子博弈1：

  |      |  F   |  B   |
  | :--: | :--: | :--: |
  |  F   | 3,1  | 0.0  |
  |  B   | 0,0  | 1.3  |

  得到NE：$(F,F),(B,B)$。

+ 子博弈2为：

  |      |  a   |  b   |
  | :--: | :--: | :--: |
  |  A   | 4,4  | 0.0  |
  |  B   | 0,0  | 1.1  |

  得到NE：$(A,a),(B,b)$。
  
  当子博弈1取$(F,F)$时，子博弈2取$(A,a)$时，$P_1$会选择$C$，得到SPNE为$(CFA,Fa)$。
  
  当子博弈1取$(F,F)$时，子博弈2取$(B,b)$时，$P_1$会选择$S$，得到SPNE为$(SFB,Fb)$。
  
  当子博弈1取$(B,B)$时，子博弈2取$(A,a)$时，$P_1$会选择$C$，得到SPNE为$(CBA,Ba)$。
  
  当子博弈1取$(B,B)$时，子博弈2取$(B,b)$时，$P_1$由于两种收益都为1，所以$S$或$C$都可选，得到SPNE为$(SBB,Ba)$与$(CBB,Ba)$。
  
  故共有5个SPNE。
  
  

### Problem2

将收益矩阵写出，可以得到Nash均衡为$(B, R, U)$和$(T, R,D)$。因此有2个 SPNE。
