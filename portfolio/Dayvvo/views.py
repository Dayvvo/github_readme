from django.shortcuts import render, redirect
from .forms import Message
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.forms.models import model_to_dict
from smtplib import SMTPException, SMTPServerDisconnected

# Create your views here.


def anything(request):
    if request.method == 'POST':
        form = Message(request.POST)
        if form.is_valid():
            subject = 'Project Message'
            arr = [i for i in form.cleaned_data.values()]
            joiner = '\n'.join(arr)
            form.save()
            try:
                send_mail(subject, joiner, 'dayvvowork@gmail.com', ['dyvvoo@gmail.com'], fail_silently=False)
                response = {'success': 'Email Sent Successfully'}
            except SMTPException:
                response = {'exception': 'Email not sent.Please check your network connection or try again'}
            return render(request, 'response.html', response)
        else:
            return redirect('/index/', {'form': Message})
    else:
        return render(request, 'index2.html', {'form': Message})




def contactView(request):
    if request.method == 'GET':
        form = Message()
    else:
        form = Message(request.POST)
        if form.is_valid():
            subject = 'Project Message'
            from_email = form.cleaned_data['dayvvowork@gmail.com']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/success')
    return render(request, "email.html", {'form': form})


