from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib


class Email:
    """Classe de email, recebe como parâmetro um dicionário com os dados do destinatário, e recebe o 
        email e senha do rementente
    """
    def __init__(self, destinatarios: dict, remetente: str, senha: str) -> None:
        self.fromaddr = remetente
        self.toaddr = destinatarios
        self.password = senha

    def enviar(self):
        """ Atribui o host a port para criar o servivdor para enviar o email.
            Cria um laço de repetição para pegar todos os nomes e mails e para cada um ele 
            envia o email.
            E dentro do comando de repetição for ele encontra o arquivo dentro do oneDrive e coloca ele no email.
        """
        host = 'smtp.office365.com'
        port = 587

        # Criando o servidor
        server = smtplib.SMTP(host, port)

        #Logando no servidor
        server.ehlo()
        server.starttls()
        server.login(self.fromaddr, self.password)

        for nome,email, in self.toaddr.items():

            # Criando mensagem
            message = f'''
             <p><b>Olá! {nome} </b><br>
                    Como você está?<br>
                    Estamos muito felizes com sua chegada ao nosso time GOE!
                    Seja muito bem-vind@ à nossa equipe.
                    Temos certeza que você será um ótim@ acréscimo ao nosso quadro de colaboradores! <br>
                    
                    Para isso deixamos aqui nosso Workmap para você conhecer tudo sobre nossos processos,
                    como trabalhamos.
                    </p>
            '''

            email_msg = MIMEMultipart()
            email_msg['From'] = self.fromaddr
            email_msg['To'] = email
            email_msg['Subject'] = 'Workmap time GOE'
            email_msg.attach(MIMEText(message, 'html'))

            
            caminho_arquivo = "C://Users//maria//cadmus.com.br//GOE - General//6. Apresentações//Apresentação Talentos.pptx"
            filename = 'BemVindo.pptx'

            with open(caminho_arquivo,'rb') as file:
                att = MIMEBase('aplication', 'octet-stream')
                att.set_payload(file.read())
                encoders.encode_base64(att)

                att.add_header('Content-Disposition',
                            f'attachment; filename= {filename}')
                
                
            email_msg.attach(att)

            # Enviando mensagem
            print(f'Enviando mensagem para {nome}...')
            server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
            print(f'Mensagem enviada!{email}')
            
        server.quit()       