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
    #Logout
    url(r'logout/$', views.cerrar, name='cerrar'),
    #Login error
    url(r'notuser/$', views.notuser, name='notuser'),
    #Create rule 
    url(r'^createRule/$', views.createRule, name='createRule'), 
    #Conf
    url(r'^conf/$', views.paths, name='paths'), 
    #Anyadir directorio
    url(r'^addPath/$', views.addPath, name='addPath'), 
    
    url(r'^editPath/(?P<path_id>[0-9]+)/$', views.editPath, name='editPath'),
    
    url(r'^deletePath/(?P<path_id>[0-9]+)/$',views.deletePath, name='deletePath'), 
    
    url(r'^deleteRule/(?P<rule_id>[0-9]+)/$', views.deleteRule, name='deleteRule'),
    
    url(r'^editUserPermissions/(?P<user_id>[0-9]+)/$', views.showPerms, name='showPerms'),
    
    #url(r'^addPerm/*', views.addPerm, name='addPerm'),
    
     
     
    url(r'^editUserPermissions/(?P<user_id>[0-9]+)/(?P<permission_id>[0-9]+)', views.deletePerm, name='deletePerm'),
     
    url(r'^addPermissions/(?P<user_id>[0-9]+)/(?P<permission_id>[0-9]+)', views.addPerm, name='addPerm'),
    
    url(r'^logPID/(?P<log_id>[0-9]+)/$', views.showPIDLog, name='showPIDLog'),
    
    url(r'^logIP/(?P<log_id>[0-9]+)/$', views.showIP, name='showIP'),
    
    url(r'^logFile/(?P<log_id>[0-9]+)/$', views.showFile, name='showFile'),
    
    url(r'^logLine/(?P<log_id>[0-9]+)/$', views.showLine, name='showLine'),
    
    url(r'^logMsg/(?P<log_id>[0-9]+)/$', views.showMsg, name='showMsg'),
    
    url(r'^logMaturity/(?P<log_id>[0-9]+)/$', views.showMaturity, name='showMaturity'),
    
    url(r'^logAccuracy/(?P<log_id>[0-9]+)/$', views.showAccuracy, name='showAccuracy'),
    
    url(r'^logTag/(?P<log_id>[0-9]+)/$', views.showTag, name='showTag'),
    
    url(r'^logURI/(?P<log_id>[0-9]+)/$', views.showUri, name='showUri'),
    
     url(r'^delSuperUser/(?P<user_id>[0-9]+)/$', views.delSuperUser, name='delSuperUser'),
     
     url(r'^makeSuperUser/(?P<user_id>[0-9]+)/$', views.makeSuperUser, name='makeSuperUser'),
     
      url(r'^activate/(?P<user_id>[0-9]+)/$', views.habilitar, name='habilitar'),
     
     url(r'^deactivate/(?P<user_id>[0-9]+)/$', views.deshabilitar, name='deshabilitar'),
    ]