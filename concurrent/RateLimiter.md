# RateLimiter
## 算法
### 计数器
#### 实现
* [ratelimit](https://github.com/tomasbasham/ratelimit)
#### 缺点
* 临界点问题
### 滑动窗口
* The simplest way to maintain a rate of QPS is to keep the timestamp of the last granted request, and ensure that (1/QPS) seconds have elapsed since then. For example, for a rate of QPS=5 (5 tokens per second), if we ensure that a request isn't granted earlier than 200ms after the last one, then we achieve the intended rate. If a request comes and the last request was granted only 100ms ago, then we wait for another 100ms. At this rate, serving 15 fresh permits (i.e. for an acquire(15) request) naturally takes 3 seconds.
### Token Bucket(令牌桶)
#### 实现
* [RateLimiter](https://github.com/google/guava/blob/master/guava/src/com/google/common/util/concurrent/RateLimiter.java)
## 分布式限流