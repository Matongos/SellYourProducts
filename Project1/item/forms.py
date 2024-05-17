from django import forms
from .models import Item

INPUT_CLASSES ='w-full py-6 px-4 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model= Item
        fields= ('Category','name','description','price','image',)
        
        widgets ={
            'Category':forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'name':forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
             'description':forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
              'price':forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
                'image':forms.FileInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
              
                
                
        }