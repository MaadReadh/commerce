
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail.backends import console
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import  Max 
from .forms import ListingForm, CategoryForm, BidForm, CommentForm
from .models import User, Listing, Category, Comment, WatchList, Bid

def index(request):
 active_list = Listing.objects.all().filter(active=True)
 return render(request, 'auctions/index.html', {'active_list': active_list})



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")



@login_required
def add_category(request):
    creatCategForm=CategoryForm()
    if request.method =='POST':
        creatCategForm=CategoryForm(request.POST)
        if creatCategForm.is_valid():
            creatCategForm.save()
            return redirect('category-list')
    return render (request,'auctions/addCategory.html',{'creatCategForm':creatCategForm})



def create_listing(request):
    m = ""
    createForm = ListingForm()
    if request.method == 'POST':
        createForm = ListingForm(request.POST)
        if createForm.is_valid():
            obj = createForm.save(commit=False)
            obj.user = request.user
            obj.save()
        
            return redirect('index')
        else:
            m = "error in validity"

    return render(request, 'auctions/creatListing.html', {'creatForm': createForm, 'm': m})



@login_required
def category_list(request):
    category_list = Category.objects.all()
    return render(request, 'auctions/categoryList.html', {'category_list': category_list})

@login_required
def show_category(request, id):
    active_list = Listing.objects.all().filter(category_id=id, active=True)
    return render(request, 'auctions/index.html' , {'active_list':active_list})



def show_listing(request,id):
    message=''
    txt_color='text-primary'
    active_list = Listing.objects.all().filter(id=id)
    bidForm=BidForm()
    commentForm=CommentForm()
    comment_list=Comment.objects.all().filter(listing_id=id)
    max_bid=Bid.objects.all().aggregate(Max('bid'))
    if request.method == 'POST':
        creatBid = BidForm(request.POST)
        if creatBid.is_valid():
         Obj = creatBid.save(commit=False) 
         Obj.user = request.user
         user_bid = creatBid.cleaned_data['bid']
         start = Listing.objects.all().get(id=id).start_bid
         if user_bid > start :
            newList = Listing.objects.all().get(id=id)
            newList.start_bid = user_bid
            newList.save()
            Obj.save()
            message='the current bid is your bid '
            txt_color='text-primary'
         else:
                message = 'previous bids is greatar than your bid'
                txt_color='text-danger'
        else:
            pass
    if request.user.is_anonymous:
        message = 'you can not place bide to this item, Log in first!'