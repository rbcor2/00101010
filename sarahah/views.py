from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

from .forms import MessageForm

def sarahah_view(request):
    if request.method == "POST":
        form = MessageForm(request.POST or None)
        sent = False
        print('post requests geted')
        if form.is_valid():
            print('form valid')
            subject = "SAHARAH MESSAGE FROM WEBSITE"
            body  = form.cleaned_data.get('body','no message body found')
            sender = 'o1935926686@gmail.com'
            recevers = ['rb60041@gmail.com']

            sent = send_mail(subject, body, sender, recevers, fail_silently=False)
           
            if sent:
                sent = True
                print('mail sented')
        print('render template')
        return render(request, 'sarahah/home.html', {'sent':sent, 'form':form})

    else:
        form = MessageForm()
    return render(request, 'sarahah/home.html', {'form':form})
