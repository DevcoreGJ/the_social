from django.contrib import admin
from .models import Venue
from .models import MyClubUser
from .models import Event

# Register your models here.

# Commenting out venue as adding a
# more comprehensive feature that encapsulates

#admin.site.register(Venue)

admin.site.register(MyClubUser)
admin.site.register(Event)

# Better practice than the above original
@admin.register(Venue)

# Class containing venue admin deatails
class VenueAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'phone')

# Sets the ordering of venues as alphabetical
	oredering = ('name',)

# Sets the ordering of venues as reverse alphabetical
	# ordering = ('-name')

# Creates criteria for searching Table
	search_fields = ('name', 'address')

