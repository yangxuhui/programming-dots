## 衰减
### 指数衰减(Exponential decay)
* `exp(-(冷却系数) * 时间间隔)`
* "冷却系数"是一个你自己决定的值
## 基于用户投票的排名算法
根据用户的投票，决定最近一段时间内的"热文排名"。
* 单位时间内用户的投票数进行排名
* [Hacker News](https://news.ycombinator.com/item?id=1781013)
    * `(votes - 1) / pow((item_hour_age+2), gravity) // gravity = 1.8`
* [How Reddit ranking algorithms work](https://medium.com/hacking-and-gonzo/how-reddit-ranking-algorithms-work-ef111e33d0d9)
* [Stack Overflow](http://www.ruanyifeng.com/blog/2012/03/ranking_algorithm_stack_overflow.html)

不考虑时间因素，基于用户投票排序
* [威尔逊区间](http://www.ruanyifeng.com/blog/2012/03/ranking_algorithm_wilson_score_interval.html)
* [贝叶斯平均](http://www.ruanyifeng.com/blog/2012/03/ranking_algorithm_bayesian_average.html)