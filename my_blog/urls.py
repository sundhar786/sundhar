from django.urls import path
from . import views

urlpatterns=[
    path('',views.register_view,name='register_view'),
    path('login',views.login_view,name='login_view'),
    path('logout',views.logout_view,name='logout_views'),
    path('home',views.home_page,name='home_page'),
    path('post/<int:post_id>',views.post_detail,name='post_detail')

#     path('',views.home,name='home'),
#     path('p_result',views.p_result,name='submit'),
#     path('edit/<int:id>',views.edit,name='edit'),
#     path('update/<int:id>',views.update,name='update'),
#     path('delete/<int:id>',views.delete,name='delete')
]