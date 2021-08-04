from django.urls import path

from bookmark.views import BookmarkList, BookmarkCreate, BookmarkDetail, \
    BookmarkUpdate, BookmarkDelete

app_name = 'bookmark'

urlpatterns = [
    # 북마크 목록 - 127.0.0.1:8000/bookmark
    path('', BookmarkList.as_view(), name='list'),

    # 북마크 추가 - 127.0.0.1:8000/bookmark/create
    path('create/', BookmarkCreate.as_view(), name='create'),

    # 북마크 상세 보기 - 127.0.0.1:8000/bookmark/1
    path('<int:pk>/', BookmarkDetail.as_view(), name='detail'),

    # 북마크 수정 - 127.0.0.1:8000/bookmark/update/2
    path('update/<int:pk>/', BookmarkUpdate.as_view(), name='update'),

    # 북마크 삭제 - 127.0.0.1:8000/bookmark/delete/2
    path('delete/<int:pk>/', BookmarkDelete.as_view(), name='delete'),

]