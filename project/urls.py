
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .view import *

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',include('products.urls',namespace='product')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('accounts/', include('allauth.urls')),

    path('',home,name='home'),
    path('admin_management/',admin_management,name='admin_management'),
    path('admin_filter/<time>/<d>',admin_filter,name='admin_filter'),

    path('Order_Manage/',management,name='management'),
    path('<int:id>/',detail,name='detaill'),
    
    path('accounts/signup',signup,name='signup'),

    #Reset Password#
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'registration/password_reset_form.html'), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'registration/password_reset_done.html'), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/password_reset_confirm.html'), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'registration/password_reset_complete.html'), name ='password_reset_complete'),
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
