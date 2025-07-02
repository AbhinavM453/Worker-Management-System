"""workermngt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from workerapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginadd),
    path('changepasswdadmin',views.changepasswdadmin),
    path('login_post',views.login_post),
    path('changepsw_posta', views.changepsw_posta),
    path('changepasswdworker',views.changepasswdworker),
    path('changepsw_postw',views.changepsw_postw),
    path('changepasswduser',views.changepasswduser),
    path('changepsw_postu',views.changepsw_postu),
    path('adminhome',views.adminhome),#admin
    path('userhome',views.userhome),#user
    path('workerhome',views.workerhome),#worker
    path('registeruser',views.registeruser),#user
    path('vuser',views.vuser),#admin
    path('registerworker',views.registerworker),#worker
    path('vworker',views.vworker),#admin
    path('vcomplaints',views.vcomplaints),#admin
    path('viewfdbackuser',views.viewfdbackuser),#admin
    path('user_post',views.user_post),#user
    path('worker_post',views.worker_post),#worker
    path('sndfeedbackuser',views.sndfeedbackuser),#worker,user
    path('fd_postuser',views.fd_postuser),#worker,user
    path('sndcomplaints',views.sndcomplaints),#user
    path('sndcom_post',views.sndcom_post),#user
    path('sndreplay/<id>',views.sndreplay),#admin
    path('sndreplay_post/<id>',views.sndreplay_post),#admin
    path('worker_approve/<id>',views.worker_approve),#admin
    path('worker_reject/<id>',views.worker_reject),#admin
    path('verified_worker',views.verified_worker),#admin
    path('sndfeedbackworker',views.sndfeedbackworker),#worker
    path('fd_postworker',views.fd_postworker),#worker
    path('viewfdworker',views.viewfdworker),#worker
    path('viewworker',views.viewworker),#worker
    path('editworker/<id>',views.editworker),#worker,admin
    path('edit_wpost/<id>',views.edit_wpost),#worker
    path('delete_worker/<id>',views.delete_worker),#admin
    path('service_mngt',views.service_mngt),#worker
    path('smngt_post',views.smngt_post),#worker
    path('viewservice',views.viewservice),#user
    path('viewuser',views.viewuser),#user
    path('edituser/<id>',views.edituser),#user,admin
    path('edit_upost/<id>',views.edit_upost),#user,admin
    path('delete_user/<id>',views.delete_user),#admin
    path('sndrequest',views.sndrequest),#user
    path('req_post',views.req_post),#user
    path('editservice/<id>',views.editservice),#worker
    path('editservice_post',views.editservice_post),#worker
     path('viewservice',views.viewservice),
    path('viewservicereq',views.viewservicereq),#worker
    path('sndratings',views.sndratings),#user
    path('rating_post',views.rating_post),#user
    path('viewratings',views.viewratings),#worker
    path('viewreplay',views.viewreplay),#user
    path('approvereq/<id>',views.approvereq),#worker
    path('rejectrq/<id>',views.rejectrq),#worker
    path('viewverifiedreq',views.viewverifiedreq),#Worker
    path('viewserviceuser',views.viewserviceuser),
    path('logout',views.logout),
    path('verified_workeruser',views.verified_workeruser),
    path('forgetpassword',views.forgetpassword),
    path('forgotpassword_post',views.forgotpassword_post),





]
