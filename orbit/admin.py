from django.contrib import admin

from orbit.models import About, Category, Portfolio, HappyClients, Service, Education, WorkExperience, Contact

admin.site.register(About)
admin.site.register(Category)
admin.site.register(Portfolio)
admin.site.register(HappyClients)
admin.site.register(Service)
admin.site.register(Education)
admin.site.register(WorkExperience)

class ContactAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email","is_published")
    list_filter = ("is_published",)
    readonly_fields = ("create_at","update_at")
    search_fields = ("first_name","last_name")
admin.site.register(Contact,ContactAdmin)
