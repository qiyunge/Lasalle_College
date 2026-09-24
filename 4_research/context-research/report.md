明天汇报时，不要照着论文念

你口头上其实只需要讲清楚一条故事线：

第一步：模型能力从哪里来？
模型经过 pre-training 和 post-training 后参数被冻结，但 frozen model 有能力不等于每次 inference 都能表现出这种能力。

然后：

$$ \theta_{\text{frozen}} + C_t \rightarrow \text{Effective Behavior} $$

第二步：那 context 是什么？
我把它看成 frozen model 的 inference-time program。它不只是 user prompt，还包括 instruction、memory、tools、retrieved evidence、environment state 等。所以 context 一方面赋予模型当前任务所需要的信息和能力，另一方面也是控制模型行为的 harness。

然后进入 Agent：

第三步：Agent 为什么让这个问题变重要？
因为 Agent 长时间运行后，available information \(H_t\) 会越来越大，但是每一次真正交给模型的 working context \(C_t\) 是有限的。

画一个最简单的图：

$$ \boxed{H_t} \xrightarrow{\pi} \boxed{C_t} \xrightarrow{f_\theta} \boxed{y_t} $$

然后讲 memory 类比：

这有点像 computer memory system。系统有大量 information，但当前 computation 只需要 working set。所以问题不是“能不能把所有东西塞进 window”，而是“当前到底应该让模型看到什么”。

接下来三篇论文各用一句话，不要陷进去：

Lost in the Middle：

信息在 context 里，不代表模型能同样有效地使用它。

MemGPT：

context/memory 可以像有限系统资源一样被主动管理。

LongMemEval-V2：

长期 Agent memory 不只要考虑 accuracy，也需要考虑 retrieval/context cost 和 latency。

最后停在你自己的问题：

$$ \boxed{ \text{Does Lost-in-the-Middle still exist?} } $$

↓

$$ \boxed{ \text{Is full context really better than selective context?} } $$

↓

$$ \boxed{ \text{Should context selection itself be adaptive?} } $$

然后告诉老师：

I do not plan to start with reinforcement learning or train another manager model. I want to keep the model frozen, build a controlled evaluation harness, reproduce the position/context-length experiments on modern models, compare several context strategies, and then implement a lightweight adaptive policy.

我觉得这句话尤其重要，因为它会让导师马上知道这个项目是能落地的，而不是一个“我要解决所有 context engineering 问题”的巨大课题。

而且你明天甚至可以在最后一页只留这一张图：

$$ \boxed{ \text{Available Information }H_t } $$ $$ \downarrow $$ $$ \boxed{ \text{Context Policy }\pi } $$ $$ \downarrow $$ $$ \boxed{ \text{Working Context }C_t } $$ $$ \downarrow $$ $$ \boxed{ \text{Frozen Model }f_\theta } $$ $$ \downarrow $$ $$ \boxed{ \text{Effective Behavior} } $$

然后最后一句：

My research focuses on the middle of this pipeline: how to construct the working context, rather than how to retrain the model.

这句话非常适合收尾，也把你的研究边界钉死了。