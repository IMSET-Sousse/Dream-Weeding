# services/views.py
from django.shortcuts import render
from .models import Article   

def liste_articles(request):
    articles = Article.objects.all()  
    return render(request, 'wedding/liste_articles.html', {'articles': articles})  
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarder le message dans la base de données
            return redirect('success')  # Redirection vers une page de succès
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():  # Si les données sont valides
            form.save()  # Sauvegarde le message dans la base de données
            return redirect('success')  # Redirection vers une page de succès
    else:
        form = ContactForm()  # Si la méthode est GET, on affiche un formulaire vide
    return render(request, 'contact.html', {'form': form})


from django.shortcuts import render
from .models import Article

def galerie_view(request):
    articles = Article.objects.all()  # Récupère tous les articles
    return render(request, 'galerie.html', {'articles': articles})
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
