from django.conf.urls import url, include
from django.contrib import admin
# remove auth_views
from django.contrib.auth import views as auth_views
from participants.views import add, ECUserFormView


urlpatterns = [
    url(r'^$', add, name='add_data'),
    url(r'^participants/', include('participants.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', ECUserFormView.as_view()),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
]
