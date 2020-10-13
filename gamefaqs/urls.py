"""gamefaqs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from user_faq import views
from authentication.views import login_view, logout_view
from gamefaq_app import views as gamefaqviews
from console_app import views as consoleviews
from game_app import views as gameviews
from news_app import views as newsviews
from reviews_app import views as reviewsviews

urlpatterns = [
    path('', views.index, name='home'),
    path('user_profile_view/<int:user_id>/edit/',views.edit_user_profile_view.as_view()),
    path('user_profile_view/<int:user_id>/', views.user_profile_view, name='user_profile'),
    path('login_view/', login_view, name='login'),
    path('signup_view/', views.signup_view.as_view()),
    path('logout_view/', logout_view, name='logout'),
    path('admin/', admin.site.urls),
    path('gamefaq/<int:gamefaqid>/',gamefaqviews.gamefaqview,name="gamefaq"),
    path('game/<int:gameid>/',gameviews.gamesview,name="game"),
    path('newgamefaq/', gamefaqviews.newgamefaqview, name="newgamefaq"),
    path('playstation/', consoleviews.PlaystationView, name="playstation"),
    path('xbox/', consoleviews.XboxView, name="xbox"),
    path('nintendo/', consoleviews.NintendoView, name="nintendo"),
    path('pc/', consoleviews.PcView, name="pc"),
    path("console/<int:console_id>/", consoleviews.consoleview, name="console"),
    path("postnews/", newsviews.Newspostform.as_view(), name="newpost"),
    path('newspost/<int:newsid>/', newsviews.NewpostView, name="newspostview"),
    path('search/', gamefaqviews.SearchResultsView.as_view(), name='search_results'),
    path('<int:faqid>/reviews/', reviewsviews.ReviewsView, name="reviews"),
    path('newreview/<int:faqid>/',reviewsviews.CreateReview.as_view(),name="reviewform")
]
