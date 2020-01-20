from django import forms
 
STAR_CHOICES = (
    ('0','0'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
)



class AddReviewForm(forms.Form):
    title = forms.CharField(required=True)
    star_score = forms.ChoiceField( widget=forms.RadioSelect, choices=STAR_CHOICES)
    review_content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))