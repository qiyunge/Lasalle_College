# 从 Version Space 到 Decision Theory
从概念学习到统计决策理论

——机器学习从 Version Space 到 Risk Minimization 的演化

引言

机器学习的发展并不是一条单一的技术路线，而是经历了多个不同思想体系的演化。从早期的符号学习（Symbolic Learning），到统计学习理论（Statistical Learning Theory），再到现代概率机器学习（Probabilistic Machine Learning）与决策理论（Decision Theory），研究者关注的问题不断发生变化。

在早期人工智能中，人们主要关心：

如何从有限样本中归纳出正确的规则？

这一时期的代表思想包括 Concept Learning、Rule Learning 和 Version Space 等方法，其核心目标是寻找能够解释训练数据的符号规则（Symbolic Rules）。

随着统计学习理论的发展，研究重点逐渐转向：

为什么模型能够泛化到未见过的数据？

Vapnik 提出的 Statistical Learning Theory、VC Dimension、SRM（Structural Risk Minimization）等理论，为理解模型复杂度与泛化能力提供了数学基础。

进入现代机器学习时代后，人们开始认识到：

学习模型并不是最终目标，决策才是最终目标。

概率机器学习将不确定性纳入统一框架，通过概率分布描述知识，通过推断（Inference）获得预测，再通过损失函数（Loss Function）与风险（Risk）评价决策质量。

因此，现代机器学习的核心链条逐渐演化为：

State
↓
Observation
↓
Probability Model
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
↓
Optimization

从这个角度看：

* 符号学习（Symbolic Learning）关注的是“规则”；
* 统计学习理论（Statistical Learning Theory）关注的是“泛化”；
* 概率机器学习（Probabilistic Machine Learning）关注的是“不确定性”；
* 决策理论（Decision Theory）关注的是“行动”。

虽然这些理论关注的问题不同，但它们都围绕同一个核心目标：

从有限信息中学习，并在未来环境中做出更好的决策。

本文将沿着：

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

这一主线，梳理机器学习从符号学习到统计决策理论的发展脉络。
统计学习与概率机器学习

为什么会有两条路线？

学习机器学习时，很多人会发现不同教材关注的问题似乎完全不同。

例如：

* Mitchell 关注 Concept Learning、Version Space；
* Vapnik 关注 VC Dimension、SRM；
* ESL 关注 Bias-Variance、Regularization；
* Murphy 关注 Probability、Inference、Decision。

这些内容并不矛盾，而是机器学习发展过程中不同阶段的关注重点。

⸻

1. Statistical Learning（统计学习）

统计学习的核心问题是：

如何从有限样本中学习一个能够泛化到未来数据的模型？

其研究重点包括：

Function Approximation
Generalization
Capacity
Regularization
Bias-Variance

核心目标：

学习一个好的函数

即：

f(x)

↓

y

⸻

统计学习主要研究：

为什么训练集表现好？
为什么测试集表现也好？

也就是说：

为什么模型能够泛化？

⸻

典型理论：

* ERM（Empirical Risk Minimization）
* SRM（Structural Risk Minimization）
* VC Dimension
* Bias-Variance Tradeoff
* Regularization

⸻

典型模型：

* Linear Regression
* Logistic Regression
* SVM
* Random Forest
* Boosting

⸻

2. Probabilistic Machine Learning（概率机器学习）

概率机器学习关注的问题不同：

如何在不确定性下进行推断和决策？

其研究重点包括：

Probability
Likelihood
Posterior
Inference
Uncertainty
Decision

核心目标：

学习概率分布

而不仅仅是学习一个函数。

⸻

统计学习：

输入
↓
函数
↓
输出

即：

y = f(x)

⸻

概率机器学习：

输入
↓
概率模型
↓
概率分布

即：

p(y|x)

⸻

例如：

统计学习输出：

猫

⸻

概率机器学习输出：

P(猫)=0.9
P(狗)=0.08
P(狐狸)=0.02

因此保留了：

不确定性

的信息。

⸻

3. 两者的关注点

统计学习关注：

模型为什么可靠？

即：

Generalization

⸻

概率机器学习关注：

模型知道自己有多不确定吗？

以及：

面对不确定性如何行动？

⸻

因此：

统计学习关注：

Prediction

⸻

概率机器学习关注：

Prediction
+
Decision

⸻

4. Murphy 属于哪条路线？

Kevin Murphy 的《Probabilistic Machine Learning》属于：

Probabilistic Machine Learning
+
Decision Theory

路线。

⸻

Murphy 的核心思想：

世界
↓
概率模型
↓
推断(Inference)
↓
预测(Prediction)
↓
决策(Decision)

⸻

其统一框架：

State
↓
Observation
↓
Probability Model
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
↓
Optimization

⸻

Murphy 更关注：

如何在不确定环境下做出最优决策

而不是：

为什么模型能够泛化

⸻

5. 两条路线的关系

两者并不是竞争关系。

实际上：

Probabilistic Machine Learning
⊃
Statistical Learning

⸻

统计学习解决：

如何学到一个好的模型

⸻

概率机器学习进一步解决：

如何利用模型进行推断和决策

⸻

6. 机器学习的发展脉络

可以将机器学习的发展理解为：

Symbolic Learning
↓
Concept Learning
↓
Version Space
↓
ERM
↓
SRM
↓
Statistical Learning
↓
Bayesian Learning
↓
Probabilistic Machine Learning
↓
Decision Theory
↓
Reinforcement Learning
↓
Decision Systems

⸻

7. 对现代 AI 的意义

对于现代分类任务：

Statistical Learning

已经足够强大。

⸻

对于：

* Agent
* Reinforcement Learning
* Autonomous Systems
* Robotics
* Decision Systems
* Robustness Engineering

则必须进一步考虑：

Uncertainty
Decision
Risk

因此：

Probability
+
Decision Theory

逐渐成为现代 AI 系统的核心框架。

⸻

一句话总结

统计学习研究：

如何学到一个泛化能力好的模型。

概率机器学习研究：

如何在不确定性下进行推断与决策。

Murphy 的体系属于：

Probability
+
Inference
+
Decision Theory

路线，其最终目标不是预测本身，而是利用预测支持最优决策。

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