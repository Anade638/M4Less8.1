from django.contrib import admin
from.models import Advertisement

class AdvertismentAdmin(admin.ModelAdmin):
    list_display = ['id', 'red_title', 'description', 'price', 'created_date', 'updated_date','auction']
    list_filter = ['auction', 'created_at']
    actions = ['make_aution_as_false', 'make_aution_as_true']
    fieldsets = (
        ('Общее', {
            'fields' : ('title', 'description')
        }),
        ('Финансы', {
            'fields' : ('price', 'auction'),
            'classes' : ['collapse']
        }),

    )


    @admin.action(description='Убрать возможность торга')
    def make_aution_as_false(self, reqest, queryset):
        queryset.upadte(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_aution_as_true(self, reqest, queryset):
        queryset.upadte(auction=True)


admin.site.register(Advertisement, AdvertismentAdmin)
