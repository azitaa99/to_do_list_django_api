from django.db import models
from django.contrib.auth.models import User




class  Task(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='tasks')
    title=models.CharField(max_length=150, db_index=True)
    description=models.TextField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    complite=models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title} created by {self.user}'
    
    class Meta:
        verbose_name= 'task'
        verbose_name_plural='tasks'
        ordering=['complite','-created']






# Create your models here.
