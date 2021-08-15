from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse, HttpRequest, HttpResponseRedirect
from django.forms import modelformset_factory, formset_factory
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from django.db.models import Avg

ListeArticles = Articles.objects.all()
ListeMedia = Media.objects.all()
ListeComments = Commentaires.objects.all()

# Create your views here.
def article(request, slug,):
    article = ListeArticles.get(slug=slug)
    article.average = ListeComments.filter(comment_article=article.id).aggregate(Avg('comment_rating'))
    images = Media.objects.filter(media_article=article)
    Comments = ListeComments.filter(comment_article=article.id)
    CommentsForm = FormComment()
    CommentsForm.fields["comment_article"].initial = article.id
    
    #si une reservation est faite
    if request.method == 'POST':
        form = FormComment(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'gestion_voies/article.html', locals())

def liste_annonces(request):
    ListeArticles = Articles.objects.all()
    #Ajoute pour chaque agences le nombre de voiture et le code postal
    for article in ListeArticles:
            article.img =  Media.objects.filter(media_article=article.id).first()
            article.average = ListeComments.filter(comment_article=article.id).aggregate(Avg('comment_rating'))
    return render(request, 'gestion_voies/liste_annonces.html', locals())

def formulaire(request):
    article = FormArticle()
    images = FormMedia()
    if request.method == 'POST':
        form = FormArticle(request.POST)
        files = request.FILES.getlist('images')
        if form.is_valid():
            post_form = form.save()
            post_form.save()
            for f in files:
                Media.objects.create(media_article=post_form,media_img=f)
            return redirect('index')
    return render(request, 'gestion_voies/formulaire.html', locals())
