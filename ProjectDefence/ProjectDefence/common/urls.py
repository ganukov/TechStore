from ProjectDefence.common.views import HomePageView, AboutPageView, ContactUsPageView, ContactUsFormView
from django.urls import path

urlpatterns = (
    path('', HomePageView.as_view(), name='home'),
    path('about-us/', AboutPageView.as_view(), name='about-us'),
    path('contact-us/', ContactUsPageView.as_view(), name='contact-us'),
    path('contact-us/enquiry', ContactUsFormView.as_view(), name='enquiry'),
)
