from django.db import models

# Create your models here.
from django.contrib.auth.models import User

#分类
class Category(models.Model):  #Django要求模型必须继承models.Model类
    #Category只需要一个简单的分类名name就可以
    name = models.CharField(max_length=100)  
    #CharField指定了分类名name的数据类型，CharField是字符型
    #CharField的max_length参数指定其最大长度，超过这个长度的分类名就不能被存入数据库
    def __str__(self):
        return self.name

#标签
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

#文章
class Post(models.Model):
    #文章标题
    title = models.CharField(max_length=70)
    #文章正文
    body = models.TextField()
    #文章的创建时间和最后一次修改时间，存储时间的字段用DateTimeField类型
    created_time = models.DateField()
    modified_time = models.DateField()
    #默认情况下CharField要求我们必须存入数据，否则就会报错
    #指定CharField的blank=True参数值后就可以允许空值了。
    excerpt = models.CharField(max_length=200,blank=True)

    category = models.ForeignKey(Category,None)
    tags = models.ManyToManyField(Tag,blank=True)

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    author = models.ForeignKey(User,None)
    def __str__(self):
        return self.title