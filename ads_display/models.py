from django.db import models

# Create your models here.
class humans(models.Model):
    ID=models.AutoField(primary_key=True)
    Time=models.CharField(max_length=20)
    Date=models.CharField(max_length=20)
    Total_Females=models.IntegerField(null=False)    
    Total_Males=models.IntegerField(null=False)    
    Total_attracted_humans=models.IntegerField(null=False)
    Total_present_humans=models.IntegerField(null=False)
    
        