#第十一次作业
- 刘祥干 2013301020107

##背景
- 行星运动可以用牛顿万有引力定律描述,本文讨论双星系统.
- 双星系统在宇宙中最常见也最简单的多体系统.
- 平方反比有心力场中的运动是稳定的.本文顺便探讨对平方反比定律的偏离所带来的影响,可以定性地得到近似的和广义相对论相同的结论.

##内容
- newton万有引力定律方程为:
    ![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter4/homework11/%E5%85%AC%E5%BC%8F1.png)
    
- 与牛顿第二定律结合,可以得到行星的运动轨迹.而对于二体问题可以引入约化质量u,使二体问题化为单体问题.可以精确求解:
    ![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter4/homework11/%E5%85%AC%E5%BC%8F2.png)
    
- 则可以导出轨道方程为:
    ![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter4/homework11/%E5%85%AC%E5%BC%8F3.png)
    
- 其中e为离心率,与系统的角动量和能量相关.e大于1为双曲线轨道,e等于1为抛物线轨道,e小于1为椭圆轨道.
- 平方反比定律下,在M1/M2为2时.描述其运动轨道[代码](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter4/homework11/11.1.py):

    ![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter4/homework11/11.1.png)
    
- 偏离平方反比定律时,讨论不同偏离带来的影响:
   n=1.97时,不同离心率的情况:
   ![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter4/homework11/11.2.png)
   
  n= 2.03时,不同离心率的情况:
   ![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter4/homework11/11.3.png)
   

##结论
- 1.容易看出平方反比定律下轨道很稳定,不同初始条件下轨道的形状不同.但都是闭合的椭圆,
- 2.与n=2偏离一点后,轨道明显不再闭合,而是有一定的进动.与广义相对论结论一样.
- 3.离心率越大,进动越明显.且进动速率和离心率大致成线性关系.

##致谢
- 感谢王铮同学给出的范例.
- reference:课本
