from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^home$', views.home),
    url(r'^question/(?P<subtopic_id>\d+)$', views.question),
    url(r'^create_post$', views.create_post),
    url(r'^submit_post$', views.submit_post),
    url(r'^info/(?P<post_id>\d+)$', views.info),
    url(r'^addComment/(?P<post_id>\d+)$', views.addComment),
    url(r'^user_profile/(?P<user_id>\d+)$', views.user_profile),

]