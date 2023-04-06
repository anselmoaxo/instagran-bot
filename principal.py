import InstagranBot
from time import sleep

# Colocar login e senha para se logar
bot = InstagranBot.InstaBot('colocar o Login ', 'Colocar senha ')
# Abre o Link
bot.abrir_link("https://www.instagram.com/")
# Realiza o Login
bot.fazer_login()
# Busca o o Usuário do Intagran digitado
bot.pesquisar_usuario('colocar o @do usuário a ser  localizado')
bot.pegar_fotos()
bot.curtir_fotos()
bot.comentar_fotos()


