---
title: Go 语言笔试面试题(并发编程)
seo_title: 极客面试
date: 2020-09-05 23:10:10
description: Go 语言/golang 笔试题，面试题，基础语法与内部实现原理，包括不限于垃圾回收机制(GC)、面向对象、并发编程等。
tags:
- Go
nav: 面试
categories:
- Go 语言面试题
image: post/qa-golang/go_questions.jpg
github: https://github.com/geektutu/interview-questions
---

![golang interview questions](qa-golang/go_questions.jpg)

**[Go 语言笔试面试题汇总](https://geektutu.com/post/qa-golang.html)，[Github](https://github.com/geektutu/interview-questions)**

## Q1 无缓冲的 channel 和 有缓冲的 channel 的区别？

<details>
<summary>答案</summary>
<div>

对于无缓冲的 channel，发送方将阻塞该信道，直到接收方从该信道接收到数据为止，而接收方也将阻塞该信道，直到发送方将数据发送到该信道中为止。

对于有缓存的 channel，发送方在没有空插槽（缓冲区使用完）的情况下阻塞，而接收方在信道为空的情况下阻塞。

例如:

```go
func main() {
	st := time.Now()
	ch := make(chan bool)
	go func ()  {
		time.Sleep(time.Second * 2)
		<-ch
	}()
	ch <- true  // 无缓冲，发送方阻塞直到接收方接收到数据。
	fmt.Printf("cost %.1f s\n", time.Now().Sub(st).Seconds())
	time.Sleep(time.Second * 5)
}
```

```go
func main() {
	st := time.Now()
	ch := make(chan bool, 2)
	go func ()  {
		time.Sleep(time.Second * 2)
		<-ch
	}()
	ch <- true
	ch <- true // 缓冲区为 2，发送方不阻塞，继续往下执行
	fmt.Printf("cost %.1f s\n", time.Now().Sub(st).Seconds()) // cost 0.0 s
	ch <- true // 缓冲区使用完，发送方阻塞，2s 后接收方接收到数据，释放一个插槽，继续往下执行
	fmt.Printf("cost %.1f s\n", time.Now().Sub(st).Seconds()) // cost 2.0 s
	time.Sleep(time.Second * 5)
}
```


</div>
</details>

## Q2 什么是协程泄露(Goroutine Leak)？

<details>
<summary>答案</summary>
<div>

协程泄露是指协程创建后，长时间得不到释放，并且还在不断地创建新的协程，最终导致内存耗尽，程序崩溃。常见的导致协程泄露的场景有以下几种：

- 缺少接收器，导致发送阻塞

这个例子中，每执行一次 query，则启动1000个协程向信道 ch 发送数字 0，但只接收了一次，导致 999 个协程被阻塞，不能退出。

```go
func query() int {
	ch := make(chan int)
	for i := 0; i < 1000; i++ {
		go func() { ch <- 0 }()
	}
	return <-ch
}

func main() {
	for i := 0; i < 4; i++ {
		query()
		fmt.Printf("goroutines: %d\n", runtime.NumGoroutine())
	}
}
// goroutines: 1001
// goroutines: 2000
// goroutines: 2999
// goroutines: 3998
```

- 缺少发送器，导致接收阻塞

那同样的，如果启动 1000 个协程接收信道的信息，但信道并不会发送那么多次的信息，也会导致接收协程被阻塞，不能退出。

- 死锁(dead lock)

两个或两个以上的协程在执行过程中，由于竞争资源或者由于彼此通信而造成阻塞，这种情况下，也会导致协程被阻塞，不能退出。

- 无限循环(infinite loops)

这个例子中，为了避免网络等问题，采用了无限重试的方式，发送 HTTP 请求，直到获取到数据。那如果 HTTP 服务宕机，永远不可达，导致协程不能退出，发生泄漏。

```go
func request(url string, wg sync.WaitGroup) {
	for {
		if _, err := http.Get(url); err == nil {
			// write to db
			break
		}
		time.Sleep(time.Second)
	}
	wg.Done()
}

func main() {
	var wg sync.WaitGroup
	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go request(fmt.Sprintf("exampe.com/%d", i), wg)
	}
	wg.Wait()
}
```

</div>
</details>

## Q3 Go 可以限制运行时使用的CPU核数吗？

<details>
<summary>答案</summary>
<div>

可以使用 `runtime.GOMAXPROCS(num int)` 设置，例如：

```go
runtime.GOMAXPROCS(1) // 限制使用的逻辑核数为 1
```

</div>
</details>
