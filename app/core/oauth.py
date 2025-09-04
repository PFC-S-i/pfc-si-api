#Fluxo Google OAuth ( a fazer )
#Só será usado se GOOGLE_CLIENT_ID/SECRET/REDIRECT_URI estiverem no .env.


from authlib.integrations.starlette_client import OAuth
from app.core.config import settings

oauth = OAuth()
if settings.GOOGLE_CLIENT_ID and settings.GOOGLE_CLIENT_SECRET:
    oauth.register(
        name="google",
        client_id=settings.GOOGLE_CLIENT_ID,
        client_secret=settings.GOOGLE_CLIENT_SECRET,
        server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
        client_kwargs={"scope": "openid email profile"},
    )
