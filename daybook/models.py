from django.db import models
image = models.ImageField(upload_to='media')


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Attendance(models.Model):
    emp_id = models.CharField(max_length=200)
    emp_name = models.CharField(max_length=200)
    attend_date = models.DateTimeField('date published')
    attend_status = models.CharField(max_length=1)
