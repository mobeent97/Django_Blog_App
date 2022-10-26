from django.contrib import admin
from django.urls import path, include 
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='RegisterPage'),
    path('profile/', user_views.profile, name='ProfilePage'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='LoginPage'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='LogoutPage'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='PasswordReset'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-_eset_done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='PasswordResetDone'),
    path('', include('blog.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

