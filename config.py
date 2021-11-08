import socket

# basic config

USERNAME = ""
PASSWORD = ""

# advance config

config={
    "gatewayUrl" : "https://gw.buaa.edu.cn",
    "USERNAME" : "",
    "PASSWORD" : "",

    "loki_config" : {
            "url": "http://116.62.247.0:3100/loki/api/v1/push",
            "tags": {
                "application": "buaaGatewayAutoLogin",
                "pc": socket.gethostname()
            },
            "version": "1"
        }  # 日志相关
}

config["USERNAME"] = USERNAME
config["PASSWORD"] = PASSWORD

assert USERNAME != ""
assert PASSWORD != ""