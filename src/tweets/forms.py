from django import forms

from .models import tweet

class tweetModelForm(forms.ModelForm):
    #new_title = forms.CharField()
    content = forms.CharField(label='', widget=forms.Textarea(
        attrs={'placeholder':"your message", 
            "class":"form-control"}))
    class Meta:
        model = tweet
        fields = [
           # "user",
            "content"
        ]
    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")
        if content == "abc":
            raise forms.ValidationError("Can not be abc")
        return content
    