from django.db import models
from django.contrib import admin
from django.utils.html import format_html

class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Отметьте если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time)
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')
    
    @admin.display(description='Дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color: grey; font-weight: bold;">Сегодня в {}</span>', updated_time)
        return self.updated_at.strftime('%d.%m.%Y в %H:%M:%S')
    
    @admin.display(description='Заголовок')
    def red_title(self):
            return format_html('<span style="color: red; font-weight: bold;">{}</span>', self.title)

    def __str__(self) -> str:
        return f"advertisements(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = "advertisements"

