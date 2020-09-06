---
title: Go 语言笔试面试题汇总
seo_title: 极客面试
date: 2020-09-04 20:10:10
description: Go 语言/golang 笔试题，面试题，基础语法与内部原理/实现，包括不限于垃圾回收机制(GC)、面向对象、并发编程等。
tags:
- Go
nav: 面试
categories:
- Go 语言面试题
image: post/qa-golang/go_questions.jpg
top: 3
github: https://github.com/geektutu/interview-questions
---

![golang interview questions](qa-golang/go_questions.jpg)

**[Go 语言笔试面试题汇总](https://geektutu.com/post/qa-golang.html)，[Github](https://github.com/geektutu/interview-questions)**

## [基础语法](https://geektutu.com/post/qa-golang-1.html)

- 01 `=` 和 `:=` 的区别？
- 02 指针的作用
- 03 Go 允许多个返回值吗？
- 04 Go 有异常类型吗？
- 05 什么是协程（Goroutine）
- 06 如何高效地拼接字符串
- 07 什么是 rune 类型
- 08 如何判断 map 中是否包含某个 key ？
- 09 Go 支持默认参数或可选参数吗？
- 10 defer 的执行顺序
- 11 如何交换 2 个变量的值？
- 12 Go 语言 tag 的用处？
- 13 如何判断 2 个字符串切片（slice) 是相等的？
- 14 字符串打印时，`%v` 和 `%+v` 的区别
- 15 Go 语言中如何表示枚举值(enums)？
- 16 空 struct{} 的用途

## [实现原理](https://geektutu.com/post/qa-golang-2.html)

- 01 init() 函数是什么时候执行的？
- 02 Go 语言的局部变量分配在栈上还是堆上？
- 03 2 个 interface 可以比较吗 ？
- 04 2 个 nil 可能不相等吗？
- 05 简述 Go 语言GC(垃圾回收)的工作原理
- 06 函数返回局部变量的指针是否安全？
- 07 非接口非接口的任意类型 T() 都能够调用 `*T` 的方法吗？反过来呢？

## [并发编程](https://geektutu.com/post/qa-golang-3.html)

- 01 无缓冲的 channel 和有缓冲的 channel 的区别？
- 02 什么是协程泄露(Goroutine Leak)？
- 03 Go 可以限制运行时操作系统线程的数量吗？