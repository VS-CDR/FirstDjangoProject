from django.db import models
from django.contrib.auth.models import User


class CalcHistory(models.Model):
    """
    :param expression: сгенерированное вычисляемое выражение
    :param res: результат выражения
    """
    expression = models.TextField()
    res = models.IntegerField()


class StrHistory(models.Model):
    """
    :param date: дата
    :param time: время
    :param input_str: введённая строка
    :param cnt_words: кол-во слов в строке
    :param cnt_symbols: кол-во символов в строке
    :param client: :class: 'django.contrib.auth.models.User'
    """
    date = models.TextField()
    time = models.TextField()
    input_str = models.TextField()
    cnt_words = models.IntegerField()
    cnt_symbols = models.IntegerField()
    client = models.ForeignKey(to=User, on_delete=models.CASCADE)


class NewYearGifts(models.Model):
    """
    :param date: дата
    :param gifts_from_DedMoroz: кол-во подарков, доставленных Дедом Морозом
    :param gifts_from_DedMoroz: кол-во подарков, доставленных эльфами
    :param gifts_from_DedMoroz: кол-во подарков, доставленных Почтой России
    """
    date = models.TextField()
    gifts_from_DedMoroz = models.IntegerField()
    gifts_from_elfs = models.IntegerField()
    gifts_from_PR = models.IntegerField()
