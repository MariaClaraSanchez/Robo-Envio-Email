from controllers.config import Config
from controllers.enviar_email import Email
from controllers.lista_emails import Planilha

def start():
    config = Config.get_config()

    arquivo = Planilha()
    dados = arquivo.emails()

    email = Email(dados,config['login']['user'],
                                 config['login']['senha'])

    email.enviar()

if __name__ == '__main__':
    start()