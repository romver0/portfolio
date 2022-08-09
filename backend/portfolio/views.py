from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.models import ContactForm
from .models import Project


def home(request):
    projects = Project.objects.all()
    size = len(projects) - 1
    projects_number = []
    for value in enumerate(projects, start=0):
        projects_number.append(value)

        # если метод GET, вернём форму
        if request.method == 'GET':
            form = ContactForm()
        # если метод POST, проверим форму и отправим письмо
        elif request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                # очещенные данные
                subject = form.cleaned_data['subject']
                # subject='Важно!'
                # message='Тебе понравилось моё портфолио,можешь написать мне на эту почту и мы с тобой всё обговорим!'
                from_email = form.cleaned_data['from_email']
                message = form.cleaned_data['message']

                try:
                    subject = subject
                    message = message
                    host_email = settings.EMAIL_HOST_USER

                    # send_mail(f'{subject}', f'{message}', settings.EMAIL_HOST_USER, [f'{from_email}'])
                    send_mail(f'{subject}', f'----- от {from_email} -----\n\n{message}', settings.EMAIL_HOST_USER,
                              [host_email, ])

                    subject = 'Важно'
                    message = 'Вы успешно отправили  письмо!'
                    send_mail(subject, f'----- от создателя блога -----\n\n{message}', settings.EMAIL_HOST_USER,
                              [from_email, ])
                # плохой ответ заголовка
                except BadHeaderError:
                    return HttpResponse('Ошибка в теме письма!Подсуетись,чтоб сделать нормально!')
                return redirect('success')
        else:
            return HttpResponse('Неверный запрос.')
    return render(request, 'portfolio/home.html', {'projects': projects_number, 'size': size, 'form': form})


def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку. Можете проверить свою почту!')


def description(request):
    projects = Project.objects.all()
    size = len(projects) - 1
    projects_number = []
    for value in enumerate(projects, start=0):
        projects_number.append(value)

        # если метод GET, вернём форму
        if request.method == 'GET':
            form = ContactForm()
        # если метод POST, проверим форму и отправим письмо
        elif request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                # очещенные данные
                subject = form.cleaned_data['subject']
                # subject='Важно!'
                # message='Тебе понравилось моё портфолио,можешь написать мне на эту почту и мы с тобой всё обговорим!'
                from_email = form.cleaned_data['from_email']
                message = form.cleaned_data['message']

                try:
                    subject = subject
                    message = message
                    host_email = settings.EMAIL_HOST_USER

                    # send_mail(f'{subject}', f'{message}', settings.EMAIL_HOST_USER, [f'{from_email}'])
                    send_mail(f'{subject}', f'----- от {from_email} -----\n\n{message}', settings.EMAIL_HOST_USER,
                              [host_email, ])

                    subject = 'Важно'
                    message = 'Вы успешно отправили  письмо!'
                    send_mail(subject, f'----- от создателя блога -----\n\n{message}', settings.EMAIL_HOST_USER,
                              [from_email, ])
                # плохой ответ заголовка
                except BadHeaderError:
                    return HttpResponse('Ошибка в теме письма!Подсуетись,чтоб сделать нормально!')
                return redirect('success')
        else:
            return HttpResponse('Неверный запрос.')
    return render(request, 'portfolio/description.html',{'form': form})

def handler_not_found(request,exception):
    return render(request,'portfolio/404.html',status=404)
# def home(request):
#     projects = Project.objects.all()
#     size=len(projects)
#     return render(request, 'portfolio/home_test.html', {'projects': projects,'size':size})
