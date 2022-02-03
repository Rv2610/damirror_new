from django.db import models

class Songs(models.Model):
    songname = models.CharField(max_length=100 , default="null")
    songlink= models.CharField(max_length=100 , default="null")
    
    


    
   


    

