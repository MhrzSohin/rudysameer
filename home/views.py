from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *


# Create your views here.
class BaseView(View):
    views = {}
    views['categories'] = Category.objects.all()
    views['organics'] = Product.objects.filter(labels='organic')
    views['freshs'] = Product.objects.filter(labels='fresh')
    views['bests'] = Product.objects.filter(labels='best')
    views['services'] = Service.objects.all()
    views['vegetables'] = Product.objects.filter(category_id=1)
    views['fruits'] = Product.objects.filter(category_id=2)
    views['breads'] = Product.objects.filter(category_id=3)
    views['meats'] = Product.objects.filter(category_id=4)


class HomeView(BaseView):
    def get(self, request):
        self.views
        self.views['sliders'] = Slider.objects.all()
        self.views['feedbacks'] = Feedback.objects.all()
        self.views['features'] = Feature.objects.all()

        return render(request, 'index.html', self.views)


class CartView(BaseView):
    def get(self, request):
        username = request.user.username
        total_price = 0
        self.views['cart_products'] = Cart.objects.filter(name=username, checkout=False)
        for i in Cart.objects.filter(name=username, checkout=False):
            total_price = total_price + i.total
        self.views['total_price'] = total_price
        self.views['delivery_charge'] = 5
        self.views['all_total_price'] = total_price + self.views['delivery_charge']
        return render(request, 'cart.html', self.views)


class ShopView(BaseView):
    def get(self, request):
        self.views
        self.views['products'] = Product.objects.all()
        return render(request, 'shop.html', self.views)


class CategoryView(BaseView):
    def get(self, request, slug):
        self.views
        cat_id = Category.objects.get(slug=slug).id
        self.views['cat_products'] = Product.objects.filter(category_id=cat_id)
        return render(request, 'category.html', self.views)


class SearchView(BaseView):
    def get(self, request):
        self.views
        query = request.GET.get('search')
        if query != '':
            self.views['search_products'] = Product.objects.filter(name__icontains=query)
        else:
            return redirect('/')
        return render(request, 'search.html', self.views)


class DetailView(BaseView):
    def get(self, request, slug):
        self.views['detail_products'] = Product.objects.filter(slug=slug)
        cat_id = Product.objects.get(slug=slug).category_id
        self.views['related_products'] = Product.objects.filter(category_id=cat_id)
        self.views['product_reviews'] = ProductReviews.objects.filter(slug=slug)
        return render(request, 'shop-detail.html', self.views)


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "This username is already used!")
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "This email is already exists!")
                return redirect('/signup')
            else:
                User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password
                ).save()
        else:
            messages.error(request, "The passwords do not match!")
            return redirect('/signup')

    return render(request, 'signup.html')


def cart(request, slug):
    username = request.user.username
    original_price = Product.objects.get(slug=slug).price

    if Cart.objects.filter(slug=slug).exists():
        qty = Cart.objects.get(slug=slug).quantity
        qty = qty + 1

        price = original_price
        total = price * qty
        Cart.objects.filter(name=username, checkout=False, slug=slug).update(total=total, quantity=qty)
    else:
        price = original_price
        total = original_price

        Cart.objects.create(
            name=username,
            price=price,
            quantity=1,
            total=total,
            slug=slug,
            product=Product.objects.filter(slug=slug)[0]

        )

    return redirect("/cart")


def reduce_quantity(request, slug):
    username = request.user.username
    original_price = Product.objects.get(slug=slug).price

    if Cart.objects.filter(slug=slug).exists():
        qty = Cart.objects.get(slug=slug).quantity
        if qty > 1:
            qty = qty - 1
            price = original_price
            total = price * qty
            Cart.objects.filter(name=username, checkout=False, slug=slug).update(
                total=total, quantity=qty
            )
        else:
            messages.error(request, "The quantity is already 1")
            return redirect('/cart')
        return redirect('/cart')


def delete_cart(request,slug):
    username = request.user.username
    Cart.objects.filter(name = username,slug=slug,checkout = False).delete()
    return redirect('/cart')


def submit_review(request,slug):
    if request.method == 'POST':
        username = request.user.username
        email = request.user.email
        star = request.POST['star']
        review = request.POST['review']
        ProductReviews.objects.create(
            username = username,
            email = email,
            star = star,
            review = review,
            slug = slug,
        ).save()

        return redirect(f'/detail/{slug}')


def checkout(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        address = request.POST['address']
        country = request.POST['country']
        city = request.POST['city']
        phone = request.POST['phone']

        zipcode = request.POST['zipcode']
        payment = request.POST['payment']
        description = request.POST['description']

        Checkout.objects.create(
            firstname=firstname,
            lastname=lastname,
            email=email,
            Address=address,
            country=country,
            city=city,

            zipcode=zipcode,
            phone=phone,
            payment = payment,
            description = description,



            ).save()
        return redirect('/')

    return render(request, 'chackout.html')