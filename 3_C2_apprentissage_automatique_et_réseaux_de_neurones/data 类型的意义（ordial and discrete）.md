数据类型中的 Ordinal 与 Numerical 本质理解
1. 核心思想

一个数据：

是否被看作“数值（numerical）”，
并不取决于它是不是数字。

而取决于：

这些数字之间的数学运算是否有意义。

例如：

距离是否有意义
加减是否有意义
比例是否有意义
平均值是否有意义
2. 同一个数据，可以有不同理解方式

例如：

满意度
1
2
3
4
5

它可以被看作：

A. Ordinal（有序类别）

表示：

等级
排序
顺序关系

即：

1 < 2 < 3 < 4 < 5

但：

不一定意味着：

5 比 1 大 4 单位
4 和 5 的差距等于 1 和 2 的差距

这里：

更关注：

分类与顺序

B. Numerical（数值）

如果我们假设：

间隔相等
数值差异有意义

那么：

它可以进入：

平均值
回归
欧氏距离
梯度优化

这时：

更关注：

数值关系

3. 本质区别
Ordinal

核心：

顺序（order）

但：

不保证：

间隔一致
距离可测量

例如：

教育水平
小学
初中
高中
大学

这里只知道：

小学 < 初中 < 高中 < 大学

Numerical

核心：

数学结构

允许：

加减
平均
距离
比例

例如：

身高
170
180

这里：

180 − 170 有真实意义。

4. 数据类型的真正本质

统计学真正关心的不是：

数据长什么样

而是：

允许什么运算（allowed operations）

5. Stevens 四种经典尺度
(1) Nominal

只是标签：

红色
蓝色
男
女

只允许：

相等
不相等
(2) Ordinal

有顺序：

low
medium
high

允许：

大于
小于

但：

不保证间隔。

(3) Interval

间隔有意义。

例如：

摄氏温度。

30°C − 20°C 有意义。

但：

0°C 不是真正“没有温度”。

所以：

30°C 不是 15°C 的两倍热。

(4) Ratio

比例有意义。

例如：

重量。

20kg 真的是 10kg 的两倍。

因为：

0kg 是绝对零点。

6. 当分析 attribute 关系时，使用什么模型？

取决于：

你如何理解这些数据。

7. 数值关系模型（Numerical Relationship Model）

适用于：

continuous
interval
ratio
部分 discrete numerical

研究：

距离
变化率
线性关系
梯度

例如：

y=wx+b
w
b

常见方法：

regression
correlation
covariance
PCA
8. 类型关系模型（Categorical Relationship Model）

适用于：

nominal
categorical
部分 ordinal

研究：

联合分布
条件概率
类别依赖
信息量

例如：

P(A∣B)=
P(B)
P(A∩B)
	​

P(B)
P(A∩B)
P(A∣B)=
P(B)
P(A∩B)
	​

≈0.46
P(B)=0.65
P(A∩B)=0.30
P(A|B) ≈ 0.46
A∩B is the part of B where A also happens

常见方法：

contingency table
chi-square
mutual information
9. 一个重要误区

很多人：

把类别直接数字化：

男=0
女=1

然后：

直接做距离计算。

这是危险的。

因为：

0 和 1：

很多时候只是 label。

不是连续空间中的点。

10. ML 中的现实情况

现代 ML：

经常：

把类别映射为向量。

例如：

word embedding。

于是：

原本：

“类型关系”

变成：

“几何关系”。

这是深度学习非常核心的思想。

11. 最核心总结

真正重要的不是：

数据是不是数字

而是：

你是否认为这些数字之间的数学关系有意义。

12. 一句话总结
看法	关注点
Ordinal	分类与顺序
Numerical	距离与数值关系

因此：

“一个数据是不是数值型”，本质上是一个建模假设（modeling assumption）。