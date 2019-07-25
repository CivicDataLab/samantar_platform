# add to the top
from .forms import FormContact
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings


#
def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormContact(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = "{0} has sent you a new message:\n\n{1}".format(sender, form.cleaned_data['message'])
           
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['shreyaagrawal0809@gmail.com']
        if cc_myself:
            recipients.append(sender)

        send_mail(subject, message, sender, recipients)
        return redirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FormContact()


    return render(request, 'contact.html', {'form': form})

