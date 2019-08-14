## 1、代码的下载
问题：怎么把一个Git仓库的代码下载到本地?

1. 登录github获取仓库拷贝地址:<https://github.com/Gunnine/Pintuan>
2. 打开终端使用以下命令下载所有代码
 
  1》cd一个下载目录
 
  2》git clone XXX.git 代码会被下载到当前目录
 
  3》cd近代码文件 输入ls 查看拷贝代码中的文件
  
  4》发现只有一个文件，为什么呢?
 因为默认使用的是master分支，而master分支

 里我没放代码。 此时，需要用 git checkout 命令来转入指定分支。

 5》git branch 查看当前分支

    git branch -a 查看所有分支

    git checkout xx 转入分支

 6》可以用pycharm查看项目代码

## 2、工具类 RestClient 请求客户端
问题1：那么为什么写这个类？
>假如我们不用这个类,收发请求一般是requests来做。

例1：reuqests收发请求的示例：

----
```
response = requests.post("http://csp.nhsoft.cn/post",data={"a":"b"})
print(reponse.text)
```
----

但是这样的请求之间没有关联，当我们需要一些连续请求时，比如“先登录再把商品加入购物车“，这时，需要使用 requests 的 session 功能。伪代码示例如下:

例2：requests session 收发请求的伪代码示例：

----
```
session = requests.session()
```
### #登录伪代码
```
response = session.post("http://csp.nhsoft.cn/login",
data={"username":"aaa","password":"bbb"})
print(response.text)
```
----
### #将一个商品加入购物车伪代码
```
response = session.post("http://csp.nhsoft.cn/cart"，data={"aaa":"b"})
print(response.text)
```
### #分析
例2的两个请求都由同一个requests session对象发出，两个请求带了同一个header信息
与cookie,所以可以完成先登录再购物的操作

### #思考
除了公用session还有什么地方可以优化?
>不足：按照例2的写法需要每个请求都写一遍完整的url

>改进:我们可以建一个类自动给所有url加上前缀

例3：增加了代码前缀功能的RestClient类
```
import requests,json
class RestClient():
    def __init__(self,api_root_url):
        self.api_root_url=api_root_url
        self.session = requests.session()

    def get(self,url, **kwargs):
        return self.request(url,"get",**kwargs)

    def post(self,url,data=None,json=None,**kwargs):
        return self.request(url, "post",data,json,**kwargs)

    def options(self, url, **kwargs):
        return self.request(url, "potions", **kwargs)

    def head(self, url, **kwargs):
        return self.request(url, "head", **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, "put", data,**kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, "patch", data,**kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "delete", **kwargs)

    def request(self,url,method_name,data=None,json=None,**kwargs):
        url = self.api_root_url+url
        if method_name == "get":
            return self.session.get(url, **kwargs)
        if method_name == "post":
            return self.session.post(url, data, json, **kwargs)
        if method_name == "options":
            return self.session.options(url, **kwargs)
        if method_name == "head":
            return self.session.head(self, url, **kwargs)
        if method_name == "put":
            return self.session.put(self, url, data, **kwargs)
        if method_name == "patch":
            return self.session.patch(self, url, data, **kwargs)
        if method_name == "delete":
            return self.session.delete(self, url, **kwargs)
```


1. init方法：初始化这个类，初始化的时候需要输入api_root_url，也就是URL的前缀。
另外还在初始化时创建了self.session用于保存requests的session。

2. get,post等各种http方法，用于让用户使用。但这里并没有真正实现这些方法，
因为这些方法都是在requests里有实现过，我们只要把参数传给requests就行了。
这个传递我们写在request方法里，所以这里的http方法都是调用requests方法。

3. request方法:真正调用self.session的各种方法，这里同样是把参数传下去，
只是在传之前，给所有用户输入的url加了一个前缀。前缀的值是用户在init方法输入的。

例4：运行例3的类代码

----
```
r=RestClient("http://csp.nhsoft.cn")
x= r.post("/post",json= {"a":"b"})
print(x.text)
```
----

## 3、代码的提交
  1》cd 进项目
  2》git status 查看项目状态
  3》git add xx
  4》git commit -m "提交备注"
  5》git push

## 4、代码更新
 1》git fetch 可拉取新分支
 2》git pull 更新

