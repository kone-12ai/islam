# blog.views.py

from django.views import generic

from blog import mixins
from blog.models import Post


class HomeView(generic.TemplateView):
    template_name = 'index.html'
    extra_context = {'page_title': 'Accueil'}

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.post_recently()
        context['posts_all'] = Post.objects.all()
        return context


home_view = HomeView.as_view()


class PostSportListView(generic.ListView, mixins.CategoryListMixins):
    paginate_by = 100
    context_object_name = 'post_list'

    def get_queryset(self):
        post_sport_list = self.posts_sports()
        print(post_sport_list)
        return post_sport_list


post_sport_view = PostSportListView.as_view(
    template_name='posts/post_list.html', extra_context={'page_title': 'sport'}
)



class PostReligionListeView(generic.ListView, mixins.CategoryListMixins):
    paginate_by =100
    context_object_name = 'post_list'

    def get_queryset(self):
        post_religion_list = self.posts_religion()
        print(post_religion_list)
        return post_religion_list

post_religion_view = PostReligionListeView.as_view(
    template_name = 'posts/post_list.html', extra_context={'page_title': 'religion'}
    )



class PostPolitiqueListeView(generic.ListView, mixins.CategoryListMixins):
    paginate_by =100
    context_object_name = 'post_list'

    def get_queryset(self):
        post_politique_list = self.posts_politique()
        print(post_politique_list)
        return post_politique_list

post_politique_view = PostPolitiqueListeView.as_view(
    template_name = 'posts/post_list.html', extra_context={'page_title': 'politique'}
    )




class PostInternationalListeView(generic.ListView, mixins.CategoryListMixins):
    paginate_by =100
    context_object_name = 'post_list'

    def get_queryset(self):
        post_international_list = self.posts_international()
        print(post_international_list)
        return post_international_list

post_international_view = PostInternationalListeView.as_view(
    template_name = 'posts/post_list.html', extra_context={'page_title': 'international'}
    )

class PostCommuniqueListView(generic.ListView, mixins.CategoryListMixins):
    paginate_by = 100
    context_object_name = 'post_list'

    def get_queryset(self):
        post_communique_list = self.posts_communique()
        print(post_communique_list)
        return post_communique_list


post_communique_view = PostCommuniqueListView.as_view(
    template_name='posts/post_list.html', extra_context={'page_title': 'communique'}
)

class PostSocieteListView(generic.ListView, mixins.CategoryListMixins):
    paginate_by = 100
    context_object_name = 'post_list'

    def get_queryset(self):
        post_societe_list = self.posts_societe()
        print(post_societe_list)
        return post_societe_list


post_societe_view = PostSocieteListView.as_view(
    template_name='posts/post_list.html', extra_context={'page_title': 'societe'}
)

class PostBKNewsListView(generic.ListView, mixins.CategoryListMixins):
    paginate_by = 100
    context_object_name = 'post_list'

    def get_queryset(self):
        post_bknews_list = self.posts_bknews()
        print(post_bknews_list)
        return post_bknews_list


post_bknews_view = PostBKNewsListView.as_view(
    template_name='posts/post_list.html', extra_context={'page_title': 'Bouaké News'}
)


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_post_title = self.object.post_title
        context['page_title'] = '{0}'.format(str(get_post_title))
        return context


post_detail_view = PostDetailView.as_view(template_name='posts/post_detail.html')
