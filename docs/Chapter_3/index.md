# 第3章：类

## 值类型和引用类型

- 浅复制和深复制
- 相等性
https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/object-oriented/objects

## 类

https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/types/classes
https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/object-oriented/
- 声明语法
    - 类成员、命名法https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/coding-style/identifier-names
    - 属性：get、set、init
- 初始化
    - 字段初始值
        - 字段和静态变量自动初始化为**默认值**
    - 构造函数
    - 主构造函数https://learn.microsoft.com/zh-cn/dotnet/csharp/whats-new/tutorials/primary-constructors
    - require
    - readonly
        - 编译时常量constant和运行时常量readonly
    - ref out
        - https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/functional/discards
- 创建对象
- 目标类型new()

## 继承
https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/object-oriented/inheritance
https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/object-oriented/polymorphism
## 静态类

- 用途：实例无关
- 隐式密封

## 记录类
https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/types/records
- 与抽象类的区别：层级/合同
- 简化写法：record
- 不可变性
- 值相等性
- 自动的ToString实现
- 继承

## 接口
https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/types/interfaces
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

# 第4章

## 泛型

https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/types/generics

## 为null性
https://learn.microsoft.com/zh-cn/dotnet/csharp/nullable-references
https://learn.microsoft.com/zh-cn/dotnet/csharp/nullable-migration-strategies

## 迭代器
https://learn.microsoft.com/zh-cn/dotnet/csharp/iterators

# 第5章

## 匿名类型
https://learn.microsoft.com/zh-cn/dotnet/csharp/programming-guide/classes-and-structs/anonymous-types
https://learn.microsoft.com/zh-cn/dotnet/standard/base-types/choosing-between-anonymous-and-tuple

## LINQ
https://learn.microsoft.com/zh-cn/dotnet/csharp/linq/ 一整章

# 第6章 异步

https://learn.microsoft.com/zh-cn/dotnet/csharp/asynchronous-programming/

# 第7章 委托和事件

https://learn.microsoft.com/zh-cn/dotnet/csharp/delegates-overview