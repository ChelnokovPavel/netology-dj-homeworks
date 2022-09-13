from django.contrib import admin


from .models import Article, Tag, Scopes


class ScopesInline(admin.TabularInline):
    model = Scopes


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopesInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Scopes)
class ScopesAdmin(admin.ModelAdmin):
    pass
