from django.db import models


# 创建类实现创建数据库的表
class UserInfo(models.Model):
    name = models.CharField(max_length=32)  # 字符串类型
    password = models.CharField(max_length=64)  # 字符串类型
    age = models.IntegerField(default=25)  # 整数型
    # data = models.IntegerField(default=2)  # 假设为已有前面数据，新要添加的数据必须设置默认值
    # score = models.IntegerField(null=True,blank=True)  # 设置默认值为空

    '''
    上面的类等价于写创建表的SQL语句：
    create table app01_UserInfo(
        id bigint auto_increment primany key,  （默认添加到创建的表）
        name varchar(32),
        password varchar(64),
        age int,
    )
    '''

class Department(models.Model):
    title = models.CharField(max_length=16)

# 新建数据方式
# SQL语句写法  insert into app01_Department(title)values("销售部");
# ORM方式  Department.objects.create(title = "销售部")
# 一般ORM方式写入数据不在此处，在veiws.py文件中，先导入此处的类。

# class Role(models.Model):
#    caption = models.CharField(max_length=16)



