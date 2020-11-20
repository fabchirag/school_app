from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.name


