# MiniAppArticleSpider
自动抓取小程序社区(微信小程序、百度智能小程序、蚂蚁金服小程序)文章并页面展示

## 安装
```
# scrapy
pip install scrapy

# Flask
pip install Flask
```

## 运行
```
# 服务器启动 (URL: http://0.0.0.0:5000/)
python app.py

# 爬虫启动
python main.py

# 服务器部署
nohup python app.py >/dev/null 2>&1 &

# 定时启动爬虫 (23:25启动)
25 23 * * * /usr/bin/python /home/miniapp/main.py
```

## 效果

[在线体验 http://article.hiandroid.net](http://article.hiandroid.net/) <br/>

![](./screenshot/s1.png)

## 抓取网页
- https://developers.weixin.qq.com/community/
- https://openclub.alipay.com/index.php?c=thread&a=subforum&orderby=postdate&fid=66&theme=
- www.wxapp-union.com
- https://github.com/Tnfe/TNFE-Weekly


## 致谢
- [jinja2](http://docs.jinkan.org/docs/jinja2/)
- [flask](http://docs.jinkan.org/docs/flask/patterns/templateinheritance.html#template-inheritance)
- [SUI Mobile](http://m.sui.taobao.org/getting-started/)