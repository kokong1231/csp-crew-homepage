from django.contrib import admin
from .models import Csp_hack_list, Csp_hack_list_qna, Hack_comment, Hack_comment_qna

# Register your models here.

admin.site.register(Csp_hack_list)
admin.site.register(Csp_hack_list_qna)
admin.site.register(Hack_comment)
admin.site.register(Hack_comment_qna)