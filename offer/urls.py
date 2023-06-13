from django.urls import path
from offer.views import offer_list, OfferListView, OfferDetailsView,\
    OfferCreateView, OfferUpdateView, OfferDeleteView


urlpatterns = [
    path("", OfferListView.as_view(), name="offer-list"),
    path("<int:pk>/", OfferDetailsView.as_view(), name="offer-details"),
    path("update/<int:pk>/", OfferUpdateView.as_view(), name="offer-update"),
    path("delete/<int:pk>/", OfferDeleteView.as_view(), name="offer-delete"),
    path("create/", OfferCreateView.as_view(), name="offer-create"),
]
