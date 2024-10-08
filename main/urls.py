from django.urls import path
from main.views import show_main, create_shoes_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, add_shoes_entry_ajax
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_shoes
from main.views import delete_shoes

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-shoes-entry/', create_shoes_entry, name='create_shoes_entry'),
    path('shop/', show_main, name='shop'),  # Mengarahkan ke show_main
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-shoes/<uuid:id>', edit_shoes, name='edit_shoes'),
    path('delete/<uuid:id>', delete_shoes, name='delete_shoes'),
    path('create-shoes-entry-ajax', add_shoes_entry_ajax, name='add_shoes_entry_ajax'),
]