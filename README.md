# Programming Dots
## 消息/任务队列
### [beanstalkd](https://github.com/beanstalkd/beanstalkd)
#### Tube
> The "ignore" command will reply "NOT_IGNORED\r\n" if the client attempts to ignore the only tube in its watch list.
#### [Client Libraries](https://github.com/beanstalkd/beanstalkd/wiki/Client-Libraries)
## 监控
### [Metrics](https://metrics.dropwizard.io/3.1.0/getting-started/)
#### Client Libraries
* java
    * [metrics](https://github.com/dropwizard/metrics)
* python
    * [pyformance](https://github.com/omergertel/pyformance)
## Docker
## Signal Handle
### python
* Add signal handler:`signal.signal(signal.SIGALRM, handler)`
* Stop threads using [Event](https://docs.python.org/3/library/threading.html#event-objects)
```python
class App:
    def __init__(self):
        self._stop = threading.Event()
    
    def worker(self):
        while not self._stop.is_set():
            ...
    
    def stop(self):
        self._stop.set()
```
## Code Complexity Analysis Tool
### python
#### [wily](https://github.com/tonybaloney/wily)
## Design Patterns
### Creational Patterns
#### Singleton
* 应用场景
    * 显式确保某个类的对象有且仅有一个
* 实现方式
    * 将构造函数声明为私有成员函数，创建一个静态方法来进行对象的创建
    * [How to implement a configurable singleton?](https://stackoverflow.com/questions/34642170/how-to-implement-a-configurable-singleton)
## Programming Languages
### golang
#### [`init`](https://golang.org/doc/effective_go.html#init)