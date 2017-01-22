#/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.http import HttpResponse, Http404
from blog.models import Article, Contact, Categorie
from blog.forms import ContactForm, ArticleForm, NouveauContactForm
from django.views.generic import ListView, DetailView

# Create your views here.

def home(request):
	""" Exemple de page HTML, non valide pour que l'exemple soit concis """
	text = """<h1>Bienvenue sur mon blog !</h1>
			  <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
	return HttpResponse(text)

def view_article(request, id_article):
	""" Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
		Son ID est le second paramètre de la fonction (pour rappel, le premier
		paramètre est TOUJOURS la requête de l'utilisateur) """
 
	# Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
	if int(id_article) > 100 :
		raise Http404
	elif int(id_article) > 50 :
		return redirect('afficher_article', id_article=1)

	text = "Vous avez demandé l'article #{0} !".format(id_article)
	return HttpResponse(text)

def list_articles(request, month, year):
	""" Liste des articles d'un mois précis. """

	# Il veut des articles qui sont pas d'une bonne année ? on redirige
	if int(year) > 2015 : 
		return redirect(view_redirection)
		return redirect("https://www.djangoproject.com")

	text = "Vous avez demandé les articles du mois {0} de l'année {1}.".format(month, year)
	return HttpResponse(text)

def view_redirection(request):
	return HttpResponse("Vous avez été redirigé.")

def date_actuelle(request):
	couleurs = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet']
	couleursdico = {'FF0000':'rouge', 
			'ED7F10':'orange', 
			'FFFF00':'jaune', 
			'00FF00':'vert', 
			'0000FF':'bleu', 
			'4B0082':'indigo', 
			'660099':'violet'}
	id_article = 42
	return render(request, 'blog/date.html', {'date': datetime.now(), 'age' : 17, 'couleurs' : couleurs, 
		'couleursdico' : couleursdico, 'ID_article' : id_article})

def addition(request, nombre1, nombre2):    
	total = int(nombre1) + int(nombre2)

	# Retourne nombre1, nombre2 et la somme des deux au tpl
	return render(request, 'blog/addition.html', locals())

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

def lire(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire.html', {'article':article})

def contact(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = ContactForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            # Ici nous pouvons traiter les données du formulaire
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            renvoi = form.cleaned_data['renvoi']

            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer

            envoi = True

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = ContactForm()  # Nous créons un formulaire vide

    return render(request, 'blog/contact.html', locals())

def articleForm(request) :
	article = Article.objects.get(pk=1)
	if request.method == 'POST':  # S'il s'agit d'une requête POST
		form = ArticleForm(request.POST, instance=article)
		if form.is_valid():
		    form.save()
	else :
		form = ArticleForm(instance=article)  # article est bien entendu un objet d'Article quelconque dans la base de données
	return render(request, 'blog/contact.html', locals())

def nouveau_contact(request):
    sauvegarde = False

    if request.method == "POST":
        form = NouveauContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = Contact()
            contact.nom = form.cleaned_data["nom"]
            contact.adresse = form.cleaned_data["adresse"]
            contact.photo = form.cleaned_data["photo"]
            contact.save()

            sauvegarde = True
    else:
        form = NouveauContactForm()

    return render(request, 'blog/newcontact.html', locals())

def voir_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'blog/voir_contacts.html', {'contacts': contacts})

class ListeArticles(ListView):
    model = Article
    context_object_name = "derniers_articles"
    template_name = "blog/accueil.html"
    paginate_by = 3

    def get_queryset(self):
       return Article.objects.filter(categorie__id=1)

    def get_context_data(self, **kwargs):
	    # Nous récupérons le contexte depuis la super-classe
	    context = super(ListeArticles, self).get_context_data(**kwargs)
	    # Nous ajoutons la liste des catégories, sans filtre particulier
	    context['categories'] = Categorie.objects.all()
	    return context

class LireArticle(DetailView):
    context_object_name = "article"
    model = Article
    template_name = "blog/lire.html"

    def get_object(self):
        # Nous récupérons l'objet, via la super-classe
        article = super(LireArticle, self).get_object()
    
        article.nb_vues += 1  # Imaginons un attribut « Nombre de vues »
        article.save()
    
        return article  # Et nous retournons l'objet à afficher