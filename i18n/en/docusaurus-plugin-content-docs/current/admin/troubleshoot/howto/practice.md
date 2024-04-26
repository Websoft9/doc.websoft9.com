---
sidebar_position: 4
slug: /troubleshoot/practice
---

# 综合实践指南

本节是一个完整的解决问题综合指南，它遵循 [PDCA](https://wiki.mbalib.com/wiki/戴明循环) 闭环逻辑。

## 是什么?

问题是什么是**战略问题**。如果战略错误，其他的都没有价值，所以问题是什么是最重要的，也是最值得花时间的地方。

### 收集证据 

收集证据主要从如下几个方面着手：  

- 阅读官方文档
- 保护问题现场
- [分析日志](../linux#logs)
- 尝试让问题重现
- 多人访谈与讨论

收集证据阶段要保持**客观、无我**的一种心理状态，努力保持证据完整，切莫在这个阶段进行深入分析以避免主观因素干扰。 

### 推理

根据证据，得出一个符合逻辑的初步结论。然后，再对初步结论进行交叉分析，分析其适应性。

1. [什么类型的问题？](./method/type)
2. 问题流程逻辑
3. 交叉分析

## 怎么解决？

寻找解决问题的方案需要注意如下几个方面：

- 指导思想：遵循**简单实用，大道至简**的哲理，解决问题的方法一定具备**道**的属性，尽量从**大处着手**。  
- 协作原则：多人会诊，充分运用集体的智慧
- 迭代原则：解决问题的方法需能够适应长期的变化，切莫引入新的问题
- 利他原则：让用户更简单，让维护者更方面

在寻找解决方案过程中，仍然需要少量的实验以初步验证假设的可行性。  

## 解决问题

解决问题相对前面的步骤，反而更容易。因为它是相对确认的范围，目标也非常明确。  

主要遵循的方法如下：  

1. 问题拆解：将问题进行**去业务化**的划分，以便可以使用外脑
2. 关键路径：确认问题的关键路径（与业务无关的技术难点），交给最合适的人

## 总结

将问题进行总结升华，完善产品和知识库。  