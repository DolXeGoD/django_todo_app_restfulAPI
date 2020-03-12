from django.db import models

# Create your models here.

class TbTodoList(models.Model):
    no = models.AutoField(primary_key=True)
    pcode = models.CharField(max_length=4, blank=True, null=True)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    is_complete = models.IntegerField(blank=True, default=0)
    priority = models.IntegerField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_todo_list'