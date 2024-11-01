from django.db import models

# Create your models here.

class TodoList(models.Model):
    tasks=models.CharField(max_length=250)
    done=models.BooleanField("Done",default=False)

    def __str__(self) -> str:
        return self.tasks
