from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class ProjectCode(models.Model):
    pcode = models.CharField(primary_key=True, max_length=4)
    pname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'project_code'

class Csp_prog_list(models.Model):
    no = models.AutoField(primary_key=True)
    pcode = models.CharField(max_length=4)
    user_id = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(max_length=20000)
    is_complete = models.BooleanField()
    end_date = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def csp_prog_save(self):
        self.save()

    class Meta:
        managed = False
        db_table = 'prog_board'



class Csp_prog_list_qna(models.Model):
    no = models.AutoField(primary_key=True)
    pcode = models.CharField(max_length=4)
    user_id = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(max_length=20000)
    is_complete = models.BooleanField()
    end_date = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def csp_prog_save_qna(self):
        self.save()

    class Meta:
        managed = False
        db_table = 'prog_board_qna'