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