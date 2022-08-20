from django.shortcuts import render,redirect
from owner.models import Books
from django.views.generic import View,ListView,CreateView
from customer.forms import UserRegistrationForm,LoginForm,OrderCreateForm
from django.contrib.auth import authenticate,login,logout
from customer.decorates import sign_in_required
from django.utils.decorators import method_decorator
from customer.models import Carts
from django.db.models import Sum
from customer.models import Orders
from django.contrib import messages

# Create your views here.


@method_decorator(sign_in_required,name="dispatch")
class ViewAllBook(View):
    def get(self,request):
        if request.user.is_authenticated:
            qs=Books.objects.all()
            context={'books':qs}
            return render(request,'list.html',context)
        else:
            return redirect("signin")


class SignUpView(View):
    def get(self,request):
        form=UserRegistrationForm()
        context={'form':form}
        return render(request,"signup.html",context)
    def post(self,request):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("USER CREATED SUCCESSFULLY")
            return render(request,'signup.html')
        else:
            context={'form':form}
            return render(request,'signup.html',context)


class SignInView(View):
    def get(self,request):
        form=LoginForm()
        context={'form':form}
        return render(request,"signin.html",context)
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("c_name")
            else:
                context={'form':form}
                return render(request,"signin.html",context)
def Sign_Out(requset):
    logout(requset)
    return redirect("signin")

class AddToCartView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        book=Books.objects.get(id=id)
        user=request.user
        cart=Carts(user=user,item=book)
        cart.save()
        messages.success(request,"item has been added to cart")

        print("your item had been addedd")
        return redirect("c_name")

class CartItem(ListView):
    model = Carts
    template_name = "itemscart.html"
    context_object_name = "items"
    def get(self,request,*args,**kwargs):
        qs= self.model.objects.filter(user=self.request.user).exclude(status="cancelled")
        total=qs.aggregate(Sum("item__price"))
        print(total)

        sum=total["item__price__sum"]
        context={"items":qs,"sum":sum}

        return render(request,self.template_name,context)
class RemoveCartItem(View):
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        cart=Carts.objects.get(id=id)
        cart.status="cancelled"
        messages.success(request,"item has been removed from cart")

        cart.save()
        return redirect("c_name")

class OrderView(CreateView):
    model=Orders
    form_class=OrderCreateForm
    template_name = "order_create.html"
    def post(self,request,*args,**kwargs):
        print(kwargs)
        form=self.form_class(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.user=request.user
            book=Books.objects.get(id=kwargs["p_id"])
            order.item=book
            order.save()
            c_id=kwargs.get("c_id")
            cart=Carts.objects.get(id=c_id)
            cart.status="order_placed"
            cart.save()
            print("order has been placed")
            messages.success(request, " order has been placed")

            return redirect('c_name')
        else:
            return render(request,self.template_name,{"form":form})

class MyOrders(ListView):
    model = Orders
    template_name = "my_order.html"
    context_object_name = "orders"
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
class CancelOrder(View):
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        order=Orders.objects.get(id=id)
        order.status="order_cancelled"
        order.save()
        messages.success(request,"your order has been cancelled")
        print("your order has been cancelled")
        return redirect("c_name")
