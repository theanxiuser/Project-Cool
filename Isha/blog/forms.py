from django import forms
from .models import Post, Category, Comment

#choices = [("coding", "coding"), ("science", "science"), ("education", "education")]
choices = Category.objects.all().values_list("name", "name")

choice_list = []

for choice in choices:
    choice_list.append(choice)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "author","category", "body", "snippet", "header_image")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter post title here"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control", "value": "", "id": "isha_id","type":"hidden"}),
            #"author": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(choices=choice_list, attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
            "snippet": forms.Textarea(attrs={"class": "form-control"})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "body", "snippet", "header_image")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter post title here"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            #"author": forms.Select(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
            "snippet": forms.Textarea(attrs={"class": "form-control"})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body")

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your name"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }