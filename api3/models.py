from django.db import models
from learn_drf import settings

# Create your models here.
class BaseModel(models.Model):
    '''基模型'''
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        '''设置为抽象的'''
        abstract = True


class Course(BaseModel):
    course_name = models.CharField(max_length=128)
    hours=models.IntegerField()
    price=models.DecimalField(decimal_places=2,max_digits=5)
    school = models.ForeignKey(to="School", on_delete=models.CASCADE,  # 级联删除
                                db_constraint=False,  # 删除后对应的字段可以为空
                                related_name="courses", )  # 反向查询的名称
    teachers = models.ManyToManyField(to="Teacher", db_constraint=False, related_name="courses")

    class Meta:
        db_table = "zhf_course"
        verbose_name = "课程表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course_name


class School(BaseModel):
    school_name = models.CharField(max_length=128)
    pic = models.ImageField(upload_to='img', default="img/1.jpg")
    address = models.CharField(max_length=256)

    @property
    def img(self):
        '''这里重写了pic，返回了一个图片的全路径,说实话，暂时用不到'''
        return "%s%s%s" % ("http://127.0.0.1:8000/",settings.MEDIA_URL,self.pic)

    class Meta:
        db_table = "zhf_school"
        verbose_name = "学校"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.school_name


class Teacher(BaseModel):
    teacher_name = models.CharField(max_length=128)
    age=models.IntegerField()
    class Meta:
        db_table = "zhf_teacher"
        verbose_name = "老师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.teacher_name


class TeacherDetail(BaseModel):
    phone = models.CharField(max_length=11)
    salary = models.DecimalField(decimal_places=2, max_digits=5)
    teacher = models.OneToOneField(to="Teacher", on_delete=models.CASCADE, related_name="detail")

    class Meta:
        db_table = "zhf_teacher_detail"
        verbose_name = "教师详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s的详情" % self.teacher.teacher_name