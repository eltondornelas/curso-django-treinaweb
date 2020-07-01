class Router(object):
    # parametros obrigatórios.
    def db_for_read(self, models, **hints):
        return 'read'

    def db_for_write(self, models, **hints):
        return 'write'

# basta retornar o nome da conexão
