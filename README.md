# Envio E-mail com arquivo 
Essa solução foi desenvolvida utilizando puramente a linguagem de programação Python com algumas biblioteca afim de automatizar o envio de emails com arquivos de extensão .pptx.
  
# Configuração
## Máquina Virtual
Caso queira executar o projeto separadamente da onde fica seus documentos python é preciso cria uma máquina virtual e para isso precisa da os seguintes passos :
<br>
1º Instalar o env em sua máquina para isso utilize o comando :
```
pip install venv
```
2º Criar sua máquina virtual:
```
python3 -m venv nome_maquina_virtual-env
```
3º Escolha o comando de acordo com seu sistema opercional:
#### Para Windows:
```
nome_maquina_virtual-env\Scripts\activate.bat
```
#### Para Unix ou no MacOS:
```
source nome_maquina_virtual-env/bin/activate
```

## Instalando Dependências
Use o gerenciado de pacote [pip](https://pip.pypa.io/en/stable/) para instalar as dependências.
```bash
pip install -r requirements.txt
```

## Arquivo de Configuração
Para executar o projeto é necessário criar um arquivo `config.yaml` na raiz do projeto. Segue exemplo de estrutura do arquivo:

```yaml

login:
  user: '' # endereço do remetente
  senha: '' # senha do remetente
```

# Inicializando

Para executar o robô basta executar o comando :

```
pyhton main.py
```
