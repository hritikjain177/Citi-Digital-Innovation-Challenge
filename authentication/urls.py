from .views import  MutualFundsView,SipsView,StocksView,ChartsView, ContactsView, MapsView, RegistrationView, UsernameValidationView, EmailValidationView, LogoutView, VerificationView, LoginView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register', RegistrationView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('Maps', MapsView.as_view(), name="Maps"),
    path('sips',  SipsView.as_view(), name='sips'),
    path('mutualfunds',  MutualFundsView.as_view(), name='mutualfunds'),
    path('Charts',ChartsView.as_view() , name="Charts"),
    path('Contacts',ContactsView.as_view() , name="Contacts"),
    path('stocks',StocksView.as_view() , name="stocks"),
    
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),
         name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),
         name='validate_email'),
    path('activate/<uidb64>/<token>',
         VerificationView.as_view(), name='activate'),
]
