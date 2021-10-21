# buaaGatewayAutoLogin
北航校园网网关自动登录脚本，挂在实验室服务器上，自动登录，防止断网

## 使用

```
pip install -r .\requirements.txt
```

修改`config.py`中的`USERNAME`和`PASSWORD`

在当前目录执行脚本

```
nohup python .\logintask.py &
```

默认一小时登录一次