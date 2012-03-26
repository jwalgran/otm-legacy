from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns(
    '',
    (r'^version$', version),
    (r'^plots$', get_plot_list),
    (r'^plots/(?P<plot_id>\d+)/tree/photo/(?P<photo_id>\d+)', get_tree_image),
    (r'^locations/(?P<lat>-{0,1}\d+(\.\d+){0,1}),(?P<lon>-{0,1}\d+(\.\d+){0,1})/plots', plots_closest_to_point),

    (r'^login/reset_password$', reset_password),
    (r'^login/create_user$', register),
    (r'^login$', verify_auth),

    (r'^user/(?P<user_id>\d+)/photo/(?P<title>.+)$', add_profile_photo),  

    (r'^tiles',  get_trees_in_tile),
)
