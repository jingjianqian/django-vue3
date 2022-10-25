from django.db import models


# Create your models here.

# 年级表模型
class Grade(models.Model):
    grade_year = models.IntegerField()  # 年级年份
    grade_name = models.CharField(max_length=256)  # 班级名称
    grade_index = models.IntegerField()  # 年级序号
    objects = models.Manager()


# 学生表模型
class Student(models.Model):
    student_name = models.CharField(max_length=64)  # 学生姓名
    student_sex = models.CharField(max_length=3)  # 学生性别
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    student_id = models.IntegerField()  # 学号
    objects = models.Manager()


# 课程表
class Course(models.Model):
    course_id = models.IntegerField()  # 课程id
    course_name = models.CharField(max_length=256)  # 课程名称
    objects = models.Manager()


# 平时分记录表
class GeneralScore(models.Model):
    score_type = models.BooleanField()  # true是加分，false是减分
    score_value = models.IntegerField()  # 分数变化类型
    mark = models.CharField(max_length=255)  # 备注
    objects = models.Manager()


# 学生课程关联表
class StudentCourse(models.Model):
    student_id = models.IntegerField()  # 学生id
    course_id = models.IntegerField()  # 课程id
