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

class Csp_hack_list(models.Model):
    no = models.AutoField(primary_key=True)
    pcode = models.CharField(max_length=4)
    user_id = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(max_length=20000)
    is_complete = models.BooleanField()
    end_date = models.DateTimeField(default=timezone.now())
    user_name = models.CharField(max_length=50)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def csp_hack_save(self):
        self.save()

    class Meta:
        managed = False
        db_table = 'hack_board'



class Csp_hack_list_qna(models.Model):
    no = models.AutoField(primary_key=True)
    pcode = models.CharField(max_length=4)
    user_id = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(max_length=20000)
    is_complete = models.BooleanField()
    end_date = models.DateTimeField(default=timezone.now())
    user_name = models.CharField(max_length=50)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def csp_hack_save_qna(self):
        self.save()

    class Meta:
        managed = False
        db_table = 'hack_board_qna'


class Hack_comment(models.Model):
    user_no = models.AutoField(primary_key=True)
    comment = models.TextField(max_length=500)
    user_name = models.CharField(max_length=50)
    insert_date = models.DateTimeField(default=timezone.now())
    no = models.ForeignKey(Csp_hack_list, on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def hack_comment_save(self):
        self.save()

    class Meta:
        managed = False
        db_table = 'hack_comment'