from django.urls import path
from . import views
urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("adduser", views.ReviewView.as_view()),
    path('details/<int:id>', views.details, name='details'),
    path('details/topup/<int:id>', views.topup, name='topup'),
    path('details/topup/updaterecord/<int:id>',
         views.updaterecord, name='updaterecord'),
    path('details/travel/<int:id>', views.travel, name='travel'),
    path('details/travel/updaterecord1/<int:id>', views.updaterecord1, name='updaterecord1'),
    path('details/<int:id>',
         views.updaterecord, name='details'),
    path('showuser', views.starting_page1, name='starting_page1'),
]
