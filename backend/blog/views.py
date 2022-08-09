from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, ContactForm


# def lenta(request):
#     projects=Project.objects.all()
#     size = len(projects)-1
#     projects_number = []
#     for value in enumerate(projects,start=0):
#         projects_number.append(value)
#     return render(request, 'portfolio/home_test.html', {'projects':projects_number, 'size':size})

def all_blogs(request):
    # blogs=Blog.objects.all()
    blogs=Blog.objects.order_by('-date')[:3]


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
    return render(request, 'blog/blog.html',{'blogs':blogs,'form':form})

def detail(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)

    #Добавлено(09.08.2022)
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
    return render(request,'blog/detail.html',{'blog':blog,'form':form})