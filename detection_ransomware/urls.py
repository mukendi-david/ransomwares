from django.urls import path
from .views import (index, backup_data, user_login, user_logout, register,
                    Filter_Emails, Capture_Traffic
                    )

app_name = 'ransomwares'

urlpatterns = [
    path('', index, name='home'),
    path('backup_data/', backup_data, name='backup_data'),
    path('capture-traffic/', Capture_Traffic, name='Capture_Traffic'),
    path('filter-emails/', Filter_Emails, name='Filter_Emails'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # path('capture_traffic/', capture_traffic, name='capture_traffic'),
    # path('filter_emails/', filter_emails, name='filter_emails'),

]
