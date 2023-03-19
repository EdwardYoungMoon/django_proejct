from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView

from blog.models import Post


class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2
    
class PostDV(DetailView):
    model = Post
    
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'
    
class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True # 해당 연도에 해당하는 객체의 리스트를 만들어서 템플릿에 넘겨준다 default = False
    
class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    
class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'
    
class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'