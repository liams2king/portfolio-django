from django.contrib import admin
from django.utils.html import format_html
from .models import Project
from .models import Message

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image_tag', 'url')  # colonnes visibles
    list_filter = ('category',)  # filtre à droite
    search_fields = ('title', 'description')  # barre recherche
    ordering = ('title',)  # tri
    list_editable = ('category',)  # modif rapide catégorie

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 60px; height:auto;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'

admin.site.register(Project, ProjectAdmin)
admin.site.register(Message)
