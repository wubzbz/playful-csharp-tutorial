# 前言


20XX年，三体人入侵地球。由于过去数十年来人工智能（AI）的飞速发展，人类对其依赖的程度逐渐加深，越来越多的技能被人们遗忘。“非物质文化遗产”是人类把它们扫进历史的故纸堆之前，留下的最后一瞥……

然而，随着掌握了碾压级科技水平的三体文明轻而易举地把地球上的AI全部瘫痪后，工厂里的机器人、道路上的交通工具、房间里的智能家具，乃至身上穿戴的智能设备接连停止运转，人类面临着真正的生存危机。

重建人类文明的希望，就落在了那些不愿放弃“过时技能”的人身上——包括现在正学习编程的你🫵！

呃呃、不瞎扯了。总之，这是一个既简单又有趣的C#编程语言教程。

!!! warning

    本教程尚未完成，正持续更新。


## 都什么年代了还学C#？

非常好的问题。

在可预见的未来，AI的编程能力一定会超过人类。到那时，“搬砖”式的机械劳动与重复工作一定会被全面取代。基础开发工作有可能完全移交给AI Agent，整个项目所需的人类也许只剩顶尖的架构师 ~~（还有甲方）~~ 。也就是说，想通过掌握这门语言来混口饭吃必然会越来越难。这就是现实。

那么，现在还有必要学C#吗？本教程还有阅读的意义吗？关于这些问题，我肯定给不出比付费商业课程的宣传语更动听的回答。

至少在当下，想要提高与AI协作的效率，还是值得亲自学习C#的。当Copilot给你生成一大堆代码后，你怎么知道它们能否按照**你的**意愿工作？其中会有潜在的问题吗？再退一步讲，就算你完全信任AI生成代码的质量，你真的**会**给AI下达指令吗？你能用精确的语言描述你的想法，让AI立刻明白要做什么，而不是东拉西扯半天后气得破防大骂AI不好用吗？

#### <center>AI能给你答案，却不能代替你思考。</center>

有了计算器后，会珠算的人变少了，但会算数的人没有。这就是我想说的，也是贯穿于本教程的思想。

## 这篇教程能让你学会什么？

一共就4样东西：

1. 扎实的C#**编程功底**。（废话，不然为什么叫C#教程
2. 正式项目的**构建**、**测试**与**维护**能力。
3. 通用的**程序设计**思维与**架构**视野。
4. 跨平台应用和Web应用的开发能力。

## 这篇教程有哪些特点？

- 🧠 从零开始，真·初学者视角
- 🗣️ 用人话讲C#，拒绝黑话与机翻
- 🚀 紧跟C#最新特性，与时俱进
- 📚 按专题组织章节，而非按语法横向切割，力求讲全讲透
- 🛠️ 即学即用的实战项目与挑战
- 🎯 注重引导思考，培养思维能力
- 💻 覆盖从基础语法到全栈应用的完整路径

## 谁适合看这篇教程？

|身份|推荐程度|理由|
|----|-------|----|
|学龄前儿童|⭐|学习本教程需要先掌握自然语言。|
|小学生|⭐|就算再怎么简化，也难免需要数学和英语基础。|
|初中生|⭐⭐⭐|对编程感兴趣的同学可以看着玩（或者玩着看）。看不懂的地方可以跳过。|
|高中生|⭐⭐⭐⭐|你的知识水平已经足够理解全部内容了。但学这个需要牺牲你宝贵的课外时间。|
|0基础学习者|⭐⭐⭐⭐⭐|这篇教程就是为你定制的。当然，不会打开电脑的那种0基础另说。|
|被反自学教程劝退的人|⭐⭐⭐⭐⭐|这篇教程就是为你定制的。|
|有专业背景的学习者|⭐⭐⭐⭐⭐|无论看什么教程你都能学会。你可以跳过已经会了的部分。|
|希望XX天速成的学习者|⭐|你看看这个教程的目录有多长就知道这是不可能的。|
|人工智能|⭐⭐|你更适合阅读结构化的文档，而不是把token浪费在听我瞎扯。|
|三体人|❓|你想用C#做甚？|

无论你是谁，**兴趣**与**坚持**都是你打开成功之门的钥匙🔑。毕竟这篇教程真的很长。请记住，**学会这些内容的门槛正是学成之后的你的价值**。💪

## 谁创作了这篇教程？

- 内容设计：wubzbz（人类）
- 正文全文：wubzbz（人类）
- 插图：wubzbz（人类）
- 信息搜集：豆包（AI）、Deepseek（AI）、wubzbz（人类）
- 校对：Deepseek（AI）、wubzbz（人类）

## 为什么要创作这篇教程？

作为一个更习惯从文字，而非视频中学习的人，我主要是通过Microsoft提供的C#[官方文档](https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/)、[语言参考](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/)等资料学习这门语言。尽管官方教程的准确性毋庸置疑，我却深深地震惊于其混乱不堪的编排组织和不知所云的“微软式中文”。当然，附带的一些[课程](https://learn.microsoft.com/zh-cn/training/paths/get-started-c-sharp-part-1/)和[培训](https://www.freecodecamp.org/learn/foundational-c-sharp-with-microsoft/)等资源对于学习者而言非常有帮助，但它们停留在浅尝辄止的基础阶段，又或是没有形成连贯的体系。这导致我学完后，对于自己能干什么、要干什么完全没有概念，距离实现有价值的产出更是十万八千里。

在从0开始自学的过程中，我见过遣词造句十分专业、描述抽象的 ~~（睡眠改善向）~~ 教程；也见过默认读者具有相当的知识储备和理解能力，不愿意多解释哪怕一句话的教程……但是，我也读过讲解自然流畅、语言风趣幽默、内容扎实全面的 ~~（追着喂饭式）~~ 教程，它们是名副其实的照亮学习者前行之路的火炬🔥。受到它们的启发，这篇C#教程诞生了！

## 参考资料

此教程主要参考了：

- [C# documentation](https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/)
- [C# language reference](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/)

在此感谢所有的.NET贡献者！💕

## 备注

<a href="https://github.com/wubzbz/playful-csharp-tutorial">playful-csharp-tutorial</a> © 2024 - 2026 by <a href="https://github.com/wubzbz">wubzbz</a> is licensed under <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/sa.svg" style="max-width: 1em;max-height:1em;margin-left: .2em;">
