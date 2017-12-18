from django.conf.urls import url, include
from django.contrib import admin
# Add build_in auth views, like login ...
from django.contrib.auth import views as auth_views
from participants.forms import LoginForm
from participants.views import add, register_user, register_ok


urlpatterns = [
    url(r'^$', add, name='add_data'),
    url(r'^participants/', include('participants.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
    url(r'^register/$', register_user),
    url(r'^register_ok/$', register_ok),
]
