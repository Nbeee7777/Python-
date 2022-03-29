# Python-
本文主要使用 1. requests 发送请求，从服务器获取数据 2. BeautifulSoup 解析整个页面的源代码。爬取优美图库图片，分享思路、代码供大家参考。





# 前言


博主为控制科学与工程专业研究生，非科班出身，在课题之余学习编程，将代码与大家分享，代码中需要改进的地方欢迎讨论。
参考资料：[https://www.bilibili.com/video/BV1BY411E7Pi?spm_id_from=333.999.0.0](https://www.bilibili.com/video/BV1BY411E7Pi?spm_id_from=333.999.0.0)。





# 一、开发环境
Python == 3.9
requests == 2.26.0
beautifulsoup4 == 4.10.0





# 二、网站分析
## 1.发送请求到服务器，找到每套图片的链接地址
![在这里插入图片描述](https://img-blog.csdnimg.cn/e1f71c0b92bc4677a0ad47cbd4969267.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATmJlZWU3Nzc3,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)



## 2.进入套图获取图片的下载链接
![在这里插入图片描述](https://img-blog.csdnimg.cn/84dec3768e5244c4a8d69f2f464f289b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATmJlZWU3Nzc3,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)



## 3.找到套图中每张图片链接的特点
![在这里插入图片描述](https://img-blog.csdnimg.cn/3ed6a60fe56545c6bfbbca59d717f156.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATmJlZWU3Nzc3,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)



# 三、代码示例







---

# 总结
效果如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20ff235039e344a19e517cdea450a2db.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATmJlZWU3Nzc3,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)





以上为本文分享的内容，本文仅简单对requests与bs4命令的使用，有很多地方还需要学习，欢迎讨论。
