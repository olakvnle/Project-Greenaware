# from rest_framework.authentication import BaseAuthentication
# from rest_framework.exceptions import AuthenticationFailed
# from .models import ApiKeys
#
#
# class APIKeyAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         api_key = request.META.get('api_key', None)
#         if not api_key:
#             return None
#
#         try:
#             api_key_instance = ApiKeys.objects.get(api_key=api_key)
#             return (api_key_instance, None)
#         except ApiKeys.DoesNotExist:
#             raise AuthenticationFailed('Invalid API key')
#
#
