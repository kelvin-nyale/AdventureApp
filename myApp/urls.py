from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from myApp.views import index, update_user, add_activity, update_activity

urlpatterns = [
    # HOME PAGE URL
    path('', views.index, name='index'),
    
    path('register/', views.register, name='register'),
    
    path('login/', views.login, name='login'),
    
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    path('instructor_dashboard/', views.instructor_dashboard, name='instructor_dashboard'),
    
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),

    # path('logout/', views.logout, name='logout'),

    # USERS URLS
    path('users/', views.users, name='users'),
    path('adduser/', views.add_user, name='add_user'),
    path('updateuser/<int:pk>/', views.update_user, name='update_user'),
    path('deletuser/<int:pk>/', views.delete_user, name='delete_user'),

    #PACKAGES URLS
    path('packages/', views.packages, name='packages'),
    path('addpackage/', views.add_package, name='add_package'),
    path('updatepackage/<str:package_id>/', views.update_package, name='update_package'),
    path('deletepackage/<str:package_id>/', views.delete_package, name='delete_package'),

    #ACITVITIES URLS
    path('activities/', views.activities, name='activities'),
    path('addactivity/', views.add_activity, name='add_activity'),
    path('updateactivity/<int:id>/', views.update_activity, name='update_activity'),
    path('deleteactivity/<int:id>/', views.delete_activity, name='delete_activity'),

    #SERVICES URLS
    path('services/', views.services, name='services'),
    path('addservice/', views.add_service, name='add_service'),
    path('updateservice/<int:id>/', views.update_service, name='update_service'),
    path('deleteservice/<int:id>/', views.delete_service, name='delete_service'),

    path('rooms/', views.rooms_list, name='rooms'),
    path('rooms/add/', views.add_room, name='add_room'),
    path('rooms/update/<int:room_id>/', views.update_room, name='update_room'),
    path('rooms/delete/<int:room_id>/', views.delete_room, name='delete_room'),

    #BOOKINGS URLS
    # path('book/', views.book_activity, name='book_activity'),
    # path('my-bookings/', views.user_bookings, name='user_bookings'),
    # path('admin-bookings/', views.bookings, name='bookings'),
    # path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),


    # path(r'^static/(?P<path>.*)$', server, {'document_root': settings.STATIC_ROOT})

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #for image upload purposes