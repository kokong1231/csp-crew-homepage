from django import forms
from .models import Csp_hack_list, Csp_hack_list_qna, Hack_comment, Hack_comment_qna
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class Csp_hack_form(forms.ModelForm):
    class Meta:
        model = Csp_hack_list
        fields = ('title', 'content', 'is_complete')

    widgets = {
        'content': forms.CharField(widget=CKEditorUploadingWidget()),
    }

class Hack_CommentForm(forms.ModelForm):

    class Meta:
        model = Hack_comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].label = "댓글"

class Csp_hack_form_qna(forms.ModelForm):
    class Meta:
        model = Csp_hack_list_qna
        fields = ('title', 'content', 'is_complete')

    widgets = {
        'content': forms.CharField(widget=CKEditorUploadingWidget()),
    }

class Hack_CommentForm_qna(forms.ModelForm):

    class Meta:
        model = Hack_comment_qna
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].label = "댓글"