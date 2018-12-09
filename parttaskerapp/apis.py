# from django.http import JsonResponse
#
# from .models import Company
#
# from parttaskerapp.serializers import CompanyParttaskerSerializer
#
# def client_get_parttasker(request):
#     parttasker = CompanyParttaskerSerializer(
#     Company.objects.all().order_by('-id'),
#     many=True,
#     context={'request':request}
#     ).data
#     return JsonResponse({'parttasker':parttasker})
#
# def client_get_parts(request):
#     return JsonResponse({})
