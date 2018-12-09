# from rest_framework import serializers
# from parttaskerapp.models import Company
#
# class CompanyParttaskerSerializer(serializers.ModelSerializer):
#     logo = serializers.SerializerMethodField()
#     def get_logo(self,parttasker):
#         request = self.context.get('request')
#         logo_url = parttasker.logo.url
#         return request.build_absolute_uri(logo_url)
#     class Meta:
#         model = Company
#         fields = ('id','name','phone','address','logo')
