# blog.mixins.py

from blog.models import Post


class CategoryListMixins:

    def posts_sports(self):
        post_sport_list = Post.objects.sports()
        return post_sport_list

    def posts_bknews(self):
        post_bknews_list = Post.objects.bknews()
        return post_bknews_list

    def posts_culture(self):
        post_culture_list = Post.objects.culture()
        return post_culture_list

    def posts_religion(self):
        post_culture_list = Post.objects.religion()
        return post_culture_list

    def posts_politique(self):
        post_politique_list = Post.objects.politique()
        return post_politique_list

    def posts_communique(self):
        post_communique_list = Post.objects.communique()
        return post_communique_list

    def posts_international(self):
        post_international_list = Post.objects.international()
        return post_international_list
