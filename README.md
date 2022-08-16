# blog-ocean-brasil
Para deploy no Heroku

FAzer login

## Cria app
heroku create <nome do app>
## cria Banco
heroku addons:create heroku-postgresql:hobby-dev --app <nome do app>
## Verifica config do app
heroku config --app blog-python-ocean

## Para atualizar
git push heroku main
