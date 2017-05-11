from django.conf.urls import url
import views as account_views


urlpatterns = [
    url(r'^profile', account_views.profile.as_view(), name="profile"),
]
