from django import forms
from .models import Csp_hack_list, Csp_hack_list_qna
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class Csp_hack_form(forms.ModelForm):
    class Meta:
        model = Csp_hack_list
        fields = ('title', 'content', 'is_complete')

    widgets = {
        'content': forms.CharField(widget=CKEditorUploadingWidget()),
    }


class Csp_hack_form_qna(forms.ModelForm):
    class Meta:
        model = Csp_hack_list_qna
        fields = ('title', 'content', 'is_complete')

    widgets = {
        'content': forms.CharField(widget=CKEditorUploadingWidget()),
    }
