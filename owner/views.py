from django.shortcuts import render,redirect
from django.http import HttpResponse
from owner.forms import BookForm
from django.urls import reverse_lazy
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from owner.models import Books
from django.utils.decorators import method_decorator
from customer.decorates import owner_permission
# Create your views here.
# from owner.models import books



# class based views, function based
@method_decorator(owner_permission,name="dispatch")
class AddBookView(CreateView):
    model = Books
    form_class = BookForm
    template_name = "addbook.html"
    success_url = reverse_lazy("booklist")

    # def get(self,request,*args,**kwargs):
    #     form=BookForm()
    #     context={'form':form}
    #     return render(request,'addbook.html',context)
    # def post(self,request,*args,**kwargs):
    #     form=BookForm(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return render(request,'addbook.html')
    #     else:
    #         context={'form':form}
    #         return render(request,'addbook.html',context)
@method_decorator(owner_permission,name="dispatch")
class BookListView(ListView):
    model = Books
    context_object_name = "books"
    template_name = "booklist.html"

    # def get(self,request):
    #     qs=Books.objects.all()
    #     context={'books':qs}
    #     return render(request,'booklist.html',context)
@method_decorator(owner_permission,name="dispatch")
class BookDetailView(DetailView):
    model = Books
    context_object_name = "book"
    template_name = "bookdetail.html"
    pk_url_kwarg = "id"
    # def get(self,request,**kwargs):
    #     print(kwargs)
    #     id=kwargs.get('id')
    #     qs=Books.objects.get(id=id)
    #     context={'book':qs}
    #     return render(request,'bookdetail.html',context)
@method_decorator(owner_permission,name="dispatch")
class BookEditView(UpdateView):
    model = Books
    form_class = BookForm
    template_name = "book_edit.html"
    success_url = reverse_lazy("booklist")
    pk_url_kwarg = "id"

    # def get(self,request,**kwargs):
    #     id=kwargs.get('id')
    #     qs=Books.objects.get(id=id)
    #     form=BookForm(instance=qs)
    #     context={'form':form}
    #     return render(request,'book_edit.html',context)
    # def post(self,request,**kwargs):
    #     id=kwargs.get('id')
    #     qs=Books.objects.get(id=id)
    #     form=BookForm(request.POST,files=request.FILES,instance=qs)
    #     if form.is_valid():
    #         form.save()
    #         return render(request,'book_edit.html')
    #     else:
    #         context={'form':form}
    #         return render(request,'book_edit.html',context)
@method_decorator(owner_permission,name="dispatch")
class BookDeleteView(View):
    # template_name = "book_delete.html"
    # context_object_name = "book"
    # template_name = "booklist.html"
    # sucd
    # pk_url_kwarg = "id"

    def get(self,request,**kwargs):
        id=kwargs.get('id')
        qs=Books.objects.get(id=id)
        qs.delete()
        context={'book':qs}
        return render(request,'booklist.html',context)


        # print(form.cleaned_data)
        # bookname=form.cleaned_data.get("book_name")
        # author=form.cleaned_data.get("author_name")
        # price=form.cleaned_data.get("price")
        # copies=form.cleaned_data.get("copies")
        # qs=Books(book_name=bookname,
        #     author=author,
        #     price=price,
        #     copies=copies,
        # )
        # qs.save()
        # print("Book saved")
        # return render(request,"addbook.html")

# def owner_home(request):
#     return render(request,"c_base.html")
#
# def add_book(request):
#     if request.method=="GET":
#         print("inside get")
#         return render(request,"addbook.html")
#     else:
#         print("am inside post ")
#         print(request.method)
#         return render(request, "addbook.html")
#
#
# def lis_book(request):
#     context={"books":books}
#     return render(request,"booklist.html",context)
#
# # owner/books/100
#
# def book_detail(request,id):
#     book=[book for book in books if book["id"]==id]
#     context={"book":book}
#     return render(request,"bookdetail.html",context)