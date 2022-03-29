from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.db.models import Q  # 帮助完成查询条件设置
from django.views.generic import ListView, DetailView
from django.shortcuts import HttpResponse
from .forms import CommentForm, addArticleForm, updateArticleForm
from .models import *


# class LoginRequiredMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.login_url = settings.LOGIN_URL
#         self.open_urls = [self.login_url] + getattr(settings, 'OPEN_URLS', [])
#
#     def __call__(self, request):
#         if not request.user.is_authenticated and request.path_info not in self.open_urls:
#            return redirect(self.login_url + '?next=' + request.path)
#         return self.get_response(request)


# class Index(ListView):
#     model = Article
#     template_name = 'index.html'
#     queryset = Article.objects.filter(status=2).order_by('-id')  # 获取到全部文章并按编号降序排列。
#     paginate_by = 3  # 设置分页时每页的文章数量

# 博客主页
def Index(request):
    if not request.session.get('is_login', None):
        return redirect('login')
    print(request.session.get('is_login'))
    if request.GET.get('order') == 'total_views':
        queryset = Article.objects.filter(status=3).order_by('-total_views')
        order = 'total_views'
    else:
        queryset = Article.objects.filter(status=3).order_by('-pub_time', '-id')
        order = 'normal'
    # queryset = Article.objects.filter(status=1).order_by('-id')
    # 每页显示 1 篇文章
    paginator = Paginator(queryset, 5)
    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给 articles
    articles = paginator.get_page(page)
    category = Category.objects.all().order_by("id")
    context = {
                'articles': articles,
                'category': category,
                'order': order
              }
    return render(request, 'index.html', context)
    # paginate_by = 3
    # return render(request, 'index.html', {'queryset': queryset, "category" : category})

# 文章分类
def CategoryList(request, pd):
    if not request.session.get('is_login', None):
        return redirect('login')
    if request.GET.get('order') == 'total_views':
        queryset = Article.objects.filter(category=pd, status=3).order_by('-total_views')
        order = 'total_views'
    else:
        queryset = Article.objects.filter(category=pd,status=3).order_by('-id')
        order = 'normal'
    # queryset = Article.objects.filter(category=pd, status=1).order_by('-id')
    paginator = Paginator(queryset, 5)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    category = Category.objects.all().order_by("id")
    category1 = Category.objects.get(id=pd)
    # article = Article.objects.filter(category=pd, status=2).first()
    # article.total_views += 1
    # article.save(update_fields=['total_views'])
    context = {
                'articles': articles,
                'category': category,
                'category1': category1,
                'order': order
              }
    return render(request, 'category.html', context)

# class CategoryList(ListView):
#     model = Article
#     template_name = 'category.html'
#     paginate_by = 5
#
#     def get_queryset(self):  # 定义通过分类查询的QuerySet
#         # 按参数传入的分类id进行查询并按文章编号降序排序
#         list = Article.objects.filter(category=self.kwargs['pd'])
#         if len(list) != '':
#             return Article.objects.filter(category=self.kwargs['pd']).order_by('-id')
#             # 查询标题或者内容包含关键字的数据对象
#         else:
#             return None
#
#     def get_context_data(self, **kwargs):  # 增加额外要传递给模板的数据
#         context = super().get_context_data(**kwargs)
#         try:
#             category = Category.objects.get(id=self.kwargs['pd'])
#             context['category'] = category.name  # 将分类对象的名称存入传递给模板的数据中
#             return context
#         except Category.DoesNotExist:
#             category = None
#             context['category'] = ''  # 将分类对象的名称存入传递给模板的数据中
#             return context


# def Category1(request):
#     CategoryLi = Category.objects.all()
#     return CategoryLi

# 文章搜索
def Search(request):
    key = request.GET.get('key')
    order = request.GET.get('order')
    category = Category.objects.all().order_by("id")
    if key:
        if order == 'total_views':
            if User.objects.filter(username=key):
                print(User.objects.get(username=key), 'aaa')
                article = Article.objects.filter(author_id=(User.objects.get(username=key)).id, status=3).order_by('-total_views')
            else:
                article = Article.objects.filter((Q(title__icontains=key) | Q(content__icontains=key)) & Q(status=3)).order_by('-total_views')
        else:
            if User.objects.filter(username=key):
                # print(User.objects.get(username=key), 'aaa')
                article = Article.objects.filter(author_id=(User.objects.get(username=key)).id, status=3)
            else:
                article = Article.objects.filter((Q(title__icontains=key) | Q(content__icontains=key)) & Q(status=3)).order_by('-id')
    else:
        key = ''
        if order == 'total_views':
            article = Article.objects.filter(status=3).order_by('-total_views')
        else:
            article = Article.objects.filter(status=3).order_by('-id')
    paginator = Paginator(article, 5)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {
                'articles': articles,
                'category': category,
                'key': key,
                'order': order
              }
    return render(request, 'search.html', context)


# class Search(ListView):
#     model = Article
#     template_name = 'search.html'
#     paginate_by = 3
#
#     def get_queryset(self):
#         key = self.request.GET['key']  # 获取查询关键字
#         if key:
#             author1 = User.objects.filter(username=key)
#             article = Article.objects.filter(author=author1.id)
#             article1 = Article.objects.filter(Q(title__icontains=key) | Q(content__icontains=key)).order_by('-id')
#             context = {
#                 'article': article,
#                 'article1': article1,
#             }
#             return context
#             # 查询标题或者内容包含关键字的数据对象
#         else:
#             return None
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['key'] = self.request.GET['key']  # 获取关键字存入传入模板的数据中
#         return context

# 文章详情
class ArticleDetail(DetailView):
    model = Article
    template_name = 'detail.html'

    def comment_sort(self, comments):  # 评论排序函数
        self.comment_list = []  # 排序后的评论列表
        self.top_level = []  # 存储顶级评论
        self.sub_level = {}  # 存储回复评论
        for comment in comments:  # 遍历所有评论
            if comment.reply == None:  # 如果没有回复目标
                self.top_level.append(comment)  # 存入顶级评论列表
            else:  # 否则
                self.sub_level.setdefault(comment.reply.id, []).append(comment)  # 以回复目标（父级评论）id为键存入字典
        for top_comment in self.top_level:  # 遍历顶级评论
            self.format_show(top_comment)  # 通过递归函数进行评论归类
        return self.comment_list  # 返回最终的评论列表

    def format_show(self, top_comment):  # 递归函数
        self.comment_list.append(top_comment)  # 将参数评论存入列表
        try:
            self.kids = self.sub_level[top_comment.id]  # 获取参数评论的所有回复评论
        except KeyError:  # 如果不存在回复评论
            pass  # 结束递归
        else:  # 否则
            for kid in self.kids:  # 遍历回复评论
                self.format_show(kid)  # 进行下一层递归

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(article=self.kwargs['pk'])  # 通过文章id查询评论内容
        article1 = Article.objects.get(id=self.kwargs['pk'])
        # print(self.kwargs['pk'])
        if article1.status.id == 3:
            # article = Article.objects.get(status=1)
            article1.total_views += 1
            article1.save(update_fields=['total_views'])
        context['comment_list'] = self.comment_sort(comments)  # 将排序归类后的文章列表存入传送到模板的数据中
        context['category'] = Category.objects.all()
        try:
            context['session'] = {
                'name': self.request.session['name'],
                'email': self.request.session['email'],
                'content': self.request.session['content']
            }
            # 将session数据存入传送到模板的数据中
        except:  # session读取异常时不做处理
            pass
        comment_form = CommentForm()  # 创建评论表单对象
        context['comment_form'] = comment_form  # 将表单对象传送到模板的数据中
        return context

# 发布评论函数
def pub_comment(request):
        if request.method == 'POST':  # 如果是post请求
            # request.session['name'] = request.POST.get('name')  # 将请求中的昵称存入session
            # request.session['email'] = request.POST.get('email')  # 将请求中的邮箱存入session
            comment = Comment()  # 创建评论对象
            comment.article = Article.objects.get(id=request.POST.get('article'))  # 设置评论所属的文章
            if request.POST.get('reply') != '0':  # 如果回复的不是文章而是他人评论
                comment.reply = Comment.objects.get(id=request.POST.get('reply'))  # 设置回复的目标评论
            form = CommentForm(request.POST, instance=comment)  # 将用户的输入和评论对象结合为完整的表单数据对象
            if form.is_valid():  # 如果表单数据校验有效
                try:
                    form1 = form.save(commit=False)
                    a = request.session.get('_auth_user_id')
                    form1.name = User.objects.get(id=a).username
                    form1.email = '123@compal.com'
                    form1.save()  # 将表单数据存入数据库
                    result = '200'  # 提交结果为成功编码
                    request.session['content'] = ''  # 发布成功时session中存储的内容数据为空值
                except:  # 如果发生异常
                    result = '100'  # 提交结果为失败编码
                    request.session['content'] = request.POST.get('content')  # 发布失败时将请求中的内容存入session

            else:  # 如果表单数据校验无效
                result = '100'  # 提交结果为失败编码
            return HttpResponse(result)  # 返回提交结果到页面
        else:  # 如果不是post请求
            return HttpResponse('非法请求！')  # 返回提交结果到页面

# 注册
def Register(request):
    if request.method =='POST':
        user_name = request.POST.get('username', '')
        pass_word_1 = request.POST.get('password_1', '')
        pass_word_2 = request.POST.get('password_2', '')
        nick_name = request.POST.get('nickname', '')
        email = request.POST.get('email', '')
        if User.objects.filter(username=user_name):
            return render(request, 'register.html', {'error': '用户已存在'})
            #将表单写入数据库
        if(pass_word_1 != pass_word_2):
            return render(request, 'register.html', {'error': '两次密码请输入一致'})
        user = User()
        user.username = user_name
        user.password = pass_word_1
        user.email = email
        user.nickname = nick_name
        user.save()
            #返回注册成功页面
        return render(request, 'login.html')
    else:
        return render(request, 'register.html')

# 登录
def Login(request):
    # 不允许重复登录
    if request.session.get('is_login', None):
        return redirect('index')

    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user1 = User.objects.filter(username=user_name)  #查看数据库里是否有该用户名
        if user1:#如果存在
            user = User.objects.get(username=user_name)#读取该用户信息
            if pass_word == user.password:#检查密码是否匹配
                request.session['is_login'] = True
                request.session['flag'] = "1"
                request.session['user_id'] = user.id
                request.session['nickname'] = user.nickname
                request.session['username'] = user_name
                request.session['_auth_user_id'] = user.id
                request.session['canEdit'] = user.canEdit
                request.session.set_expiry(12 * 60 * 60)
                # print(request.session.get("flag"))
                # queryset = Article.objects.all().order_by('-id')
                # return render(request, 'index.html', {'queryset': queryset})
                return redirect("index")
            else:
                return render(request, 'login.html', {'error': '密码错误!'})
        else:
            return render(request, 'login.html', {'error': '用户名不存在!'})
    else:
        return render(request, 'login.html')

#登出
def logout(request):
    # print('t')
    # print (request.session.get('is_login', None))
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        # print('logout')
        return redirect("login")
    #flush()方法是比较安全的一种做法，而且一次性将session中的所有内容全部清空，确保不留后患。但也有不好的地方，那就是如果你在session中夹带了一点‘私货’，会被一并删除，这一点一定要注意
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("login")



# def logsuccess(request):
#     return render(request, 'index.html')

# def index(request):
#     return render(request, 'index.html')



# def addArticle(request):
#     return render(request, 'addArticle.html')


# 写文章的视图
def article_create(request):
    # 判断用户是否提交数据
    # category = Category.objects.all().order_by("id")
    if not request.session.get('is_login', None):
        return redirect('login')
    category = Category.objects.all().order_by("id")
    tag = Tag.objects.all()
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = addArticleForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            a = request.session.get('_auth_user_id')
            new_article.author = User.objects.get(id=a)
            # print(new_article)
            # new_article.category = Category.objects.get(id=1)
            if request.session.get('canEdit') == 0:
                new_article.status = Status.objects.filter(id=3).first()
            else:
                new_article.status = Status.objects.filter(id=2).first()
            # 将新文章保存到数据库中
            new_article.save()
            article_post_form.save_m2m()
            # 完成后返回到文章列表
            # return render(request, 'addArticle.html', locals())
            if request.session.get('canEdit') == 0:
                return redirect('index')
            else:
                return redirect('myArticle')
        # 如果数据不合法，返回错误信息
        else:
            error = "表单内容有误，请重新填写。"
            cleanData = article_post_form.errors
            # return render(request, 'addArticle.html', {'error': '表单内容有误，请重新填写。'})
            # print(article_post_form)
            return render(request, 'addArticle.html', locals())
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = addArticleForm()
        # 赋值上下文
        context = {'article_post_form': article_post_form, 'category': category, "tag": tag }
        # 返回模板
        return render(request, 'addArticle.html', context)

# 删文章
def article_delete(request, id):
    # if request.session.get('is_login', None):
    #     return redirect('login')
    # 根据 id 获取需要删除的文章
    comment = Comment.objects.filter(article_id=id).order_by('-reply_id')
    for com in comment:
        print(com.reply_id, '111111')
        comment1 = Comment.objects.filter(article_id=id, reply_id=com.reply_id)
        comment1.delete()
    article = Article.objects.get(id=id)
    # 调用.delete()方法删除文章
    article.delete()
    # 完成删除后返回文章列表
    # if request.session.get('canEdit') == 0:
    return redirect("index")
    # else:
    #     return redirect("myArticle")

# 我的文章
def MyArticle(request):
    if not request.session.get('is_login', None):
        return redirect('login')
    a = request.session.get('_auth_user_id')
    queryset = Article.objects.filter(author=a).order_by('status', '-pub_time')
    order = 'normal'
    # queryset = Article.objects.filter(status=1).order_by('-id')
    # 每页显示 1 篇文章
    paginator = Paginator(queryset, 5)
    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给 articles
    articles = paginator.get_page(page)
    category = Category.objects.all().order_by("id")
    context = {
                'articles': articles,
                'category': category,
                'order': order
              }
    return render(request, 'myArticle.html', context)



# 关闭评论功能
def closeComment(request):
    if request.method == 'POST':  # 如果是post请求
        article = Article.objects.get(id=request.POST.get('article'))
        # print(article)
        article.permission = 1
        article.save()
        result = '200'
        return HttpResponse(result)
    else:
        result = '100'
        return HttpResponse(result)


# 更新文章
def article_update(request, id):
    # 获取需要修改的具体文章对象
    category = Category.objects.all().order_by("id")
    tag = Tag.objects.all()
    article = Article.objects.get(id=id)
    list = []
    for i in article.tag.all():
        list.append(i.id)
    # 判断用户是否为 POST 提交表单数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = updateArticleForm(data=request.POST)
        # print(article_post_form, "1234222")
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.content = request.POST['content']
            a = request.POST.get("category")
            article.category = Category.objects.get(id=a)
            taglist = request.POST.getlist('tag')
            article.status = Status.objects.get(id=2)
            # print(taglist)
            # for tag in taglist:
            article.tag.set(taglist)
            article.reason = ''
            # print(request.POST.getlist('tag'))
            article.save()
            # 完成后返回到修改后的文章中。需传入文章的 id 值
            return redirect("detail", pk=id)
        # 如果数据不合法，返回错误信息
        else:
            error = "表单内容有误，请重新填写。"
            # return HttpResponse("表单内容有误，请重新填写。")
            return render(request, 'updateArticle.html', locals())

    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        article_post_form = updateArticleForm()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        # context = {
        #                'article': article,
        #                'article_post_form': article_post_form,
        #                'category': category,
        #                'tag': tag
        #            }
        # 将响应返回到模板中
        return render(request, 'updateArticle.html', locals())

#增加标签
def Tag_add(request):
    if request.method == "POST":
        tag_name = request.POST.get('tag')
        tag = Tag()
        tag.name = tag_name
        tag.save()
        return redirect("addArticle")
    else:
        return HttpResponse("表单内容有误，请重新填写。")

#审核文章页面
def examine_article(request):
    queryset = Article.objects.filter(status='2').order_by('-pub_time', '-status')
    status = Status.objects.all()
    order = 'normal'
    # 每页显示 1 篇文章
    paginator = Paginator(queryset, 5)
    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给 articles
    articles = paginator.get_page(page)
    category = Category.objects.all().order_by("id")
    context = {
                'articles': articles,
                'category': category,
                'order': order,
                'status': status
              }
    return render(request, 'auditingArticle.html', context)

#修改文章状态
def ChangeStatus(request):
    id = request.POST.get('sta')
    print(id, '11111')
    if request.method == "POST":
        article = Article.objects.get(id=id)
        article.status = Status.objects.get(id=request.POST.get('status'))
        # print(article.status, '222222')
        article.reason = request.POST.get('reason')
        article.save()
        return redirect("auditing")
    else:
        return HttpResponse("内容有误，请重新填写。")

    # if request.method == 'POST':  # 如果是post请求
    #     article = Article.objects.get(id=request.POST.get('sta'))
    #     # print(article)
    #     article.status = Status.objects.get(id=request.POST.get('id'))
    #     article.save()
    #     result = '200'
    #     return HttpResponse(result)
    # else:
    #     result = '100'
    #     return HttpResponse(result)


def changPassword(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    # print (request.method)
    if request.method == "POST":
        OldPassword=request.POST.get('inputoldPassword', '')
        Password = request.POST.get('inputnewPassword1', '')
        Passwordc = request.POST.get('inputnewPassword2', '')
        user = request.session.get('_auth_user_id')
        userpass = User.objects.get(id=user).password
        # print(OldPassword,userpass)
        if OldPassword == userpass:
            if Password == Passwordc:
                # print(request.session.get('user_name', None))
                updatep = User.objects.filter(username=request.session.get('username', None))
                # print (updatep)
                # for e in updatep:
                #    print (e.password)
                updatep.update(password=Password)
                request.session.flush()
                return redirect("/login/")
            else:
                error = "密码不一致"
                return render(request, 'changePass.html', locals())
        else:
            error = "旧密码不正确"
            return render(request, 'changePass.html', locals())
    return render(request, 'changePass.html', locals())


def change_flag(request):
    if request.method == 'POST':  # 如果是post请求
        request.session['flag'] = "2"
        result = '200'
        return HttpResponse(result)
    else:
        request.session['flag'] = True
        result = '100'
        return HttpResponse(result)
