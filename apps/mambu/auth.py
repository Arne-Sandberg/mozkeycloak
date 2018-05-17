from mozilla_django_oidc.auth import OIDCAuthenticationBackend
try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

class NdeOIDC(OIDCAuthenticationBackend):
    def filter_users_by_claims(self, claim):
        username = claim.get('preferred_username')
        if not username:
            return self.UserModel.objects.none()

        return self.UserModel.objects.filter(username=username)

def provider_logout(request):
    from django.conf import settings
    logout_url = quote(settings.LOGOUT_REDIRECT_URL)
    redirect_url = settings.OIDC_BASE_URL + '/protocol/openid-connect/logout?redirect_uri=' + logout_url
    print(redirect_url)
    return redirect_url