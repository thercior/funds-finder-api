from django.contrib import admin
from api.models import FundsEstate


@admin.register(FundsEstate)
class FundsEstateAdmin(admin.ModelAdmin):
    
    list_display = ('code', 'sector', 'dividend_yield_avg_12m', 'amount_assets', 'id')

# Register your models here.
