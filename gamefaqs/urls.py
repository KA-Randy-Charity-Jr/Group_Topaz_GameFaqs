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
from django.urls import path, re_path
from . import settings
from django.views.static import serve
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from user_faq import views as userviews
from authentication.views import login_view, logout_view
from gamefaq_app import views as gamefaqviews
from console_app import views as consoleviews
from game_app import views as gameviews
from news_app import views as newsviews
from reviews_app import views as reviewsviews

urlpatterns = [
    path('', gamefaqviews.indexview, name='home'),
    path('user_profile_view/<int:user_id>/edit/',
         userviews.edit_user_profile_view.as_view()),
    path('user_profile_view/<int:user_id>/',
         userviews.user_profile_view, name='user_profile'),
    path('login_view/', login_view, name='login'),
    path('signup_view/', userviews.signup_view.as_view()),
    path('logout_view/', logout_view, name='logout'),
    path('admin/', admin.site.urls),
    path('gamefaq/<int:gamefaqid>/', gamefaqviews.gamefaqview, name="gamefaq"),
    path('game/<int:gameid>/', gameviews.gamesview, name="game"),
    path('newgamefaq/<int:gameid>/',
         gamefaqviews.newgamefaqview, name="newgamefaq"),
    path('playstation/', consoleviews.PlaystationView, name="playstation"),
    path('xbox/', consoleviews.XboxView, name="xbox"),
    path('nintendo/', consoleviews.NintendoView, name="nintendo"),
    path('pc/', consoleviews.PcView, name="pc"),
    path("console/<int:console_id>/", consoleviews.consoleview, name="console"),
    path("postnews/<int:gameid>/", newsviews.Newspostform.as_view(), name="newpost"),
    path('newspost/<int:newsid>/', newsviews.NewpostView, name="newspostview"),
    path('search/', gamefaqviews.SearchResultsView.as_view(), name='search_results'),
    path('faqsearch/', gamefaqviews.FaqResultsView.as_view(), name='search_result'),
    path('<int:faqid>/reviews/', reviewsviews.ReviewsView, name="reviews"),
    path('newreview/<int:faqid>/',
         reviewsviews.CreateReview.as_view(), name="reviewform"),
    path('follow/<int:userid>/', userviews.FollowView.as_view(), name="followuser"),
    path('unfollow/<int:userid>/',
         userviews.UnFollowView.as_view(), name="unfollowuser"),
    path('favorite/<int:gameid>/',
         userviews.FavoriteView.as_view(), name="favoritegame"),
    path('unfavorite/<int:gameid>/',
         userviews.UnFavoriteView.as_view(), name="unfavortiegame"),
    path('comment/<int:userid>/', userviews.CommentView.as_view(), name="comments"),
    path('consolefav/<int:consoleid>/',
         userviews.ConsoleFavView.as_view(), name="consolefav"),
    path('consoleunfav/<int:consoleid>/',
         userviews.ConsoleUnfavView.as_view(), name="consoleunfav"),
    path('editgamefaq/<int:faqid>/',
         gamefaqviews.Edit_GamefaqView.as_view(), name="editgamefaq"),
    path('editreview/<int:reviewid>/',
         reviewsviews.Edit_ReviewView.as_view(), name="editreview"),
    path('editnews/<int:newsid>/',
         newsviews.Edit_NewsView.as_view(), name="editnews"),
    path('editcomment/<int:commentid>/',
         userviews.edit_user_comment_view.as_view(), name="editcomment"),
    path('<pk>/deletecomment/',
         userviews.DeleteComment.as_view(), name="deletecomment"),
    path('<pk>/deletereview/',
         reviewsviews.DeleteReview.as_view(), name="deletereview"),
    path('<pk>/deletenews/',
         newsviews.DeleteNews.as_view(), name="deletenews"),
    path('<pk>/deletefaq/',
         gamefaqviews.Deletefaq.as_view(), name="deletefaq"),
    path('activityfeed/', gamefaqviews.ActivityFeed.as_view(), name="activityfeed"),
    path('upload/<slug:pk>/', userviews.Upload_photo_view.as_view(),
         name='Photo_upload'),
]

handler404 = 'gamefaq_app.views.handler404'
handler500 = 'gamefaq_app.views.handler500'

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^gallery/(?P<path>.*)$', serve,
                        {'document_root': settings.MEDIA_ROOT, }), ]
