from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .forms import FormContact
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from cms.models.pluginmodel import CMSPlugin
from django.conf import settings

@plugin_pool.register_plugin
class ContactPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Contact Form")
    render_template = "contact_form_plugin.html"

    def render(self, context, instance, placeholder):
        request = context['request']
        if request.method == "POST":
            form = FormContact(request.POST)
            if form.is_valid():
            	subject = form.cleaned_data['subject']
            	sender = form.cleaned_data['sender']
            	message = "{0} has sent you a new message:\n\n{1}".format(sender, form.cleaned_data['message'])
            	cc_myself = form.cleaned_data['cc_myself']
            	recipients = ['shreyaagrawal0809@gmail.com']
            	if cc_myself:
            		recipients.append(sender)
            	send_mail(subject, message, sender, recipients)
       
            	context.update( {
                	'contact': instance,
                })
            return context
        else:
            form = FormContact()

            context.update({
            'contact': instance,
            'form': form,
            })
            return context