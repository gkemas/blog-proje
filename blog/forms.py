from socket import fromshare
from django import forms
from .models import Post, Comment, Category

class PostForm(forms.ModelForm): 
    status = forms.ChoiceField(choices=Post.OPTIONS) # override ettik models de ki status u 
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select") #drobdown menü yapmış olduk emt_label boş ken Select yazacak menü de .
    class Meta:
        model = Post
        fields = ('title',
                   'content',
                   'image',
                   'category',
                   'status', 
                    
                    )
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("content",)
