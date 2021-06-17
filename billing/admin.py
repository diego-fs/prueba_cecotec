##Third party imports
from django.contrib import admin
##Local application imports
from .models import Bill, BillingBody
    
class BillingBodyInline(admin.TabularInline):
    model = BillingBody
    classes = ("grp-collapse grp-open")
    inline_classes = ("grp-collapse grp-open", )
    verbose_name = 'Artículo'

class BillAdmin(admin.ModelAdmin):
    list_display=('bill_id', 'bill_date', 'client')
    readonly_fields = ('bill_id', 'bill_date')
    inlines = [BillingBodyInline]

admin.site.register(Bill, BillAdmin)