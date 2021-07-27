from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template.defaultfilters import title
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.views import View

# from Tea_App.views import blog
from .models import Blog, SiteUtilities, AboutMe, ImageSlider, Subscribers, TypesOfTea
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# from .models import *

# Create your views here.

def home(request):
    #     ==================
    if request.method == "POST":
        subs_mail = request.POST.get('subs_mail')
        subs_first_name = request.POST.get('subs_first_name')

        subscribers = Subscribers.objects.all()
        match = False

        for subscribers in subscribers:
            if subs_mail == subscribers.subs_mail:
                match = True

        if match:
            messages.error(request, "You Are Already Subscribed!")
        else:
            subs_ins = Subscribers(subs_mail=subs_mail, subs_first_name=subs_first_name)
            subs_ins.save()
            messages.success(request, "Subscription Added Successfully!")

    image_slider = ImageSlider.objects.all()
    about_me = AboutMe.objects.all()
    site_utils = SiteUtilities.objects.all()
    types = TypesOfTea.objects.all()

    template_name = 'Tea_App/index.html'
    dict = {'about_me': about_me, 'img_slider': image_slider, 'site_utils': site_utils, 'types': types,
            }

    return render(request, template_name, context=dict)


def about(request):
    site_utils = SiteUtilities.objects.all()
    dict = {'site_utils': site_utils}
    return render(request, 'Tea_App/about.html', dict)


def blog_details(request, pk):
    blog1 = Blog.objects.order_by('-published_date')
    blog = Blog.objects.get(id=pk)
    dict = {'blog': blog, 'recent_blogs': blog1}
    return render(request, 'Tea_App/blog-details.html', dict)


def blog(request):
    blog = Blog.objects.order_by('-published_date')
    paginator = Paginator(blog, 6)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)
    dict = {'blog': paged_blogs, 'recent_blogs': blog}
    return render(request, 'Tea_App/blog.html', dict)


#
# def help(request):
#     site_utils = SiteUtilities.objects.all()
#     dict = {'site_utils' : site_utils}
#
#     if request.method == "POST":
#         help_name = request.POST.get('help_name')
#         help_email = request.POST.get('help_email')
#         help_subject = request.POST.get('help_subject')
#         help_message = request.POST.get('help_message')
#
#         print("\n===========\n", help_name,"\n=============\n") # for debugging
#
#         """ Contact / help mailing code
#             goes here. """
#
#         messages.success(request, "Your Message Was Sent To The Admin Successfully!")
#         message = "From: " + help_email + "n/"  " " + help_message
#
#         mail = EmailMessage(help_subject, message, to=[settings.EMAIL_HOST_USER])
#         mail.content_subtype = 'html'
#         mail.send()
#
#
#     return render(request, 'Tea_App/help.html', dict)


class Contact(TemplateView):
    template_name = './Tea_App/help.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        help_name = request.POST.get('help_name')
        help_email = request.POST.get('help_email')
        help_subject = request.POST.get('help_subject')
        help_message = request.POST.get('help_message')

        # message = "From: " + email + "/n"  " " + message
        message = "From: " + help_email + "/n"  " " + help_message
        mail = EmailMessage(help_subject, message, to=[settings.EMAIL_HOST_USER])
        mail.content_subtype = 'html'
        mail.send()
        return render(request, './Tea_App/help.html')


def tea_details(request, id):
    tea_type = TypesOfTea.objects.get(pk=id)
    data = {'tea_type': tea_type}
    return render(request, 'Tea_App/tea-details.html', data)


def types(request):
    site_utils = SiteUtilities.objects.all()
    types = TypesOfTea.objects.all()
    data = {
        'site_utils': site_utils,
        'types': types
    }
    return render(request, 'Tea_App/types.html', data)


# def search(request):
#     if request.method == "POST":
#         query_name = request.POST.get('name', None)
#         if query_name:
#             results = Blog.objects.filter(name__contains=query_name)
#             return render(request, 'Tea_App/search.html', {"results": results})
#
#     return render(request, 'Tea_App/search.html')


def search(request):
    search_query = ""
    if request.method == "POST":
        search_query = request.POST.get("search")
    types_teas=Blog.objects.filter(title__startswith=search_query)
    print(types_teas)

    dict = {'types_teas':types_teas}


    return render(request, 'Tea_App/search.html',context=dict)
