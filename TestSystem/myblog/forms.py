from django import forms
from .models import Comment, Article


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # 需要呈现在页面上的表单元素
        widgets = {  # 定义字段对应的表单元素以及属性
            # 'name': forms.TextInput(attrs={'id': 'name', 'class': 'form-control', 'placeholder': '请输入昵称'}),
            # 'email': forms.EmailInput(attrs={'id': 'email', 'class': 'form-control', 'style': 'margin-top: 1px;', 'placeholder': '请输入邮箱'}),
            'content': forms.Textarea(attrs={'id': 'content', 'class': 'form-control', 'style': 'margin-top: 1px;', 'placeholder': '请输入评论内容'}),
        }

class addArticleForm(forms.ModelForm):
    # content = forms.CharField(required=True)
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'tag']  # 需要呈现在页面上的表单元素
        # fields = '__all__'  # 需要呈现在页面上的表单元素
        widgets = {  # 定义字段对应的表单元素以及属性
            'title': forms.TextInput(attrs={'id': 'title', "class": "form-control"}),
            'content': forms.Textarea(attrs={'id': 'content', "class": "form-control"}),
            'tag': forms.SelectMultiple(attrs={'id': 'tag', "class": "form-control"}),
            'category': forms.Select(attrs={'id': 'category', "class": "form-control"}),
            # 'tag': forms.EmailInput(attrs={'id': 'tag', "class": "form-control"}),
        }
        # error_messages = {
        #     '__all__': {
        #         'required': '必填',
        #         'invalid': '格式错误'
        #     }
        #     # 'content': {
        #     #     'required': '必填',
        #     #     'invalid': '格式错误'
        #     # }
        # }


class updateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'tag']  # 需要呈现在页面上的表单元素
        widgets = {  # 定义字段对应的表单元素以及属性
            # 'title': forms.TextInput(attrs={'id': 'title'}),
            # 'content': forms.Textarea(attrs={'id': 'content'}),
            # 'tag': forms.Textarea(attrs={'id': 'tag'}),
            # 'category': forms.TextInput(attrs={'id': 'category'}),
        }