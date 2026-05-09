from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        #NORMAL MODE
    path('', views.home, name='home'),


    #Full Maintaniance activation Mode
    # path('', views.maintenance, name='maintenance'),

    path('semesters/<int:branch_id>/', views.semesters, name='semesters'),

    path('subjects/<int:sem_id>/<int:branch_id>/', views.subjects, name='subjects'),

    path('categories/<int:subject_id>/', views.categories_view, name='categories'),

    path('files/<int:subject_id>/<int:category_id>/', views.files, name='files'),

    path('view/<int:file_id>/',views.view_file,name='view_file'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)