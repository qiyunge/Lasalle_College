# 从 Version Space 到 Decision Theory

## 1. Concept Learning（概念学习）

早期机器学习关注的问题：

> 哪些假设（Hypothesis）能够解释训练数据？

定义：

```text
Hypothesis Space H
```

表示所有可能的分类规则。

例如：

```text
h(x) = Positive
if x 位于某个矩形内
```

---

### Version Space

Version Space 定义：

VS(H,D)

= 所有与训练集 D 完全一致的假设

即：

```text
Training Error = 0
```

的全部模型。

---

### S 和 G

Most Specific Hypothesis：

```text
S
```

最保守解释。

---

Most General Hypothesis：

```text
G
```

最宽松解释。

---

真实概念可能位于：

```text
S ≤ h ≤ G
```

之间。

因此：

```text
Version Space
=
所有可能正确的解释
```

---

## 2. Version Space 的问题

如果：

```text
Training Error = 0
```

的模型有很多个，

应该选哪一个？

---

例如：

```text
h1
h2
h3
...
```

都完全正确。

---

于是产生新的问题：

```text
哪个模型泛化最好？
```

---

# 3. ERM（Empirical Risk Minimization）

经验风险最小化：

ERM

核心思想：

```text
定义 Loss
↓
最小化 Loss
```

---

Loss：

单次错误代价

L(y, ŷ)

例如：

```text
分类错误 = 1
分类正确 = 0
```

---

经验风险：

R̂(h)

=

(1/n)

Σ L(yi,h(xi))

---

目标：

h*

=

argmin R̂(h)

---

即：

```text
训练误差最小
```

---

代表：

- Logistic Regression
- Neural Network
- XGBoost

本质都属于 ERM。

---

## 4. ERM 的问题

如果模型特别复杂：

```text
Training Error = 0
```

非常容易实现。

例如：

```text
100个样本
100万参数
```

---

此时：

```text
训练误差很小
```

但：

```text
测试误差很大
```

出现：

```text
Overfitting
```

---

# 5. SRM（Structural Risk Minimization）

Vapnik 提出：

仅仅最小化经验风险不够。

还需要控制：

```text
模型复杂度
```

---

思想：

```text
真实风险
≈
经验风险
+
复杂度
```

---

形式：

R(h)

≤

R̂(h)

+

Complexity(H)

---

因此：

SRM

=

ERM

+

Complexity Control

---

即：

```text
SRM ⊃ ERM
```

---

SRM 不是比 ERM 更高级，

而是：

```text
SRM 包含 ERM
```

并进一步研究：

```text
为什么模型能泛化
```

---

# 6. VC Dimension

VC：

Vapnik-Chervonenkis Dimension

---

核心问题：

```text
模型有多复杂？
```

---

定义：

一个模型家族能够：

```text
Shatter
```

（打散）

的最大点数。

---

Shatter：

对于 n 个点，

所有：

2^n

种分类方式，

模型都能实现。

---

VC Dimension：

```text
能够被完全打散的最大点数
```

---

例如：

| 模型 | VC Dimension |
|--------|--------|
| 常数分类器 | 0 |
| 一维阈值分类器 | 1 |
| 区间分类器 | 2 |
| 二维直线分类器 | 3 |
| d维超平面 | d+1 |

---

VC 越大：

```text
模型容量越大
```

同时：

```text
过拟合风险越高
```

---

# 7. SVM 与 SRM

Version Space 中：

可能存在很多：

```text
Training Error = 0
```

的解。

---

SVM 不随便选择。

而是：

```text
选择 Margin 最大的解
```

---

Margin：

决策边界到最近样本的距离。

---

Margin 越大：

```text
对噪声越鲁棒
泛化能力越强
```

---

因此：

```text
SVM
=
SRM 思想的代表模型
```

---

# 8. Murphy 的路线

Murphy 的关注点不同。

他不主要研究：

```text
为什么能泛化？
```

而研究：

```text
如何在不确定性下做决策？
```

---

核心链条：

```text
Probability
↓
Inference
↓
Prediction
↓
Decision
↓
Loss
↓
Risk
```

---

## Loss

Loss：

单次决策代价

L(y,a)

---

例如：

```text
误诊一次
```

造成的损失。

---

## Risk

Risk：

期望损失

R(a)

=

E[L(Y,a)]

---

表示：

```text
长期平均代价
```

---

目标：

a*

=

argmin E[L(Y,a)]

---

即：

```text
选择风险最小的行动
```

---

# 9. SRM 与 Murphy 的区别

SRM：

研究：

```text
模型为什么可靠
```

关注：

```text
Generalization
```

---

Murphy：

研究：

```text
决策为什么合理
```

关注：

```text
Decision
```

---

SRM 的 Risk：

```text
预测风险
```

---

Murphy 的 Risk：

```text
决策风险
```

---

两者都使用：

```text
Risk
```

这个概念。

但目标不同。

---

# 10. 统一理解

可以把机器学习的发展理解为：

```text
Concept Learning
↓
Version Space
↓
ERM
↓
SRM
↓
Bayesian Learning
↓
Decision Theory
```

---

各自回答的问题：

Version Space：

```text
哪些模型可能正确？
```

---

ERM：

```text
哪个模型训练误差最小？
```

---

SRM：

```text
哪个模型泛化最好？
```

---

Bayesian Learning：

```text
哪个模型后验概率最大？
```

---

Decision Theory（Murphy）：

```text
哪个行动的期望风险最小？
```

---

对于现代 AI Agent / RL / Decision System：

重点通常是：

```text
State
↓
Observation
↓
Prediction
↓
Decision
↓
Loss
↓
Risk
↓
Optimization
```

因此 Murphy 的概率与决策框架通常比 VC/SRM 更直接。

但 VC/SRM 仍然是理解泛化与正则化的重要理论基础。