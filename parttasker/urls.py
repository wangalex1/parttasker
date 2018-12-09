
from django.conf.urls import url,include
from django.contrib import admin
from parttaskerapp import views,apis
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^company/sign-in/$', auth_views.login,
        {'template_name': 'company/sign_in.html'},
        name = 'company-sign-in'),
    url(r'^company/sign-out', auth_views.logout,
        {'next_page': '/'},
        name = 'company-sign-out'),
    url(r'^company/sign-up', views.company_sign_up,
        name = 'company-sign-up'),
    url(r'^company/$', views.company_home, name = 'company-home'),
    # Sign In/ Sign Up/ Sign Out
    url(r'^api/social/', include('rest_framework_social_oauth2.urls')),
    # /convert-token (sign in/ sign up)
    # /revoke-token (sign out)
    #apis
    # url(r'^api/client/parttasker/$',apis.client_get_parttasker),
    # url(r'^api/client/parts/(?P<company_id>\d+)/$',apis.client_get_parts),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
