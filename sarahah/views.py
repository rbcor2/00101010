from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

from .forms import MessageForm

def sarahah_view(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        sent = False
        if form.is_valid():
            print('form valid')
            subject = "SAHARAH MESSAGE FROM WEBSITE"
            body  = form.cleaned_data.get('body','no message body found')
            sender = 'o1935926686@gmail.com'
            recevers = ['rb60041@gmail.com']
            sent = send_mail(subject, body, sender, recevers, fail_silently=False)
            if sent:
                sent = True
        return render(request, 'sarahah/home.html', {'sent':sent, 'form':form})

    else:
        form = MessageForm()
    return render(request, 'sarahah/home.html', {'form':form})
