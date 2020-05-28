from django import forms
from .models import Csp_prog_list, Csp_prog_list_qna, Prog_comment_qna, Prog_comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class Csp_prog_form(forms.ModelForm):
    class Meta:
        model = Csp_prog_list
        fields = ('title', 'content', 'is_complete')

    widgets = {
        'content': forms.CharField(widget=CKEditorUploadingWidget()),
    }

class Prog_CommentForm(forms.ModelForm):

    class Meta:
        model = Prog_comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].label = "댓글"

class Csp_prog_form_qna(forms.ModelForm):
    class Meta:
        model = Csp_prog_list_qna
        fields = ('title', 'content', 'is_complete')

    widgets = {
        'content': forms.CharField(widget=CKEditorUploadingWidget()),
    }

class Prog_CommentForm_qna(forms.ModelForm):

    class Meta:
        model = Prog_comment_qna
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].label = "댓글"