from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

# Django Rest Framework
from rest_framework import routers
from screen.views import PlayersViewSet, TeamsViewSet, TrainerViewSet, LeagueViewSet

router = routers.DefaultRouter()
router.register(r'teams', TeamsViewSet)
router.register(r'trainers', TrainerViewSet)
router.register(r'leagues', LeagueViewSet)
router.register(r'players', PlayersViewSet)



urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'screen.views.home_view', name='home'),
    url(r'^players/', 'screen.views.players_view'),
    url(r'^teams/', 'screen.views.team_view'),
    url(r'^trainers/', 'screen.views.trainer_view'),
    url(r'^leguea/', 'screen.views.league_view'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/',include(router.urls)),
)
