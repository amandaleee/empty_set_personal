from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

# *Field is an instance of a Field class - CharField, DateTimeField, etc. The name of each field instance
#       [question_text, choice_text] is machine-friendly, and this is the column name.
#
# You can use an optional first arg in the Field, like I've done with Question below. This is the human-readable
#       name of the field.
#
# ForeignKey is what defines a relationship. below, the question column shows what question each Choice
#       model instance maps to.

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)