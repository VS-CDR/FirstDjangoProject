from datetime import datetime
from random import randint

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from root.forms import SplitForm
from root.models import CalcHistory, StrHistory, NewYearGifts


def index(request):
    """
    Главная страница сайта

    :param request: объект с деталями запроса
    :type request: :class: 'django.http.HttpRequest'
    :return: html страница
    """
    context = {'class': "Занятие №12", 'theme': "Знакомство с Django", 'date': datetime.utcnow().strftime("%d.%m.%Y"),
               'pagename': 'Первый сайт'}

    return render(request, 'index.html', context)


def riddle(request):
    """
    Страница с загадкой

    :param request: объект с деталями запроса
    :type request: :class: 'django.http.HttpRequest'
    :return: html страница
    """
    rid = []
    with open("static/riddle.txt", 'r') as f:
        for line in f:
            rid.append(line)

    context = {'riddle': rid, 'pagename': 'Загадка'}

    return render(request, 'riddle.html', context)


def answer(request):
    """
    Страница с ответом на загадку

    :param request: объект с деталями запроса
    :type request: :class: 'django.http.HttpRequest'
    :return: html страница
    """
    context = {'ans': "компьютер", 'pagename': 'Ответ на загадку'}

    return render(request, 'answer.html', context)


def multiply(request):
    """
    Страница с таблицей умножения определенного числа на 1...9

    :param request: запрос методом GET (?arg=x, где x задаваемое значение)
    :type request: :class: 'django.http.HttpRequest'
    :return: html страница
    """
    mul_table = []
    try:
        arg = int(request.GET.get('arg'))
        for mul in range(1, 10):
            mul_table.append(f'{mul} * {arg} = {mul * arg}')
    except TypeError:
        mul_table.clear()
    context = {'mul_table': mul_table, 'pagename': 'Таблица выражения'}
    return render(request, 'multiply.html', context)


def expression(request):
    """
    Страница с генерируемым алгебраическим выражением

    :param request: объект с деталями запроса
    :type request: :class: 'django.http.HttpRequest'
    :return: html страница
    """
    cnt_exp = str()
    n = randint(2, 4)
    for i in range(n):
        cnt_exp += str(randint(10, 99))
        if i + 1 != n:
            cnt_exp += ' '
            if randint(0, 1):
                cnt_exp += '+'
            else:
                cnt_exp += '-'
            cnt_exp += ' '

    expr = cnt_exp
    context = {'cnt_exp': expr, 'equal': '='}

    cnt_exp = cnt_exp.split()
    cnt_res = int(cnt_exp[0])
    op = ''
    for i in range(1, len(cnt_exp)):
        if not cnt_exp[i].isdigit():
            if cnt_exp[i] == '+':
                op = '+'
            elif cnt_exp[i] == '-':
                op = '-'
        else:
            if op == '+':
                cnt_res += int(cnt_exp[i])
            elif op == '-':
                cnt_res -= int(cnt_exp[i])

    context['cnt_res'] = cnt_res
    context['pagename'] = 'Случайное алгебраическое выражение'

    record = CalcHistory(
        expression=expr,
        res=cnt_res
    )
    record.save()

    return render(request, 'expression.html', context)


def history(request):
    """
    Страница с историей вычислений выражений

    :param request: объект с деталями запроса
    :type request: :class: 'django.http.HttpRequest'
    :return: html страница
    """
    context = {'history': CalcHistory.objects.all(), 'pagename': 'История вычислений'}
    return render(request, 'history.html', context)


@login_required
def str2words(request):
    """
    Страница для обработки строк

    :param request: объект с деталями запроса
    :type request: :class: 'django.http.HttpRequest'
    :return: html страница
    """
    form = SplitForm(request.POST)
    context = {'form': form}

    if form.is_valid():
        string = form.cleaned_data['string']
        strings = string.split()
        nums, words = [], []

        for _str in strings:
            nums.append(_str) if _str.isdigit() else words.append(_str)

        context["nums"] = nums
        context["cnt_nums"] = len(nums)
        context["words"] = words
        context["cnt_words"] = len(words)
        context['pagename'] = 'Анализ строки'

        user = request.user
        if user.is_authenticated:
            record = StrHistory(
                date=datetime.utcnow().strftime("%Y.%m.%d"),
                time=datetime.utcnow().strftime("%H:%M:%S"),
                input_str=string,
                cnt_words=context["cnt_words"],
                cnt_symbols=len(string),
                client=user
            )
            record.save()

    return render(request, 'str2words.html', context)


@login_required
def str_history(request):
    """
    Страница с историей обработок строк

    :param request: объект с деталями запроса
    :type request: :class: 'django.http.HttpRequest'
    :return: html страница
    """
    context = {'history': StrHistory.objects.filter(client_id=request.user), 'pagename': 'История анализа строк'}
    return render(request, 'str_history.html', context)


def clicker(request):
    """
    Страница с новогодним кликером (пока что не полностью рабочая)

    :param request: объект с деталями запроса
    :type request: :class: 'django.http.HttpRequest'
    :return: html страница
    """
    context = {'pagename': 'Новогодний кликер'}
    # record = NewYearGifts(
    #    date=datetime.utcnow().strftime("%Y.%m.%d"),
    #    gifts_from_DedMoroz=,
    #    gifts_from_elfs=,
    #    gifts_from_PR=
    # )
    # record.save()

    return render(request, 'clicker.html', context)
