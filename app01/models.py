from django.db import models

# Create your models here.


class Department(models.Model):
    """部门模型类"""

    # 部门名称, 字符串类型 max_length  最大长度
    name = models.CharField(max_length=20)
    # 部门成立时间  日期类型
    create_date = models.DateField()
    is_delete = models.BooleanField(default=False)

    # Ctrl + o 重写方法
    def __str__(self):
        return self.name


class Employee(models.Model):
    """员工"""

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    # 性别 0表示男
    sex = models.IntegerField(default=0)
    # 999999.99
    # decimal_places小数点位数
    # max_digits 总位数
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    # 备注信息
    comment = models.CharField(max_length=500)
    # 外键: 所属的部门
    department = models.ForeignKey('Department')


class Employee2(models.Model):
    """员工"""

    name = models.CharField(default='hh',max_length=20)
    name2 = models.CharField(max_length=20)
    age = models.IntegerField()
    # 性别 0表示男
    sex = models.IntegerField(default=0)
    # 999999.99
    # decimal_places小数点位数
    # max_digits 总位数
    salary2 = models.DecimalField(max_digits=8, decimal_places=2)
    # 备注信息
    comment = models.CharField(max_length=500)
    # 外键: 所属的部门
    department = models.ForeignKey('Department')
