from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ["id","sender","author","amount","sent_at"]

    search_fields = ["sender","sent_at"]

    date_hierarchy = "sent_at"

    list_display_links = ["id","sender","author","amount","sent_at"]

admin.site.register(Transaction, TransactionAdmin)