from django.contrib import admin


from webapp.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'date', 'details']
    list_filter = ['status']
    search_fields = ['status']
    fields = ['description', 'status', 'date', 'details']


admin.site.register(Todo, TodoAdmin)


# Register your models here.
