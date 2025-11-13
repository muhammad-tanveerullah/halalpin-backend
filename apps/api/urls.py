from rest_framework import routers
from apps.core.views import CityViewSet
from apps.users.views import UserViewSet
from apps.vendors.views import VendorViewSet
from apps.listings.views import ListingViewSet
from apps.reviews.views import ReviewViewSet

router = routers.DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'users', UserViewSet)
router.register(r'vendors', VendorViewSet)
router.register(r'listings', ListingViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = router.urls
