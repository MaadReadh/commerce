from django import  forms

from auctions.models import  Category, Bid, Comment, Listing


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = [
            'category'
        ]


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            'title',
            'description',
            'imgurl',
            'price',
            'category',
        ]
 


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = [
            'bid'
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comments',
        ]
