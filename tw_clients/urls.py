"""tw_clients URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls')),
]


'''
# comandos utilizando o dumpdata; ele exporta os dados do db para o arquivo
python manage.py dumpdata > dados.json
python manage.py dumpdata --indent 2 > dados.json
python manage.py dumpdata --indent 2 --exclude auth.permission > dados.json
python manage.py dumpdata --indent 2 --exclude auth.permission --format xml > dados.xml
'''

'''
# comando para importar para o db os dados de um arquivo existente
python manage.py loaddata dados.json

# OBS: por padrão o django vai procurar no diretório fixtures
# ele não "readiciona" os que ja existiam, apenas é armazenado os novos dados
'''