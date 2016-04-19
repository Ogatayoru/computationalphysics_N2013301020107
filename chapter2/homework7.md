#第七次作业
- 刘祥干2013301020107

##背景
- 本次作业要求解决棒球运动的有关问题。棒球运动的特点是：球速较高，且带有一定的自旋,导致其飞行轨迹变化多。
- 棒球在空中飞行时，其空气拖拽系数将依赖于速度，并且棒球旋转将使其受到额外的马格努斯力，因而棒球的轨迹可以变得十分复杂。
- 本次作业主要解决课本2.19习题，且在带有空气阻力的情形下讨论.

##正文
- 棒球的飞行是典型的抛体运动，但是棒球在飞行过程中除受到重力作用外，还会受到空气阻力和因棒球旋转产生的马格努斯力，棒球飞行轨迹由下述方程描述:![公式1](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter2/%E5%85%AC%E5%BC%8F1.png)
- S0在棒球的运动速度范围内一般是常量,而B2依赖于速度,其近似公式为:![公式2](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter2/%E5%85%AC%E5%BC%8F2.png)
- 欧拉法求解其运动:![公式3](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter2/%E5%85%AC%E5%BC%8F3.png)
- 为了减小欧拉法带来的误差,将步长设为0.1秒.
- 取初始发射角为45度,初始发射高度为50米.为了看的更多的轨迹信息,落地点取为-100米
- 取初速度为500mph,分别取不同角速度计算,结果如下图
- [这是代码](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter2/homework7.py)
- ![这是图片](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter2/homework7.png)

##小结
- 从计算结果可以看到不同的角速度导致的轨迹差别巨大.

##感谢
- 感谢陈洋遥的代码例子.感谢百度,
