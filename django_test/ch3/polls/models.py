from django.db import models

# Create your models here.

from django.db import models


# id(자동생성) , question_text(varchar(200)) , pub_date(datetime)
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # 객체를 문자열로 표현
    def __str__(self):
        return self.question_text


# id(자동생성) , choice_text(varchar(200)), votes(integer), question_id(integer)
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # 객체를 문자열로 표현
    def __str__(self):
        return self.choice_text
