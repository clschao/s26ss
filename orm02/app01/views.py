from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from app01 import models

from django.db.models import Avg,Max,Min,Count,Sum,F,Q





def book_list(request):
    all_books = models.Book.objects.all()

    # book_obj = models.Book.objects.get(id=1)
    # book_obj.authors.all() # 拿到这个书籍对应的所有的作者对象




    return render(request,'book_list.html',{'all_books':all_books})





from django.views import View
from app01 import myforms

class BookAddView(View):

    def get(self,request):
        # all_publishs = models.Publish.objects.all()
        # all_authors = models.Author.objects.all()
        book_form_obj = myforms.BookForm()


        return render(request,'book_add.html',{'book_form_obj':book_form_obj})

    def post(self,request):
        print(request.POST)
        book_form_obj = myforms.BookForm(request.POST)
        if book_form_obj.is_valid():
            # print(book_form_obj.cleaned_data)
            data = book_form_obj.cleaned_data
            authors = data.pop('authors')
            new_book = models.Book.objects.create(
                **data
            )
            new_book.authors.add(*authors)
            # new_book.authors.add(*[1,2])

            return redirect('book_list')
        else:
            return render(request,'book_add.html',{'book_form_obj':book_form_obj})



        # data = request.POST.dict()
        # # print('>>>>',data)
        # data.pop('csrfmiddlewaretoken')
        # authors = request.POST.getlist('authors')
        # data.pop('authors')
        # print(authors)
        # # create方法的返回值就是你创建的这个记录的model对象
        # new_booj_obj = models.Book.objects.create(
        #     **data
        #     # publishs=models.Publish.objects.get(id=1),
        #     # publishs_id=1,
        # )
        # # book_obj = models.Book.objects.get(title=data['title'])
        # # book_obj.authors.add(1,2,3)
        # new_booj_obj.authors.add(*authors)


        return redirect('book_list')


def login(request):
    return render(request,'auth/login.html')

def register(request):
    return render(request,'auth/register.html')

class BookEditView(View):

    def get(self,request,book_id):

        old_book_obj = models.Book.objects.get(id=book_id)

        # all_publishs = models.Publish.objects.all()
        # all_authors = models.Author.objects.all()
        form_obj = myforms.BookModelForm(instance=old_book_obj)

        # print(form_obj)

        return render(request,'book_edit.html',{'form_obj':form_obj})
        # return render(request,'book_edit.html',{'old_book_obj':old_book_obj,'all_publishs':all_publishs,'all_authors':all_authors})

    def post(self,request,book_id):
        old_book_obj = models.Book.objects.get(id=book_id)
        # old_book_obj = models.Book.objects.get(id=2)
        # form_obj = myforms.BookModelForm(request.POST,instance=old_book_obj)
        form_obj = myforms.BookModelForm(request.POST,instance=old_book_obj)
        if form_obj.is_valid():
            # data = book_form_obj.cleaned_data
            # authors = data.pop('authors')
            # new_book = models.Book.objects.create(
            #     **data
            # )
            # new_book.authors.add(*authors)

            ret = form_obj.save()  #不加instance --create
            # 加上instance关键字,就是update操作
            print('>>>',ret)
            return redirect('book_list')
        else:
            return render(request, 'book_edit.html', {'form_obj': form_obj})
        # data = request.POST.dict()
        # # print('>>>>',data)
        # data.pop('csrfmiddlewaretoken')
        # authors = request.POST.getlist('authors')
        # data.pop('authors')
        # print(authors)
        # # create方法的返回值就是你创建的这个记录的model对象
        #
        # obj_query_set = models.Book.objects.filter(id=book_id)
        #
        # obj_query_set.update(
        #     **data
        # )
        #
        # # print(ret)
        # # ['1','2','3']
        #
        # obj_query_set.first().authors.set(authors)

        return redirect('book_list')



def book_del(request,book_id):
    models.Book.objects.filter(id=book_id).delete()
    return redirect('book_list')

from django.http import JsonResponse

def swal_delete(request):

    ret_data = {'status':None,}
    if request.method == 'POST':

        try:
            book_id = request.POST.get('id')
            models.Book.objects.filter(id=book_id).delete()
            ret_data['status'] = 1
        except Exception:
            ret_data['status'] = 2
        return JsonResponse(ret_data)

    return redirect('book_list')


def index(request):

    # 1 查询每个作者的姓名以及出版的书的最高价格
    # ret = models.Author.objects.values('id','name').annotate(m=Max('book__price'))
    #
    # print(ret)

    # 2 查询作者id大于2作者的姓名以及出版的书的最高价格
    # ret = models.Author.objects.filter(id__gt=2).values('name').annotate(a=Max('book__price'))
    # print(ret)


    # 3 查询作者id大于2或者作者年龄大于等于3岁的女作者的姓名以及出版的书的最高价格
    # ret = models.Author.objects.filter(Q(id__gt=2)|Q(Q(age__gte=3)&Q(sex='女'))).values('name').annotate(a=Max('book__price'))
    # print(ret)

    # 4 查询每个作者出版的书的最高价格 的平均值
    # ret = models.Book.objects.values('authors__name').annotate(m=Max('price')).aggregate(a=Avg('m'))
    # print(ret)

    # 5 每个作者出版的所有书的最高价格以及最高价格的那本书的名称
    # ret = models.Book.objects.values('authors__name').annotate(m=Max('price'))  #  queryset({'authors__name':'xx','m':100},{'authors__name':'xx','m':100},)


    ret = models.Author.objects.annotate(m=Max('book__price')).values('m','name','book__title')
    # print(ret)
    # '''
    # select * from (select app01_author.name,app01_book.title,app01_book.price from app01_book INNER JOIN app01_book_authors on app01_book.id = app01_book_authors.book_id
    # INNER JOIN app01_author on app01_author.id = app01_book_authors.author_id ORDER BY app01_book.price desc) as t
		# group by t.name;
    #
    # '''


def xx(request):
    if request.method == 'GET':
        return render(request,'this指向问题.html')
    else:
        book_id = request.POST.get('id')

        models.Book.objects.filter(id=book_id).delete()

        return HttpResponse('ok')










    return HttpResponse('ok')




def yanzhou(request):

    return render(request,'')









