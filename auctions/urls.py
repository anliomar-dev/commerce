from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("add_to_watchlist/<int:listing_id>", views.add_to_watchlist, name="add_to_watchlist"),
    path("remove_to_watchlist/<int:listing_id>", views.remove_to_watchlist, name="remove_to_watchlist"),
    path("watchlist", views.user_watchlist, name="display_watchlist"),
    path("user_listings", views.user_listings, name="display_user_listings"),
    path("bid/<int:listing_id>", views.bid, name="bid"),
    path("close<int:listing_id>", views.close_auction, name="close_auction"),
    path("comments<int:listing_id>", views.comment, name="comment"),
    path("categories", views.all_categories, name="categories"),
    path("<str:category_name>", views.category, name="category"),
]
