from mixer.backend.django import mixer
from clients.models import *

# https://github.com/klen/mixer

'''
OBS: o mixer vai criar os dados direto no banco de dados
cycle -> 100 dados
blend -> qual model vai se basear. como Order (pedido) tem relações de
1-N com cliente e N-N com produtos, ele já cria essas classes fakes tbm
apesar que se for N-N e já existir dados, é provável que ele vá utilizar
os dados existentes
'''
# mixer.cycle(5).blend(Order)
mixer.cycle(5).blend(Product)

'''
# para executar precisa do shell do django:
python manage.py shell < clients/mixers/clients_mixer.py 

'''
