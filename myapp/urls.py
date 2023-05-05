from django.urls import path
from . import views
from django.contrib.auth.views import (
  LogoutView, 
  PasswordResetView, 
  PasswordResetDoneView, 
  PasswordResetConfirmView,
  PasswordResetCompleteView, 
)
from .forms import EmailValidationOnForgotPassword, ReSetPasswordForm

urlpatterns = [
  # Website related urls
  path('',views.Home.as_view(), name="home"),
  path('docs/', views.Docs.as_view(), name="docs"),

  path('activate/<uidb64>/<token>', views.activate, name='activate'),

  path('accounts/login/', views.MyLoginView.as_view(redirect_authenticated_user=True),name='login'),
  path('logout/', LogoutView.as_view(next_page='home'),name='logout'),
  path('register/', views.register ,name='register'),

  path('password-reset/', PasswordResetView.as_view(form_class=EmailValidationOnForgotPassword,template_name='myapp/password_reset.html'),name='password-reset'),
  path('password-reset/done/', PasswordResetDoneView.as_view(template_name='myapp/password_reset_done.html'),name='password_reset_done'),
  path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='myapp/password_reset_confirm.html', form_class=ReSetPasswordForm),name='password_reset_confirm'),
  path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='myapp/password_reset_complete.html'), name='password_reset_complete'),

  path('accounts/profile/', views.ProfileView.as_view(), name="profile"),
  path('edit-profile/', views.EditProfileView.as_view(), name="edit_profile"),
  path('jwt-docs/', views.JWTDocs.as_view(), name="jwt_docs"),
]
