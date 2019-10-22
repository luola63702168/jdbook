#   scrapy+scrapy_redis实现jd图书信息增量式爬虫
## 特殊说明
- 自带断点续爬。
- redis仅充当中间件作用。
- 本项目未将数据存储于redis中，如需存入，需要要进行以下两个操作
    1， 将jd.py文件62行修改为 return item
    2，将settings.py的 ITEM_PIPELINES配置项取消注释。
## 字段参考
{'b_cate': '小说', 's_href': 'https://list.jd.com/1713-3258-3304.html', 's_cate': '侦探/悬疑/推理', 'book_img': 'https://img11.360buyimg.com/n7/jfs/t1/29218/3/9128/261796/5c7c869aEcb9e2566/3f830a4e6fa876f3.
jpg', 'book_name': '福尔摩斯探案全集（珍藏版 套装共6册）', 'book_author': [' 阿瑟·柯南道尔 '], 'book_press': '北方文艺出版社', 'book_publish_date': '2009-03', 'book_sku': '10650506', 'book_price': '81.30'}
{'b_cate': '小说', 's_href': 'https://list.jd.com/1713-3258-3298.html', 's_cate': '中国近现代小说', 'book_img': 'https://img13.360buyimg.com/n7/jfs/t1/65302/40/6710/295568/5d4d3a65E6dddbd5f/fcfc042aa96fbce7
.jpg', 'book_name': '作家榜经典文库：官场现形记 （讲透官场的教科书式经典小说！了解官场的必读经典！未删减插图珍藏版，套装共2册）', 'book_author': [' 李宝嘉 '], 'book_press': '华东师范大学出版社', 'book_publi
sh_date': '2018-08', 'book_sku': '12402053', 'book_price': '86.60'}
{'b_cate': '小说', 's_href': 'https://list.jd.com/1713-3258-3304.html', 's_cate': '侦探/悬疑/推理', 'book_img': 'https://img10.360buyimg.com/n7/jfs/t16333/336/2678336175/268456/ceda4fc1/5ac1d3b1N7f34141b.jp
g', 'book_name': '鲁班的诅咒：珍藏版大全集（套装全5册）', 'book_author': [' 圆太极 '], 'book_press': '江苏凤凰文艺出版社', 'book_publish_date': '2018-03', 'book_sku': '12320660', 'book_price': '235.60'}
{'b_cate': '小说', 's_href': 'https://list.jd.com/1713-3258-3304.html', 's_cate': '侦探/悬疑/推理', 'book_img': 'https://img13.360buyimg.com/n7/jfs/t17449/305/2537263701/378861/9340b9a/5afd4446N842e3f68.jpg
', 'book_name': '丹·布朗作品：达·芬奇密码（2018年新版）（精装）', 'book_author': [' 丹·布朗 '], 'book_press': '人民文学出版社', 'book_publish_date': '2018-05', 'book_sku': '12352923', 'book_price': '59.8
0'}


