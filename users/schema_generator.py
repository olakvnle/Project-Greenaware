from rest_framework.schemas import AutoSchema


class CustomAutoSchema(AutoSchema):
    def get_link(self, path, method, base_url):
        link = super().get_link(self, path, method, base_url)

        excluded_endpoints = [
            '/users/reset_email/',
            '/users/reset_email_confirm/',
        ]
        if any(path.endswith(endpoint) for endpoint in excluded_endpoints):
            return None  # Exclude the endpoint from the schema

        return link
