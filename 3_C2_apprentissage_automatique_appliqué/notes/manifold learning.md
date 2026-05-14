# Manifold Learning 学习笔记

## 1. 什么是 Manifold Learning

Manifold Learning（流形学习）：

核心思想：

```text
现实数据虽然位于高维空间，
但真正自由度往往很低
```

因此：

```text
高维数据
通常分布在某个低维结构上
```

这个低维结构：

叫做：

```text
manifold（流形）
```

---

## 2. 什么是 manifold（流形）

直觉理解：

```text
局部像低维空间，
整体可能是弯曲复杂结构
```

---

### 地球表面的例子

地球：

```text
三维物体
```

但：

人在地表移动时：

只需要：

```text
经度 + 纬度
```

即：

```text
二维坐标
```

因此：

```text
二维曲面
嵌入在三维空间
```

这就是 manifold。

---

## 3. AI 中的 manifold

例如：

一张图片：

```text
1024 × 1024 × 3
```

维度极高。

但：

真实自然图片：

不会随机分布在整个像素空间。

因为：

随机像素大概率只是噪声。

真正自然图片：

通常只存在于：

```text
高维空间中的很小区域
```

即：

```text
data manifold
```

---

## 4. 最关键的思想

现实数据：

虽然表面高维，

但真正变化因素很少。

例如人脸：

可能真正变化的只有：

- 年龄
- 朝向
- 光照
- 表情
- 发型

于是：

```text
人脸数据
其实位于低维流形上
```

而不是：

```text
均匀分布在整个像素空间
```

---

## 5. Manifold Learning 的目标

目标：

```text
找到数据隐藏的低维结构
```

即：

```text
发现数据真正的自由度
```

---

## 6. 为什么这很重要

如果找到 manifold：

很多问题会突然简单。

例如：

- 分类
- 聚类
- 压缩
- 推理
- 生成
- 泛化

因为：

```text
真实数据结构
远比原始维度简单
```

---

## 7. 与 latent space 的关系

latent space 很多时候可以理解为：

```text
manifold 的坐标系
```

即：

### Encoder

做的是：

```text
把高维数据
映射到流形坐标
```

---

### Decoder

做的是：

```text
从流形重新展开世界
```

---

## 8. 一个经典例子

假设：

“旋转中的数字 6”

图片维度很高。

但真正变化因素：

可能只有：

```text
旋转角度
```

因此：

所有图片实际上形成：

```text
一个低维连续流形
```

甚至近似：

```text
环状 manifold
```

---

## 9. Deep Learning 为什么有效

现代观点：

深度学习强大，

不仅因为：

```text
万能函数逼近
```

更因为：

```text
它能逐渐学习数据的 manifold structure
```

---

## 10. Curse of Dimensionality

高维空间有个重要问题：

```text
Curse of Dimensionality
```

即：

```text
高维空间极其稀疏
```

大部分区域：

```text
根本没有真实数据
```

因此：

直接在原始空间学习：

很困难。

---

而 manifold learning 认为：

```text
真实数据
集中在低维流形附近
```

于是：

问题变得可学习。

---

## 11. 常见 Manifold Learning 方法

### PCA

Principal Component Analysis

核心思想：

```text
寻找数据变化最大的方向
```

假设：

```text
数据近似位于线性流形
```

---

### t-SNE

强调：

```text
局部邻域关系
```

适合：

- embedding visualization
- cluster visualization

---

### UMAP

相比 t-SNE：

- 更快
- 更保留全局结构
- 更适合大型 embedding

---

### Isomap

尝试：

```text
保留 manifold 上的测地距离
```

---

### LLE

Locally Linear Embedding

核心思想：

```text
局部线性
整体非线性
```

---

## 12. 与现代 AI 的关系

现代 AI 很多本质都在：

```text
学习世界流形
```

---

### Diffusion Model

学习：

```text
自然图像流形
```

---

### LLM

学习：

```text
语言语义流形
```

---

### RL / World Model

学习：

```text
环境状态流形
```

---

## 13. 一个非常重要的观点

现代 AI 越来越不像：

```text
函数拟合器
```

而更像：

```text
几何结构学习器
```

即：

```text
学习：
现实数据
如何分布在高维空间中
```

---

## 14. 与 latent representation 的联系

latent representation：

本质上是在寻找：

```text
适合推理的流形坐标
```

好的 latent：

意味着：

- 更容易推理
- 更容易泛化
- 更容易生成
- 更容易规划

---

## 15. 与当前研究方向的联系

以下问题：

- state abstraction
- semantic structure
- world model
- decision state
- simulation
- robustness

本质上都与：

```text
寻找适合推理的 manifold
```

相关。

因为：

一个“好状态”：

本质上是：

```text
位于正确流形坐标上的表示
```

---

## 16. 一个最终总结

现代 AI 的核心流程可以理解为：

```text
高维现实
↓
学习 manifold structure
↓
构造 latent representation
↓
在 latent manifold 中推理
↓
再展开为现实表达
```

因此：

现代 AI 的核心问题越来越变成：

```text
世界应该如何被表示
```

而不仅仅是：

```text
输入如何映射到输出
```