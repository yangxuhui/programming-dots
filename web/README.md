# Web Development
>不知从什么时候开始，我们已经不再关心、甚至根本不知道到底谁调用了我写的程序，反正我写了一个类，甚至从来没有new过，它就跑起来了...我们把模糊的记忆往前推一推，没错，就是在学了Web编程之后...

![Web Development](/images/WebDevelopment.png)
## Web Server Gateway Interfaces
web网关接口用来回答"web服务器如何与web应用程序进行交互"的问题.具体来说，主要是两个问题:
1. 服务器如何把不同的请求参数传递给web应用程序
2. web应用程序如何返回处理结果

![Web Server Gateway Interface](/images/WebServerGatewayInterfaces.png)
### CGI
### WSGI
1. server向web应用程序提供:
    * 一个名为`environ`的dict
    * 一个名为`start_response`的callable对象, `start_response`接受两个参数: `status`和`response_header`
2. 应用程序初始化时(`__init__`, `__call__`)必须接受`environ`和`start_response`作为参数; 在`return`或者`yield`之前必须调用`start_response`

同时，WSGI还有一个目标是支持请求前后处理的"中间件"，包括gzip, recording, proxy, load-balancing...因此，WSGI要求中间件遵守server端和应用程序端的协议.
#### References
* [What is WSGI?](https://wsgi.readthedocs.io/en/latest/what.html)
* [Learn about WSGI](https://wsgi.readthedocs.io/en/latest/learn.html)
### Servlet