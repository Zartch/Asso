from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from social.views import *

urlpatterns = [
    url(r'^', login_required(nou_consum) ,name='nou_consum'),
]
