

from instagramm.models import *

posts = Post.objects.all()


posts_postman = Post.objects.filter(title='Postman')

posts_filter = posts_postman.filter(body='body')

posts_2023 = Post.objects.filter(date_posted__year=2023)


Post.objects.filter(date_posted__year=2023)

post_windows = Post.objects.filter(body__startswith='Windows').filter(date_posted__year=2022)

post_windows = Post.objects.filter(body__startswith='Windows', date_posted__year=2022)

posts = Post.objects.filter(date_posted__year=2023)

post = Post.objects.get(id=1)

post = Post.objects.get(date_updated__year=2023)

post = Post.objects.get(date_updated__year=2024)

post = Post.objects.filter(date_updated__year=2024).first()

post = Post.objects.exclude(date_updated__year=2023).filter(title__startswith='Linux')

posts = Post.objects.all().order_by('-title')

posts = Post.objects.all().values('title', 'body')

posts = Post.objects.all().values_list('title', 'body')

posts = Post.objects.all().values_list('title', flat=True)

posts = Post.objects.all().none()


comments = Comment.objects.all()

comments = Comment.objects.all().select_related('post', 'user', 'post__user')

posts = Post.objects.all()[0:2]

post = Post.objects.all().order_by('-id')[0]

posts = Post.objects.all().only('title', 'body')

#Filter Lookup Type

posts = Post.objects.filter(date_posted__lte='2022-12-31')

















