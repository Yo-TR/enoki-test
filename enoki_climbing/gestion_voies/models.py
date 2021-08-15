from django.db import models
from django.utils import timezone
import string, random
from django.utils.text import slugify

def get_upload_path(instance, filename):
    x = random.choices(string.ascii_uppercase + string.digits, k=5)
    x = ''.join(x)
    ext = filename.split('.')[-1]
    print(x)
    return '{article}/images/{filename}'.format(article=instance.media_article, filename= 'image'+instance.media_article.art_title+x+'.'+ext)


# Create your models here.
class Commentaires(models.Model):
    """
    Description: Model Description
    """
    comment_author = models.CharField(max_length=280, verbose_name='Auteur*')
    comment_rating = models.IntegerField(verbose_name='Note*')
    comment_datetime = models.DateTimeField(auto_now_add=True,verbose_name="Date de parution")
    comment_article = models.ForeignKey('Articles',on_delete=models.CASCADE,)
    comment_content = models.TextField(verbose_name='Commentaire*')

    class Meta:
        verbose_name = "Commentaire"
        ordering = ['comment_datetime']

    def __str__(self):
    	return self.comment_author


class Articles(models.Model):
    """
    Description: Model Description
    """
    art_title = models.CharField(unique=True, max_length=60,verbose_name="Nom de la voie*")
    art_datetime = models.DateTimeField(auto_now_add=True,verbose_name="Date de parution*")
    slug = models.SlugField(max_length=100)
    art_content = models.TextField(verbose_name="Description*") 

    class Meta:
        verbose_name = "article"
        ordering = ['-art_datetime']
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.art_title)
        super(Articles, self).save(*args, **kwargs)

    def __str__(self):
        return self.art_title


class Media(models.Model):
    """
    Réference des media uploader
    """
    media_article = models.ForeignKey('Articles', on_delete=models.CASCADE)
    media_img = models.ImageField(upload_to=get_upload_path, max_length=100, height_field=None, width_field=None,null=False,blank=False, verbose_name="Image d'article")


    class Meta:
        verbose_name = "Images d'articles"

    def __str__(self):
        return self.media_article