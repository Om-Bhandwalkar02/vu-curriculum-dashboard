from .models import SiteSettings
from .models import NavigationItem


def site_settings(request):

    settings = SiteSettings.objects.first()

    navigation = NavigationItem.objects.filter(
        is_active=True
    )

    return {
        "site_settings": settings,
        "navigation_items": navigation
    }