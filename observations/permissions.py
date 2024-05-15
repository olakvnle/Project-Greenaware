# from rest_framework.permissions import BasePermission
# from .models import ApiKeys
#
#
# class HasAPIKey(BasePermission):
#     """
#     Custom permission to allow users with an API key to access observations without authentication.
#     """
#
#     def has_permission(self, request, view):
#         # Check if the user has an API key
#         api_key = request.META.get('api_key')  # Assuming you pass the API key in the request headers
#         if api_key:
#             # Check if the API key exists in the APIKey table
#             try:
#                 api_key_instance = ApiKeys.objects.get(api_key=api_key)
#                 # If the API key exists, allow access without authentication
#                 print(api_key_instance)
#                 return True
#             except ApiKeys.DoesNotExist:
#                 # If the API key does not exist, deny access
#                 return False
#         else:
#             # If no API key is provided, deny access
#             return False
