from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('raspisanie_new/', raspisanie_new, name='raspisanie'),
    path('raspisanie_post/', raspisanie_post, name='raspisanie_post'),
    path('raspisanie_post/monday', raspisanie_post_monday, name='raspisanie_post_monday'),
    path('raspisanie_post/tuesday', raspisanie_post_tuesday, name='raspisanie_post_tuesday'),
    path('raspisanie_post/wednesday', raspisanie_post_wednesday, name='raspisanie_post_wednesday'),
    path('raspisanie_post/thursday', raspisanie_post_thursday, name='raspisanie_post_thursday'),
    path('raspisanie_post/friday', raspisanie_post_friday, name='raspisanie_post_friday'),
    path('raspisanie_post/saturday', raspisanie_post_saturday, name='raspisanie_post_saturday'),
    path('raspisanie_calls/', raspisanie_calls, name='raspisanie_calls'),
    path('news/', newSchool, name='news'),
    path('about/', aboutSchool, name='about'),
    path('navi1/', navigation1, name='navigator1'),
    path('navi2/', navigation2, name='navigator2'),
    path('navi3/', navigation3, name='navigator3'),
    path('raspisanie_bus/', raspisanie_bus, name='raspisanie_bus'),
]
