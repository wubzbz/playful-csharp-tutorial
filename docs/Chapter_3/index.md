
# 第3章：类

## 值类型和引用类型

- 浅复制和深复制
- 相等性
    - https://learn.microsoft.com/zh-cn/dotnet/csharp/programming-guide/statements-expressions-operators/equality-comparisons
    - https://learn.microsoft.com/zh-cn/dotnet/csharp/programming-guide/statements-expressions-operators/how-to-test-for-reference-equality-identity

## 类

- https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/types/classes
- https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/object-oriented/
- 声明语法
    - 类成员、命名法：https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/coding-style/identifier-names
    - 属性：get、set、init
        - 表达式主体：https://learn.microsoft.com/zh-cn/dotnet/csharp/programming-guide/statements-expressions-operators/expression-bodied-members
- 初始化
    - 字段初始值
        - 字段和静态变量自动初始化为**默认值**：default
    - 构造函数
    - 主构造函数https://learn.microsoft.com/zh-cn/dotnet/csharp/whats-new/tutorials/primary-constructors
    - require
    - readonly
        - 编译时常量constant和运行时常量readonly
    - ref out
        - https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/functional/discards
- 创建对象:https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/object-oriented/objects
- 目标类型new()

## 继承
- 继承：https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/object-oriented/inheritance
- 回顾内置类型
- 装箱：https://learn.microsoft.com/zh-cn/dotnet/csharp/programming-guide/types/boxing-and-unboxing

## 多态
- 多态：https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/object-oriented/polymorphism
- 方法重写（运行时多态）：https://learn.microsoft.com/zh-cn/dotnet/csharp/programming-guide/classes-and-structs/versioning-with-the-override-and-new-keywords +3
- 方法重载（编译时多态）：重载方法、运算符
- YAGNI原则

## 静态类

- 用途：实例无关
- 隐式密封

## 记录类

- https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/types/records
- 与抽象类的区别：层级/合同
- 简化写法：record
- 不可变性
- 值相等性
- 自动的ToString实现
- 继承

## 接口

- https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/types/interfaces
- https://learn.microsoft.com/zh-cn/dotnet/csharp/advanced-topics/interface-implementation/default-interface-methods-versions +3
- 声明、命名约定、不可实例化
- 实现
- 显式实现
    - 多重实现的冲突
    - 实现暴露内部类的签名
- 继承

## 数据类型的选择

- 简单：内置值类型
- 临时组合：元组
- 固定常量、状态、选项：枚举
- 小型数据：结构体
- 复杂行为、派生：类
- 功能定义、标准：接口
- 值相等性：记录

# 第4章：程序结构

https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/program-structure/

## 从顶级语句和基于单个文件的应用迁移到显式Main入口、基于项目的应用

- 入口点、顶级语句和Main方法
    - 命令行参数args、为null性和长度https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/tutorials/how-to-display-command-line-arguments
    - 顶级语句的顺序https://learn.microsoft.com/zh-cn/dotnet/csharp/tutorials/top-level-statements
    https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/program-structure/top-level-statements
    - main的修饰符和返回值
    https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/program-structure/main-command-line

- 基于文件和基于项目、以及转换https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/tutorials/file-based-programs
    - 项目的概念
    - csproj文件

## 命名空间的声明和使用
https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/program-structure/namespaces
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
- 按功能拆分第3章的代码、组织命名空间
    - 单一职责原则
- 推荐命名法：CompanyName.ProductName.Feature

## 程序的组织层次
https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/program-structure/program-organization
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


# 第5章 项目开发

- 代码风格（标准化）
- 使用Nuget包
- 编译器：https://learn.microsoft.com/zh-cn/dotnet/csharp/roslyn-sdk/
- 编译指令：https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/program-structure/preprocessor-directives
- 调试器
- 测试框架
- 代码清理与重构
- debug/release/publish

# 第6章 泛型与集合

## 扩展

- 扩展方法、扩展成员https://learn.microsoft.com/zh-cn/dotnet/csharp/programming-guide/classes-and-structs/how-to-implement-and-call-a-custom-extension-method
- https://learn.microsoft.com/zh-cn/dotnet/csharp/programming-guide/classes-and-structs/how-to-create-a-new-method-for-an-enumeration

## 泛型

- https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/types/generics
- 泛型接口的协变和逆变：https://learn.microsoft.com/zh-cn/dotnet/csharp/programming-guide/concepts/covariance-contravariance/variance-in-generic-interfaces

## 迭代器
- https://learn.microsoft.com/zh-cn/dotnet/csharp/iterators

## .NET平台类型
- IEnumerable<T>、迭代器和foreach循环：https://learn.microsoft.com/zh-cn/dotnet/csharp/programming-guide/concepts/iterators
- IEquatable<T>和自定义相等性：https://learn.microsoft.com/zh-cn/dotnet/csharp/programming-guide/statements-expressions-operators/how-to-define-value-equality-for-a-type
- 数据结构：List、Stack、Queue、Tree

# 第7章 LINQ

## 匿名类型
https://learn.microsoft.com/zh-cn/dotnet/csharp/programming-guide/classes-and-structs/anonymous-types
https://learn.microsoft.com/zh-cn/dotnet/standard/base-types/choosing-between-anonymous-and-tuple

## LINQ

- https://learn.microsoft.com/zh-cn/dotnet/csharp/linq/ 一整章
- 表达式树：https://learn.microsoft.com/zh-cn/dotnet/csharp/advanced-topics/interface-implementation/default-interface-methods-versions

# 第8章 委托和事件

- https://learn.microsoft.com/zh-cn/dotnet/csharp/delegates-overview
- 委托中的协变和逆变

# 第9章 异步

- https://learn.microsoft.com/zh-cn/dotnet/csharp/asynchronous-programming/
- https://learn.microsoft.com/zh-cn/dotnet/navigate/advanced-programming/

# 第10章 特性和反射

- https://learn.microsoft.com/zh-cn/dotnet/csharp/advanced-topics/reflection-and-attributes/

# 第11章 性能工程

- https://learn.microsoft.com/zh-cn/dotnet/csharp/advanced-topics/performance/

# MAUI

# ASP.NET Core with Blazor

- https://learn.microsoft.com/en-us/aspnet/core/tutorials/choose-web-ui?view=aspnetcore-10.0