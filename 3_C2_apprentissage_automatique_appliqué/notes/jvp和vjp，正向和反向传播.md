这张图是在讲：把一个 K 层 MLP 看成 K 个函数连续复合，然后用链式法则反向求梯度。

核心结构是：

x1 = x
x2 = f1(x1, θ1)
x3 = f2(x2, θ2)
...
xK+1 = fK(xK, θK)

L = xK+1

也就是说，整个网络可以写成：

L = fK(fK-1(...f1(x, θ1)...), θK)
1. Forward pass：前向传播

第 2 行：

x1 := x

输入 x 被记作第一层输入 x1。

第 3-4 行：

for k = 1 : K do
    x{k+1} = fk(xk, θk)

意思是第 k 层接收：

输入：xk
参数：θk
输出：x{k+1}

例如普通神经网络一层通常是：

zk = Wk xk + bk
x{k+1} = σ(zk)

这里把线性变换 + 激活函数整体打包成：

fk(xk, θk)

其中：

θk = {Wk, bk}
2. Backward pass：反向传播

反向传播的目标是求：

每一层参数的梯度：∇θk L
输入的梯度：∇x L

图中用了两个重要变量：

uk：loss 对 xk 的梯度
gk：loss 对 θk 的梯度

更准确地说：

uk = ∂L / ∂xk
gk = ∂L / ∂θk
3. 为什么 uK+1 := 1？

第 6 行：

uK+1 := 1

因为算法假设：

L = xK+1

所以：

∂L / ∂xK+1 = 1

这就像：

L = y
dy/dy = 1

这是反向传播的起点。

实际神经网络里，通常不是直接：

L = xK+1

而是：

L = loss(xK+1, y)

那这一步就会变成：

uK+1 = ∂L / ∂xK+1

例如交叉熵损失、MSE 损失都会先给出这个初始梯度。

4. 第 8 行：求参数梯度 gk

图中第 8 行：

gk := u{k+1}^T · ∂fk(xk, θk) / ∂θk

意思是：

L 对 θk 的梯度
=
L 对 x{k+1} 的梯度
×
x{k+1} 对 θk 的梯度

也就是链式法则：

∂L/∂θk = ∂L/∂x{k+1} · ∂x{k+1}/∂θk

因为：

x{k+1} = fk(xk, θk)

所以：

∂x{k+1}/∂θk = ∂fk/∂θk

因此：

gk = ∇θk L
5. 第 9 行：把梯度继续传回上一层

图中第 9 行：

uk^T := u{k+1}^T · ∂fk(xk, θk) / ∂xk

意思是：

L 对 xk 的梯度
=
L 对 x{k+1} 的梯度
×
x{k+1} 对 xk 的梯度

也就是：

∂L/∂xk = ∂L/∂x{k+1} · ∂x{k+1}/∂xk

这一步就是“误差往前一层传播”。

所以：

u{k+1} 是后一层传来的梯度
uk 是传给前一层的梯度
6. 直观理解：u 是“责任信号”

可以这样理解：

u{k+1} 表示：
最终 loss 对第 k 层输出 x{k+1} 有多敏感

然后第 k 层用它做两件事：

第一，更新自己的参数：

gk = ∇θk L

第二，把责任继续传给上一层：

uk = ∇xk L

所以每一层都像一个中间节点：

接收后面传来的梯度
计算自己的参数梯度
再把梯度传给前面
7. 为什么是从 K 到 1？

因为网络是复合函数：

x → f1 → f2 → ... → fK → L

loss 在最右边。

要知道前面某一层对 loss 的影响，必须先知道后面层的影响。

所以顺序是：

先算最后一层梯度
再算倒数第二层
...
最后算第一层

这就是反向传播。

8. 最后一行输出什么？

第 11 行：

Return L = xK+1, ∇x L = u1, {∇θk L = gk : k = 1 : K}

输出三个东西：

1. L：最终 loss
2. u1：loss 对输入 x 的梯度
3. g1, g2, ..., gK：每一层参数的梯度

训练神经网络真正需要的是：

gk = ∇θk L

然后用梯度下降更新参数：

θk ← θk - η gk

一句话总结：

前向传播：保存每一层的 xk
反向传播：从 L 开始，用链式法则逐层计算梯度
gk：用于更新第 k 层参数
uk：用于把梯度继续传给前一层

Backpropagation、VJP、JVP 综合理解

你现在已经接近 autodiff（自动微分）的核心了。

真正的核心只有一句话：

Backpropagation
=
Reverse-mode Automatic Differentiation
=
连续执行 VJP

而：

Forward-mode AD
=
连续执行 JVP
1. 神经网络本质：复合函数

MLP：

x1 = x
x2 = f1(x1, θ1)
x3 = f2(x2, θ2)
...
xK+1 = fK(xK, θK)

L = xK+1

整体：

L = fK ∘ fK-1 ∘ ... ∘ f1

即：

一个巨大复合函数
2. Jacobian 是什么？

对于：

y = f(x)

若：

x ∈ Rn
y ∈ Rm

则：

J = ∂f/∂x

是：

m × n

矩阵。

它描述：

输入微小变化
如何影响输出
3. JVP：Jacobian-Vector Product

JVP：

Jv

即：

(∂f/∂x) v

意义：

输入方向 v
经过函数传播后
输出如何变化

本质：

传播 perturbation（扰动）

方向：

从前往后

即：

"
4. VJP：Vector-Jacobian Product

VJP：

vᵀ J

即：

vᵀ (∂f/∂x)

意义：

输出的 sensitivity
向输入传播

本质：

传播 gradient / sensitivity

方向：

从后往前

即：

"
5. Backprop 中的 u 是什么？

图中的：

uk = ∂L/∂xk

表示：

loss 对第 k 层输入的敏感度

或者：

gradient signal

例如：

u{k+1}
=
∂L/∂x{k+1}

已经知道后，

第 k 层继续传播：

ukᵀ
=
u{k+1}ᵀ · ∂fk/∂xk

这一步就是：

VJP

因为：

vector × Jacobian
6. 所以 Backprop 真正做了什么？

不是：

先构建完整 Jacobian

而是：

直接计算：
uᵀ J

即：

VJP
7. 为什么不能构建完整 Jacobian？

假设：

x ∈ R1,000,000
y ∈ R1,000,000

则 Jacobian：

10^12 个元素

完全不可存储。

但：

VJP

只需：

一次局部链式法则

复杂度：

≈ forward 的常数倍

这才使深度学习可训练。

8. Forward-mode vs Reverse-mode
Forward-mode（JVP）

传播：

输入扰动

形式：

v1 = J1 v0
v2 = J2 v1
...
"

即：

连续 JVP

回答：

“输入变一点，
输出怎么变？”
Reverse-mode（VJP）

传播：

loss sensitivity

形式：

uK-1 = uKᵀ JK
...
"

即：

连续 VJP

回答：

“输出对输入有多敏感？”
9. 为什么深度学习用 Reverse-mode？

神经网络：

参数极多

例如：

θ ∈ R100M

但：

loss 是标量

即：

L ∈ R

Reverse-mode：

一次 backward
得到所有参数梯度

极高效。

而 Forward-mode：

若参数很多：

需要对每个参数单独传播

成本爆炸。

所以：

10. 一个最重要的统一理解
Forward-mode
传播：
“变化”

即：

perturbation flow
Reverse-mode
传播：
“责任”

即：

sensitivity flow
11. 最后统一成一句话
神经网络反向传播
不是在构建 Jacobian

而是在不断执行：

vector × Jacobian

即：

VJP

图中的：

uk

本质就是：

已经累计传播到当前位置的梯度信号

整个 backprop：

就是 sensitivity 在计算图中的反向流动