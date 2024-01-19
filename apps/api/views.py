from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, response
from rest_framework.filters import SearchFilter, OrderingFilter
from api.serializers import FundsEstateSerializer
from api.models import FundsEstate

class FundsEstateViewSet(viewsets.ModelViewSet):
    queryset = FundsEstate.objects.all()
    serializer_class = FundsEstateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # Aplicação de filtros, buscas e ordenação de resultados
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] # processador dos filtros, buscas textuais e ordenação
    filterset_fields = ['code', 'sector'] # campos disponíveis para filtragem
    search_fields = ['code', 'sector'] # campos permitidos para busca textual
    ordering = ['dividend_yield_avg_12m'] # ordenação padrão
    ordering_fields = [
        'dividend_yield_avg_12m',
        'sector',
        'vacancy_financial',
        'vacancy_physical',
        'amount_assets',
    ]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        success_message = "FII excluído com sucesso!!!"
        return response.Response({"message": success_message})
