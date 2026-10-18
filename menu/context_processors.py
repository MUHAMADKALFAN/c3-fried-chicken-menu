from django.conf import settings
def cafe_settings(request):
    return {
        "CAFE_NAME": settings.CAFE_NAME,
        "CAFE_PHONE": settings.CAFE_PHONE,
        "WHATSAPP_NUMBER": settings.WHATSAPP_NUMBER,
        "CAFE_TAGLINE": settings.CAFE_TAGLINE,
    }
