from django import  forms

from auctions.models import  Category, Bid, Comment, Listing


class CategoryForm(forms.ModelForm):
    catogery = forms.CharField(label='Enter name of Category')
    class Meta:
        model = Category
        fields = [
            'category'
        ]


class ListingForm(forms.ModelForm):
    date = forms.DateTimeField( label='Select date',
        widget=forms.DateTimeInput(
            attrs={'class': 'form-control', 'type': 'datetime-local', 'placeholder': 'Date', 'autocomplete': 'off'}),
        required=True,
    )
    title=forms.CharField(label='Enter Title of Listing')
    description = forms.CharField(label='Enter description of Listing')
    imgurl = forms.CharField(label='Enter Image URL of Listing')
    price = forms.CharField(label='Enter price of Listing')


    class Meta:
        model = Listing
        fields = [
            'title',
            'description',
            'imgurl',
            'date',
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
