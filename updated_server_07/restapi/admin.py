# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import House
from models import mem_details
from models import imagetable
from models import videotable
from models import FarmTable
from models import farmpoints
from models import farmcroptable
from models import welltable
from models import wellinfo
from models import newfarmcroptable


# Register your models here.

admin.site.register(House)
admin.site.register(mem_details)
admin.site.register(imagetable)
admin.site.register(videotable)
admin.site.register(FarmTable)
admin.site.register(farmpoints)
admin.site.register(farmcroptable)
admin.site.register(welltable)
admin.site.register(wellinfo)
admin.site.register(newfarmcroptable)

