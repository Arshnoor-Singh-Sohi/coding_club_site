from django import forms
from myapp.models import Order

class FeedbackForm(forms.Form):
    FEEDBACK_CHOICES = [
        ('B', 'Borrow'),
        ('P', 'Purchase'),
    ]
    feedback = forms.ChoiceField(
        choices = FEEDBACK_CHOICES,
    )

class SearchForm(forms.Form):
    # Field 1: name - UPDATED with custom label as per Part 3a
    name = forms.CharField(
        max_length=100,
        required=False,
        label='Your Name'       # NEW: Custom label instead of default "Name"
    )
    
    # Field 2: category - UPDATED to be optional with custom label as per Part 3b
    CATEGORY_CHOICES = [
        ('S', 'Science & Tech'),
        ('F', 'Fiction'),
        ('B', 'Biography'),
        ('T', 'Travel'),
        ('O', 'Other'),
    ]
    
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.RadioSelect,
        required=False,                    # NEW: Made optional as per Part 3b
        label='Select a category:'         # NEW: Custom label as per Part 3b
    )
    
    # Field 3: NEW FIELD - max_price as per Part 3c
    max_price = forms.IntegerField(
        label='Maximum Price',      # Custom label
        min_value=0,               # Users cannot enter value less than 0
        required=True              # This field is required
    )
    
    # PART 3: Custom validation method for max_price
    def clean_max_price(self):
        """
        Additional custom validation for max_price field.
        This method is called automatically by Django when form.is_valid() is called.
        """
        price = self.cleaned_data.get('max_price')
        
        # Additional check to ensure price is not negative
        if price is not None and price < 0:
            raise forms.ValidationError("Maximum price cannot be less than 0")
        
        return price

class OrderForm(forms.ModelForm):
    """
    This is a ModelForm - Django automatically creates form fields 
    based on the Order model fields. Much easier than creating each field manually!
    """
    
    class Meta:
        model = Order  # Tell Django which model to base this form on
        fields = ['books', 'member', 'order_type']  # Which model fields to include in the form
        
        # Customize how fields are displayed
        widgets = {
            'books': forms.CheckboxSelectMultiple(),  # Show books as checkboxes (can select multiple)
            'order_type': forms.RadioSelect           # Show order type as radio buttons
        }
        
        # Custom labels (optional)
        labels = {
            'member': 'Member name',  # Change "Member" to "Member name"
        }
