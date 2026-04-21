# 第4章：程序结构

## 从顶级语句和基于单个文件的应用迁移到显式Main入口、基于项目的应用

- 入口点、顶级语句和Main方法
    - 命令行参数args、为null性和长度https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/tutorials/how-to-display-command-line-arguments
    - 顶级语句的顺序https://learn.microsoft.com/zh-cn/dotnet/csharp/tutorials/top-level-statements
    - main的修饰符和返回值

- 基于文件和基于项目、以及转换https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/tutorials/file-based-programs
    - 项目的概念
    - csproj文件

## 命名空间的声明和使用
https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/coding-style/coding-conventions 补充前面的约定
- 文件范围（推荐）和块范围的声明（不推荐）
    - 一个文件只声明一个空间
    - 最好只声明一个类、文件的命名
- using语句
    - 全局using、GlobalUsings.cs
    - 隐式using
    - using static
    - 创建别名
- 命名空间与文件结构对应
- 按功能拆分第2章的代码、组织命名空间
    - 单一职责原则
- 推荐命名法：CompanyName.ProductName.Feature

## 程序的组织层次

- 5种
- 访问权限和程序集（推荐internal）

## 异常处理

https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/exceptions/
https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/exceptions/using-exceptions
https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/exceptions/exception-handling
https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/exceptions/creating-and-throwing-exceptions
https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/exceptions/compiler-generated-exceptions

## XML注释
https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/tutorials/xml-documentation

## 版本
https://learn.microsoft.com/zh-cn/dotnet/csharp/versioning