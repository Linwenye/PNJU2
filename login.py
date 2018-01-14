import requests
import config

r = requests.post(url='http://p.nju.edu.cn/portal_io/login', data={'username': config.username,
                                                               'password': config.password, })
print(r.text)