from django.contrib import admin, messages
from django.utils.translation import ngettext

from .form import SmartphoneForm
from .models import Smartphone, Chapter, Book


@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ['model', 'ram', 'height', 'price', 'status']
    search_fields = ['model']
    list_filter = ['height']
    ordering = ['-price', 'model']
    form = SmartphoneForm


    fieldsets = (
        ('Basic', {
            'fields': ('model', 'ram')
        }),
        ('Cost', {
            'fields': ('height', 'price', 'status')
        })
    )

    def marcar_agotado(self, request, queryset):
        actualizados = queryset.update(status='agotado')
        self.message_user(
            request,
            ngettext(
                '%d smartphone was updated',
                '%d smartphones where updated',
                actualizados,
            ) % actualizados,
            messages.SUCCESS
        )

    actions=[marcar_agotado]


class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 2


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    inlines = [ChapterInline]
