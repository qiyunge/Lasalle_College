# Concept, Pattern, Representation

## 一句话理解

机器学习的发展大致经历了三个阶段：

```text
Concept Learning
      ↓
Pattern Learning
      ↓
Representation Learning
```

---

# 1. Concept（概念）

## 核心思想

学习一个明确的定义（Description）。

例如：

```text
Family Car
```

机器试图找到：

```text
IF Seats >= 4
AND Trunk Large
AND Price < 100k
THEN Family Car
```

这里学到的是：

```text
Concept
```

即：

> 什么是家庭车

---

## 特征

- 显式规则
- 人类容易理解
- 可解释性强

---

## 典型模型

- Rule Learning
- Version Space
- Decision Tree（部分）
- Expert System

---

# 2. Pattern（模式）

## 为什么出现？

现实世界很多概念无法写成规则。

例如：

```text
猫
狗
人脸
语音
```

很难找到：

```text
IF EarLength > x
AND NoseWidth < y
THEN Cat
```

这样的规则。

于是机器学习转向：

```text
Pattern Recognition
```

模式识别。

---

## 核心思想

学习：

```text
哪些样本长得像
哪些样本长得不像
```

而不是：

```text
什么是猫
```

---

## 数学本质

Pattern 通常对应：

```text
P(X | Class)
```

或者

```text
P(Class | X)
```

中的统计结构。

---

## 例子

### GMM

```text
Cat Cluster
      ↑
 Gaussian 1

Dog Cluster
      ↑
 Gaussian 2
```

学到的是：

```text
数据分布
```

而不是规则。

---

## 特征

- 统计规律
- 不一定可解释
- 依赖人工特征工程

---

## 典型模型

- Naive Bayes
- Logistic Regression
- SVM
- GMM
- HMM
- Random Forest
- XGBoost

---

# 3. Representation（表示）

## 为什么出现？

Pattern Learning 仍然依赖：

```text
Feature Engineering
```

例如：

```text
耳朵长度
鼻子宽度
尾巴长度
```

这些特征需要人工设计。

---

## 核心思想

机器自己学习特征。

```text
Raw Data
     ↓
Neural Network
     ↓
Representation
     ↓
Prediction
```

---

## 图像识别例子

```text
Image
  ↓
Edges
  ↓
Textures
  ↓
Parts
  ↓
Object
```

最终得到：

```text
h
```

即：

```text
Learned Representation
```

---

## 数学形式

```text
x
 ↓
fθ
 ↓
h
 ↓
g
 ↓
y
```

其中：

```text
h = Representation
```

---

## 特征

- 自动学习特征
- 表达能力极强
- 通常不可解释

---

## 典型模型

- CNN
- RNN
- LSTM
- Transformer
- GPT
- BERT

---

# 三者关系

```text
Concept
    ↑
Pattern
    ↑
Representation
```

---

## Concept

关注：

```text
What is it?
```

例如：

```text
什么是家庭车？
```

输出：

```text
规则
```

---

## Pattern

关注：

```text
What does it look like?
```

例如：

```text
家庭车通常长什么样？
```

输出：

```text
统计规律
```

---

## Representation

关注：

```text
How should data be represented?
```

例如：

```text
如何把数据映射到一个容易分类的空间？
```

输出：

```text
隐藏表示（Hidden Representation）
```

---

# 常见模型归类

| 模型 | Concept | Pattern | Representation |
|--------|----------|----------|----------|
| Rule Learning | ✓ | | |
| Expert System | ✓ | | |
| Decision Tree | ✓ | ✓ | |
| Naive Bayes | | ✓ | |
| Logistic Regression | | ✓ | |
| SVM | | ✓ | |
| GMM | | ✓ | |
| HMM | | ✓ | |
| Random Forest | | ✓ | |
| XGBoost | | ✓ | |
| CNN | | | ✓ |
| RNN | | | ✓ |
| LSTM | | | ✓ |
| Transformer | | | ✓ |
| GPT | | | ✓ |

---

# 从 AI 历史看

## 第一代 AI

```text
Symbolic AI
```

关注：

```text
Concept Learning
```

目标：

```text
学习规则
```

---

## 第二代 AI

```text
Machine Learning
```

关注：

```text
Pattern Learning
```

目标：

```text
学习统计规律
```

---

## 第三代 AI

```text
Deep Learning
```

关注：

```text
Representation Learning
```

目标：

```text
学习表示空间
```

---

# 最终总结

```text
Concept
=
学习定义（Definition）

Pattern
=
学习统计规律（Statistical Regularity）

Representation
=
学习特征空间（Feature Space）
```

现代机器学习：

```text
Machine Learning
≈ Pattern Learning
```

现代深度学习：

```text
Deep Learning
≈ Representation Learning
```

而最早期 AI：

```text
AI
≈ Concept Learning
```