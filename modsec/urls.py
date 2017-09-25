from django.conf.urls import url

from . import views


urlpatterns = [
    #Vista principal
    url(r'^$', views.index, name='index'),
    #Reglas
    url(r'^rules/', views.rules, name='rules'),
    #Registros
    url(r'^logs/', views.logs, name='logs'),
    #Mostrar una regla
    url(r'^showRule/(?P<rule_id>[0-9]+)/$', views.showRule, name='showRule'),
    #Mostrar un registro
    url(r'^showLog/(?P<log_id>[0-9]+)/$', views.showLog, name='showLog'),
    #Editar una regla
    url(r'^editRule/(?P<rule_id>[0-9]+)/$', views.editRule, name='editRule'),
    #Login
    url(r'^login/$', views.access, name='access'),
    
    url(r'logout/$', views.cerrar, name='cerrar'),
    ]