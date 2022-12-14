from ProjectDefence.products.views import add_product, DetailsProductView, LaptopsListView, PhonesListView, \
    ConsolesListView, LatestProductsView
from django.urls import path

urlpatterns = (
    path('add/', add_product, name='add-product'),
    path('details/<int:pk>/', DetailsProductView.as_view(), name='details-product'),
    path('laptops/', LaptopsListView.as_view(), name='laptops'),
    path('phones/', PhonesListView.as_view(), name='phones'),
    path('consoles/', ConsolesListView.as_view(), name='consoles'),
    path('latest_products/',LatestProductsView.as_view(),name='latest products'),
)
