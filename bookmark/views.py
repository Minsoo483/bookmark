from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from bookmark.models import Bookmark

# 북마크 목록
class BookmarkList(ListView):
    model = Bookmark

# 북마크 추가
class BookmarkCreate(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('bookmark:list')  # redirect와 같은 의미
    template_name_suffix = '_create'  # 템플릿 이름변경 bookmark_form->bookmark_create

# 북마크 상세보기
class BookmarkDetail(DetailView):
    model = Bookmark

# 북마크 수정하기
class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('bookmark:list')
    template_name_suffix = '_update'

# 북마크 삭제하기
class BookmarkDelete(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')