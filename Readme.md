# universal model package for django

![laravel-universal](https://img.shields.io/badge/stable-v0.01-success)![universal meta model](https://img.shields.io/badge/asddaniel-universal-blue)

Universaldjango est un package  django permettant de gerer vos models sans liens avec les tables de la base de données, donc pas de gestion de migration à chaque nouveau model créé



## Installation

vous pouvez installer ce package via pip:

```bash
pip install universaldjango==0.1
```
vous devez ensuite publier le package à la liste des application installer dans le fichier settings.py de cette façon 

```python 
    INSTALLED_APPS = [
    ...
    'universaldjango',
]


```
l'étape suivante consiste à tourner les migrations

```bash
    python manage.py migrate
```

vous pouvez desormais utilisez les models pour créer vos propres models qui heriterons de celui-ci 

## Utilisation 

pour crée un nouveau models vous n'avez qu'à spécifier le nom du model ainsi que les attributs 

```python
from universaldjango.models import Universal

class Post(Universal):
    attributes = ["auteur", "title", "content"]

```
ici nous venons de définir déja un model avec comme attribut : auteur, title et content
### Lire les données

dans le fichier views.py nous pouvons lire les données de cette manière
```python 

from django.shortcuts import render
from .models import Post


def home(request):
    post = Post()
    posts = post.all() #récupère tous les posts
    one  = post.get(1) #recupere le post dont l'id vaut 1

    
    return render(request, 'index.html', {'posts': posts})


```

### Création, modification et suppression 

pour crée modifier et / ou supprimer vous pouvez utiliser ceci 

```python
from django.shortcuts import render
from .models import Post


def operation(request):
   post = Post()
    post.create({'title': 'post num1', 
    'auteur':'micheal amador', 
    'content':'contenu deux'})
    #crée une nouvelle post

    post.delete(1)
    # supprime le post dont l'id vaut 1

    post.update({'title': 'post num1', 
            'auteur':'micheal amador', 
            'content':'contenu deux'}, 2)
    # met à jour le post dont l'id vaut 2 avec 
    # les donnée du dictionnaire envoyé
    #  comme premier parametere

    return render(request, 'index.html', {'posts': posts})


```

## License 

le package est fourni avec une license libre (MIT)
## auteur et liens

### Auteur
devasddaniel@gmail.com
### Package pip 
 https://pypi.org/project/universaldjango/0.1/
