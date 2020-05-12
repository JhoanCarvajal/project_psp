from django.urls import path
from .views import HomePageView, SamplePageView, ProgramListView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
    path('list-programs/', ProgramListView.as_view(), name="list-programs-core"),

]