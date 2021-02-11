# flask_api

## Installation

Installation avec pipenv : pipenv install (Attention, il s'agit de la version 3.8)
Créer une base de données sur PostgreSQL nommée "content"

Créer un fichier .env contenant:

*Pour la prod, changer l'environnement*
```
export APP_SETTINGS="settings.config.DevelopmentConfig"
```
*Remplir les champs requis*
```
export DATABASE_URL="postgresql://utilisateur:mot-de-passe@localhost:5432/base-de-données"
```
*clé secrète*
```
SECRET_K = "à changer"
```
## Migration de base de données

Pour l'installation de la base de données:
*Entrer dans l'environnement virtuel*
```
pipenv shell
```

*Faire la migration*
```
python manage.py db migrate
```

## Lancer l'application

*Entrer dans l'environnement virtuel si ce n'est pas déjà fait*
```
pipenv shell
```

*Lancer le serveur local*
```
python manage.py runserver
```

## Utilisation

*Pour ajouter un produit, remplir les champs associés à name et count*
http://127.0.0.1:5000/add?name=xxxx&count=xxxx

*Pour consulter les produits*
http://127.0.0.1:5000/getall

*Pour consulter un produit particulier, remplacer x par l'id du produit*
http://127.0.0.1:5000/get/x

