from django.conf.urls.defaults import *
from OTVA_server.cal.models import *

urlpatterns = patterns('OTVA_server.cal.views',
    (r"^month/(\d+)/(\d+)/(prev|next)/$", "month"),
    (r"^month/(\d+)/(\d+)/$", "month"),
    (r"^month$", "month"),
    (r"^day/(\d+)/(\d+)/(\d+)/$", "day"),
    (r"^settings/$", "settings"),
    (r"^(\d+)/$", "main"),
    (r"", "main"),
)
