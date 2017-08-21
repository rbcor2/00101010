from concurrent.futures import ThreadPoolExecutor

from django.shortcuts import render
from django.core.mail import send_mail

from .forms import MessageForm


executor = ThreadPoolExecutor(10)


def sarahah_view(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        sent = False
        if form.is_valid():

            kwargs = {}
            kwargs['subject'] = "SAHARAH MESSAGE FROM WEBSITE"
            kwargs['message']  = form.cleaned_data.get('body','no message body found')
            kwargs['from_email'] = 'o1935926686@gmail.com'
            kwargs['recipient_list'] = ['rb60041@gmail.com']
            kwargs['fail_silently'] = False

            sent = executor.submit(send_mail, **kwargs)

            if sent:
                sent=True
        return render(request, 'sarahah/home.html', {'sent':sent, 'form':form})

    else:
        form = MessageForm()
    return render(request, 'sarahah/home.html', {'form':form})
