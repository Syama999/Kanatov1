from django.db import models
from django.contrib.auth.models import User
from sortedm2m.fields import SortedManyToManyField

# Create your models here.
class Student(models.Model):
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    name = models.CharField(max_length = 50,verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=60, verbose_name='Отчество', blank=True)
    group = models.ForeignKey('Group', on_delete=models.PROTECT, verbose_name='Группа', blank=True, null=True)
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    user_photo = models.ImageField(verbose_name='Аватарка', blank=True, null=True, default='img.png')

    def __str__(self):
        return f"{self.name} {self.surname} {self.patronymic}"

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Group(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название группы')
    curs = models.IntegerField(default=1, verbose_name='Курс', blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name


class Subject(models.Model):
    subject_name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', )

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return f"{self.subject_name}"


class Lecturer(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=60, verbose_name='Отчество', blank=True)
    groups = models.ManyToManyField('Group', verbose_name='Группы', blank=True)
    subjects = models.ManyToManyField('Subject', verbose_name='Предметы', blank=True)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return f"{self.name} {self.surname} {self.patronymic}"


class StudentScores(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, verbose_name='Студент')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, verbose_name='Предмет', blank=True, null=True)
    lecturer = models.ForeignKey('Lecturer', on_delete=models.CASCADE, verbose_name='Преподаватель', blank=True, null=True)
    cause = models.CharField(max_length=70, verbose_name='Причина', )
    points = models.PositiveIntegerField(verbose_name='Баллы', default=0)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    date = models.DateField(auto_now_add=True, verbose_name="Дата")

    class Meta:
        verbose_name = 'Баллы студента'
        verbose_name_plural = 'Баллы студентов'

    def __str__(self):
        return f"{self.student}-{self.subject}-{self.date}"


class Facultet(models.Model):
    code = models.CharField(max_length=200, verbose_name='Код')
    name = models.CharField(max_length=200, verbose_name='Имя факультета')

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'

    def __str__(self):
        return self.name
