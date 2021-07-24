from django.contrib import admin
from .models import Home, About, Profile2, Category, Results, Skills, Portfolio, Store, Streamers, Tourn, News


# Home
admin.site.register(Home)


# About
admin.site.register(About)

# News 


class Profile2Inline(admin.TabularInline):
    model = Profile2
    extra = 1


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [
        Profile2Inline,
    ]


# Tournements
admin.site.register(Tourn)
# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]


# Portfolio
admin.site.register(Portfolio)
admin.site.register(Store)
admin.site.register(Streamers)
admin.site.register(Results)
