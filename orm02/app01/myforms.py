
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app01 import models
import re


def mobile_validate(value):
    mobile_re = re.compile(r'.*--.*')  # -- sql注释符号
    if mobile_re.match(value):
        raise ValidationError('不能包含--特殊字符')


class BookForm(forms.Form):

    title = forms.CharField(
        label='书籍名称',
        min_length=1,
        max_length=32,
        validators=[mobile_validate,],
        # widget=forms.TextInput(attrs={'class':'form-control'})
        error_messages={
            'required':'不能为空',
            'min_length':'太短了,你也好意思!',

        }
    )

    price = forms.DecimalField(    # 1000.11
        label='价格',
        max_digits=5,
        decimal_places=2,

    )
    publishDate = forms.CharField(
        label='出版日期',
        widget=forms.TextInput(attrs={'type':'date'}),
    )

    publishs = forms.ModelChoiceField(
        label='出版社',
        queryset=models.Publish.objects.all(),
        # choices=[(1)]
        # choices=[(1,出版社id为1的model对象),(2,出版社id为2的model对象)]
    )

    authors = forms.ModelMultipleChoiceField(
        label='作者',
        queryset=models.Author.objects.all(),
    )

    # csrfmiddle

    # publishs = forms.ChoiceField(
    #     label='出版社',
    #     choices=models.Publish.objects.all().values_list('id','name'),  # queryset([(1,'xx出版社'),()]) -- [{'id':1,'name':'xx出版社'},]
    # )
    #
    # authors = forms.MultipleChoiceField(
    #     label='作者',
    #     choices=[(1,'旭东'),(2,'金龙'),(3,'亚洲')],
    # )

    # 批量操作字段
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})






class BookModelForm(forms.ModelForm):

    # 自己定义的属性优先级高,会覆盖modelform翻译出来的属性
    # title = forms.CharField(
    #     label='书籍名称',
    #     min_length=1,
    #     max_length=32,
    #     validators=[mobile_validate, ],
    #     # widget=forms.TextInput(attrs={'class':'form-control'})
    #     error_messages={
    #         'required': '不能为空',
    #         'min_length': '太短了,你也好意思!',
    #
    #     }
    # )

    class Meta:
        model = models.Book
        fields = '__all__'
        labels = {
            'title':'书名',
            'price':'价格',
            'publishDate':'出版日期',
            'publishs':'出版社',
            'authors':'作者',
        }
        error_messages = {
            'title':{
                'required':'书名不能为空',
                'max_length':'太长了',
            },
            'price':{
                'required':'价格不能为空',
            }

        }
        # validators={
        #     'title':[mobile_validate,]
        # }

    def __init__(self,*args,**kwargs):

        super().__init__(*args,**kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class':'form-control xx oo'})

