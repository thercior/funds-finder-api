from django.db import models
import uuid

# Create your models here.
class FundsEstate(models.Model):
    # Opções de setores para escolhar
    SECTOR_CHOICES = [
        ('bancos', 'Agências de Bancos'), ('educacional', 'Educação'), ('fiagro', 'Fiagro'),
        ('fundo_desenvolvimento', 'Fundo de Desenvolvimento'), ('hospitalar', 'Hospitalar'),
        ('hotel', 'Hotéis'), ('imoveis_logistica', 'Imóveis de Logística, Comercial ou Industrial'),
        ('imoveis_residenciais', 'Imóveis Residenciais'), ('lajes_corporativas', 'Lajes Corporativas'),
        ('shopping', 'Shopping'), ('papeis', 'Papéis'), ('varejo', 'Varejo'), ('outros', 'Outros')
    ]
    
    # Modelagem do banco
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, blank=True)
    code = models.CharField(max_length=8)
    sector = models.CharField(max_length=50, choices=SECTOR_CHOICES)
    dividend_yield_avg_12m = models.DecimalField(max_digits=5, decimal_places=2)
    vacancy_financial = models.DecimalField(max_digits=5, decimal_places=2)
    vacancy_physical  = models.DecimalField(max_digits=5, decimal_places=2)
    amount_assets = models.IntegerField(default=0)
    