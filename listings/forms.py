from django import forms
from .models import Listing

PROPERTY_TYPES = [
    ('Apartment', 'Apartment'),
    ('House', 'House'),
    ('Villa', 'Villa'),
    ('Studio', 'Studio'),
    ('Land', 'Land'),
    ('Commercial', 'Commercial'),
]

TONE_CHOICES = [
    ('Professional', 'Professional'),
    ('Friendly', 'Friendly'),
    ('Premium', 'Premium'),
    ('Luxury', 'Luxury'),
]

class ListingForm(forms.ModelForm):
    property_type = forms.ChoiceField(choices=PROPERTY_TYPES, widget=forms.Select(attrs={'class': 'mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}))
    tone = forms.ChoiceField(choices=TONE_CHOICES, widget=forms.Select(attrs={'class': 'mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}))
    
    class Meta:
        model = Listing
        fields = ['title', 'property_type', 'location', 'price', 'size', 'bedrooms', 'bathrooms', 'features', 'condition', 'tone']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md'}),
            'location': forms.TextInput(attrs={'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md'}),
            'price': forms.TextInput(attrs={'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md'}),
            'size': forms.TextInput(attrs={'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md'}),
            'bedrooms': forms.NumberInput(attrs={'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md'}),
            'bathrooms': forms.NumberInput(attrs={'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md'}),
            'features': forms.Textarea(attrs={'rows': 3, 'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md'}),
            'condition': forms.TextInput(attrs={'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md'}),
        }
