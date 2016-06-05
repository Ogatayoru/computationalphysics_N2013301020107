#第9次作业
###2013301020107 刘祥干
##背景
- 讨论课本上的3.21题
- 混沌现象无处不在,对其研究可以增加我们对非线性的理解.这次作业以的非线性阻尼驱动物理摆为模型讨论其一些有趣的性质

##内容
- 非线性阻尼驱动物理摆的运动方程为:![]()
- 用euler-cromer方法写成离散形式:   $$w(i+1)=w(i)-[(g/l)sin(theta)-qw(i)+F_dsin(Omega*t(i)]*dt$$
                                    $$theta(i+1)=theta(i)+omega(i+1)*dt$$
                                    $$t(i+1)=t(i)+dt$$
                                 
- [代码在此](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/9.1.py)
- 1.选择参数:F_D=5,Omega_D=2,q=1
     theta-t图![]()
     相图![]()
- 2.选择参数:F_D=7,Omega_D=2,q=1 
     theta-t图![]()
     相图![]()
- 3.分岔图:(1)![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/bifurcation%20diagram1.png)
-          (2)可见在6-8之间还有精细结构.![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/bifurcation%20diagram2.png)
-          
- 4.可见F_D=7.2附近有几个分岔点.在分岔点附近选择参数,并使周期更长,以便观察相图上点的分布.
-    F_D=6.9:![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/tree/master/chapter3)
-    F_D=7.1:![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/pp%20phase%20diagram4.png)
-    F_D=7.3:![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/pp%20phase%20diagram6.png)
-    
##结论
- 易见在7.2左边一点还没有出现混沌,在7.2到7.4之间也没有混沌,7.4以后就是完全的混沌了.相图上的点已经几乎全部充满.
-  
##致谢
