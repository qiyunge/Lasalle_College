# AI / ML 核心概念总结

# 1. Rule（规则）

规则：

```python
if speed > 100:
    brake()
```

特点：

* 人工编写
* 确定性
* 可解释
* 可证明
* 通常是逻辑约束

适合：

* safety
* business logic
* invariant
* constraint

例如：

* 红灯必须停
* 年龄小于18禁止注册
* 系统状态检查

---

# 2. Algorithm（算法）

算法：

```text
输入 -> 明确计算过程 -> 输出
```

例如：

* Dijkstra
* A*
* BFS / DFS
* Dynamic Programming
* Sorting
* Physics Simulation

算法不一定是简单 rule。

它更强调：

```text
状态推进过程
```

例如：

```text
simulation loop
time advance
graph traversal
```

所以：

```text
Rule 更偏逻辑约束
Algorithm 更偏计算过程
```

---

# 3. ML（Machine Learning）

ML：

```text
从数据学习映射
```

例如：

```text
image -> class
text -> probability
state -> action score
```

不是人工写规则。

而是：

```text
参数通过优化得到
```

例如：

* Neural Network
* Logistic Regression
* Random Forest

---

# 4. Rule + ML + Simulation + Search

现代智能系统常常是：

```text
Rule + ML + Simulation + Search
```

## Rule

负责：

* safety
* constraint
* invariant

## ML

负责：

* perception
* prediction
* scoring

## Simulation

负责：

```text
如果这样做，会发生什么？
```

例如：

* physics engine
* scheduling simulator
* digital twin

## Search

负责：

```text
应该尝试哪个可能性？
```

例如：

* BFS
* A*
* MCTS
* Beam Search

---

# 5. Discriminative vs Generative

## Discriminative（判别式）

学习：

```text
P(Y|X)
```

或者：

```text
X -> Y
```

重点：

```text
分类边界
```

例如：

* Logistic Regression
* SVM
* Neural Network classifier

---

## Generative（生成式）

学习：

```text
P(X,Y)
```

或者：

```text
P(X|Y)
+
P(Y)
```

重点：

```text
数据是如何生成的
```

例如：

* Naive Bayes
* GMM
* HMM

---

# 6. GMM（Gaussian Mixture Model）

GMM 假设：

```text
数据由多个 Gaussian 混合生成
```

公式：

```text
p(x)=Σ π_k N(x|μ_k,Σ_k)
```

学习：

* cluster center
* covariance
* mixture weight

本质：

```text
概率生成结构
```

---

# 7. HMM（Hidden Markov Model）

HMM：

```text
存在隐藏状态
只能看到观测
```

学习：

## 状态转移

```text
P(z_t | z_{t-1})
```

## 发射概率

```text
P(x_t | z_t)
```

用于：

* speech recognition
* NLP
* sequence modeling

---

# 8. Association Rule Mining

例如：

```text
beer -> chips
confidence = 0.7
```

这类：

```text
不是 hard rule
而是 statistical pattern
```

即：

```text
机器发现统计关联
```

不是：

```text
人手工写逻辑规则
```

---

# 9. Representation Learning

现代 Deep Learning 核心：

```text
不是学习显式规则
而是学习表示空间
```

例如：

```text
h = latent representation
```

模型内部通常不是：

```text
if edge then digit 7
```

而是：

```text
高维连续向量空间
```

---

# 10. Hidden State h_t

RNN 中：

```text
h_t
```

既是：

* hidden layer output
* hidden state / memory

公式：

```text
h_t = f(W_h h_{t-1} + W_x x_t + b)
```

表示：

```text
当前上下文压缩表示
```

---

# 11. OCR（文字识别）

早期 OCR：

```text
image -> character probability
```

最后输出：

```text
softmax probability
```

例如：

```text
[0.01, 0.02, 0.90, ...]
```

表示：

```text
当前字符属于某类的概率
```

---

# 12. Softmax 输出层

最后一层：

```text
y = softmax(Wh+b)
```

输出：

```text
类别概率分布
```

例如：

```text
cat: 0.8
dog: 0.1
car: 0.1
```

---

# 13. 神经网络内部到底学到什么？

通常不是：

```text
显式逻辑规则
```

而是：

```text
feature representation
```

例如：

* edge
* texture
* shape
* semantic direction

这些通常：

```text
不可直接解释
```

---

# 14. 可解释 vs 不可解释

## 强可解释

* if-else rule
* decision tree
* association rule

## 部分可解释

* linear regression
* GMM
* HMM

## 弱可解释

* random forest
* boosting

## 难解释

* deep neural network
* transformer hidden state

---

# 15. Symbolic AI vs Deep Learning

## Symbolic AI

强调：

* logic
* rule
* causality
* reasoning

## Deep Learning

强调：

* representation
* optimization
* high-dimensional pattern

---

# 16. 现代 AI 一个核心问题

现代模型很强：

```text
但不知道它内部真正学到了什么
```

因此才有：

* interpretability
* explainable AI
* mechanistic interpretability
* causal representation

这些研究方向。
