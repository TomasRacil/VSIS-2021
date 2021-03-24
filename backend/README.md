# Backend
V rámci tohoto adresáře je vytvořena ukázková REST API, která slouží jako výchozí bod pro další rozvoj.

## Ovládání

Spuštění flask serveru:
```shell
python manage.py run
```

Vytvoření složky migrace databáze
```shell
python manage.py db init
```

Vytvoření migračního skriptu
```shell
python manage.py db migrate --message 'initial database migration'
```

Provedení migrace na novou verzi
```shell
python manage.py db upgrade
```

Provedení migrace na předchozí verzi
```shell
python manage.py db downgrade
```

Provedení testu funkčnosti
```shell
python manage.py test
```
