# 机器学习&编程面试笔试题

## 序言

持续整理、更新Python、机器学习(Machine Learning)、深度学习(Deep Learning)领域的面试笔试题(interview questions)。

声明：所有习题系博主花费大量精力整理，请尊重劳动成果，未经许可，禁止原文转载。

## 目录

### 机器学习

- [机器学习面试题 01-10](https://geektutu.com/post/qa-ml-1.html)，[md](qa-ml/qa-ml-1.md)
- [机器学习面试题 11-20](https://geektutu.com/post/qa-ml-2.html)，[md](qa-ml/qa-ml-2.md)

### Go 语言

- [Go 语言笔试面试题(基础语法)](https://geektutu.com/post/qa-golang-1.html)
- [Go 语言笔试面试题(实现原理)](https://geektutu.com/post/qa-golang-2.html)
- [Go 语言笔试面试题(并发编程)](https://geektutu.com/post/qa-golang-3.html)
- [Go 语言笔试面试题(代码输出)](https://geektutu.com/post/qa-golang-c1.html)

## 相关链接

- [知乎专栏](https://zhuanlan.zhihu.com/geektutu)
- [Go 语言笔试面试题](https://geektutu.com/post/qa-golang.html)
- [机器学习笔试面试题](https://geektutu.com/post/qa-ml.html)，[Github](https://github.com/geektutu/interview-questions)
- [TensorFlow 2.0 中文文档](https://geektutu.com/post/tf2doc.html)，[Github](https://github.com/geektutu/tensorflow2-docs-zh)
- [TensorFlow 2.0 图像识别&强化学习实战](https://geektutu.com/post/tensorflow2-mnist-cnn.html)，[Github](https://github.com/geektutu/tensorflow-tutorial-samples)

## 选择题示例

使用决策树分类时，如果输入的某个特征的值是连续的，通常使用二分法对连续属性离散化，即根据是否大于/小于某个阈值进行划分。如果采用多路划分，每个出现的值都划分为一个分支，这种方式的最大问题是：

- A 计算量太大
- B 训练集和测试集表现都很差
- C 训练集表现良好，测试集表现差
- D 训练集表现差，测试集表现良好

<details>
<summary>答案</summary>
<div>

**C** 连续值通常采用二分法，离散特征通常采用多路划分的方法，但分支数不宜过多。
连续特征每个值都划分为一个分支，容易过拟合，泛化能力差，导致训练集表现好，测试集表现差。
</div>
</details>


对神经网络(neural network)而言，哪一项对过拟合(overfitting)和欠拟合(underfitting)影响最大。

- A 隐藏层节点(hidden nodes)数量
- B 学习速率(learning rate)
- C 初始权重
- D 每一次训练的输入个数固定

<details>
<summary>答案</summary>
<div>

**A** 过拟合和欠拟合与神经网络的复杂程度有关，模型越大越容易过拟合。隐藏层节点数量直接决定了模型的大小与复杂程度。
</div>
</details>

## 问答题示例

经验误差(empirical error)与泛化误差(generalization error)分别指？

<details>
<summary>答案</summary>
<div>
经验误差: 也叫训练误差(training error)，模型在训练集上的误差。
泛化误差: 模型在新样本集(测试集)上的误差。
</div>
</details>

简述 K折交叉验证(k-fold crossValidation)。

<details>
<summary>答案</summary>
<div>
- 数据集大小为N，分成K份，则每份含有样本N/K个。每次选择其中1份作为测试集，另外K-1份作为训练集，共K种情况。
- 在每种情况中，训练集训练模型，用测试集测试模型，计算模型的泛化误差。
- 将K种情况下，模型的泛化误差取均值，得到模型最终的泛化误差。
</div>
</details>

## 附：题目主要来源

- [Machine Learning exam - CMU](http://www.cs.cmu.edu/~tom/10701_sp11/prev.shtml)
- [Andrew Ng - coursera](https://www.coursera.org/learn/machine-learning)