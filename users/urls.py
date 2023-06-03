from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login_page, name='login'),
    path('user-profile/', user_profile, name='user_profile'),
    path('send-otp/', ssend_otp, name='ssend_otp'),
    path('admin-password/', admin_password, name='admin_password'),
    path('register-user/', resgister_user, name='register'),
    path('edit-user/', edit_user, name='edit_user'),
    path('enter-otp/', enter_otp, name='enter_otp'),
    path('logout/', logout_view, name='logout'),
    # path('update-user/<user_id>', update_user, name='update_user'),
    # path('list-user/', list_user, name='list_user'),
    # path('delete-user/<user_id>', delete_user, name='delete_user'),
    # path('logout/', logout_page, name='logout'),
]
