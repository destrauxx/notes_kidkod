from django.db import models

# Create your models here.
class Note(models.Model):
    header = models.CharField(max_length=50, null=False, blank=False)
    text = models.CharField(max_length=250, null=False, blank=False)
    status = models.BooleanField(default=False, blank=True)
    delete_status = models.BooleanField(default=False, blank=True)
    
    def change_status(self):
        self.status = not self.status
    
    def change_delete_status(self):
        self.delete_status = not self.delete_status