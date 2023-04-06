from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By


class InstaBot:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
        self.servico = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=self.servico)
        self.todas_fotos = []

# Abre o Link do Instagram

    def abrir_link(self, link):
        navegador = self.navegador
        navegador.get(link)

    # Faz o Login e procura pela Nick da pessoa no instagram

    def fazer_login(self):
        navegador = self.navegador
        navegador.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.login)
        navegador.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.senha)
        navegador.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
        # Aguarda 2 segundos enquanto carrega a Pagina
        sleep(5)
        navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button').click()
        sleep(3)
        navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
        sleep(3)
        navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div').click()
        sleep(3)

    # É realizada a pesquisa pela instagran desejado

    def pesquisar_usuario(self, usuario):
        navegador = self.navegador
        navegador.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input').send_keys(usuario)
        sleep(3)
        navegador.find_element(By.CLASS_NAME, "_abm4").click()

    def pegar_fotos(self):
        navegador = self.navegador
        for i in range(1, 2):
            navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(10)
        fotos = navegador.find_elements(By.TAG_NAME, "a")
        for foto in fotos:
            link_foto = foto.get_attribute("href")
            if link_foto.startswith("https://www.instagram.com/p/"):
                self.todas_fotos.append(link_foto)

    def curtir_fotos(self):
        navegador = self.navegador
        for foto in self.todas_fotos:
            navegador.get(foto)
            navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(5)
            navegador.find_element(By.CLASS_NAME, '_aamx').click()
            sleep(4)

    def comentar_fotos(self):
        navegador = self.navegador
        sleep(2)
        for foto in self.todas_fotos:
            navegador.get(foto)
            navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(5)
            navegador.find_element(By.CLASS_NAME, "_aamx").click()
            navegador.find_element(By.CLASS_NAME, 'x1i0vuye').send_keys("#python")
            navegador.find_element(By.CLASS_NAME, 'x1i0vuye').send_keys(Keys.RETURN)
            sleep(4)


