#第十四次作业
- 刘祥干 2013301020107

##背景
- 弦上的机械波是经典力学里经典的波动问题.
- 波动问题在物理学里随处可见,是重要的一类动力学问题.对其有运动有一些直观的认识有助于提高我们的物理直觉.本文简单的计算弦上两个波包的叠加.和其运动图景
- ![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter6/%E5%9B%BE%E7%89%871.png)
- 不难从推导出弦上的波动方程

##内容
- 弦上的波动方程为:
                                                                                                                            
    ![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter6/%E6%96%B9%E7%A8%8B1.png)

- 化为差分方程进行数值求解:
    ![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter6/%E6%96%B9%E7%A8%8B2.png)
                 
- 1.考虑高斯型波包的运动[代码1](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter6/14.3.py):

 ![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter6/14.3.png)
            
- 2.波包叠加的动态图像[代码2](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter6/14.1.py):
![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter6/14.1.gif)


##结论
- 容易看出,在边界出有半波损失,与经典力学中的结论一致.

##致谢
- 感谢张志诚同学和郭潇同学提供的范例.
- reference:1.<<数学物理方法>>姚端正
            2.课本
