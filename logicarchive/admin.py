from django.contrib import admin
from logicarchive.models import Post, Tag, Category, Field

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass 

class TagAdmin(admin.ModelAdmin):
    pass 

class PostAdmin(admin.ModelAdmin):
    pass 

class FieldAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Field, FieldAdmin)