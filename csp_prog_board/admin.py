from django.contrib import admin
from .models import Csp_prog_list, Csp_prog_list_qna, Prog_comment, Prog_comment_qna

# Register your models here.

admin.site.register(Csp_prog_list)
admin.site.register(Csp_prog_list_qna)
admin.site.register(Prog_comment)
admin.site.register(Prog_comment_qna)