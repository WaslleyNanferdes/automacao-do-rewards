from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

lista_palavras = [
    "abacaxi", "abacate", "abandonar", "abeia", "aberto", "abismo", "abóbora", "abordo", 
    "abstrato", "acabei", "acabou", "acaso", "acento", "aceitar", "acelerar", "acidente", "acorde", "acreditar",
    "adaptação", "adicionar","adivinha", "admirar", "adotar", "afeto", "aflito", "afogar", "agendar",
    "agente", "agitar", "alegria", "alergia", "alimento", "alvo", "amigo", "anatomia", "andar", "anel",
    "anexar", "apenas", "aperto", "aplicado", "aprender", "aproveitar", "arara", "aroma", "arranjo", "arvoré",
    "asfalto", "ascender", "atirar", "audível", "azul", "balanço", "banco", "barriga", "batata", "beijo",
    "benefício", "berço", "bilhete", "boca", "bola", "bom", "borboleta", "bravo", "broto", "bufar", "buraco",
    "cabana", "cabelo", "café", "caiu", "calma", "camisa", "caneta", "cabelo", "ceia", "celular", "cera", "cesta",
    "chegar", "cidade", "clima", "cobre", "coisa", "comida", "coração", "corrida", "couro", "criança", "crise",
    "dançar", "dente", "descanso", "desejo", "despertar", "dever", "dificuldade", "dirigir", "doar", "doente", "dor",
    "encontrar", "escolher", "esfera", "esperar", "estudar", "etapa", "fazer", "febre", "feira", "feliz", "festa",
    "fogaréu", "folha", "futuro", "galinha", "garagem", "gelo", "gesto", "girar", "globo", "golpe", "grande",
    "guitarra", "havia", "hotel", "hora", "humor", "ideal", "imagem", "início", "isso", "jacaré", "janela",
    "jogo", "juiz", "lago", "lança", "lado", "laranja", "lápis", "leitura", "lugar", "mãe", "mar", "meia",
    "mundo", "natural", "nuvem", "olhar", "olho", "pai", "pano", "parede", "pasta", "pecado", "pelo",
    "pente", "pessoa", "piano", "porta", "prato", "pular", "quadro", "quente", "querer", "rede", "regra",
    "rosa", "sabor", "sal", "sala"
]

def abrirNavegador(driver, url):
    driver.get(url)
    driver.maximize_window()

def prencherCampo(driver, xpath, dadoEntrada):
    driver.find_element(By.XPATH, xpath)
    driver.implicitly_wait(5)
    ActionChains(driver)\
        .send_keys(dadoEntrada)\
        .send_keys(Keys.ENTER)\
        .perform()

def clickCampo(driver, xpath):
    driver.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)
    
def main():
    navegador = webdriver.Chrome()
    rewards_url = "https://rewards.bing.com/"
    campo_email = '//*[@id="i0116"]'
    campo_senha = '//*[@id="i0118"]'
    campo_botao = '//*[@id="declineButton"]'
    email = ''
    senha = ''

    paginaInicial = navegador.current_window_handle

    abrirNavegador(navegador, rewards_url)
    sleep(2)
    prencherCampo(navegador, campo_email, email)
    sleep(2)
    prencherCampo(navegador, campo_senha, senha)
    sleep(2)
    clickCampo(navegador, campo_botao)
    sleep(2)
    quests = navegador.find_elements(By.CLASS_NAME, 'mee-icon-AddMedium')

    for quest in quests:
        quest.click()
        sleep(2)
        pagina = navegador.window_handles
        navegador.switch_to.window(pagina[1])
        navegador.close()
        navegador.switch_to.window(paginaInicial)
        sleep(2)
    
    for i in range(0, 35):
        navegador.switch_to.new_window("tab")
        sleep(1)
        key = lista_palavras[randint(0, len(lista_palavras)-1)]
        sleep(1)
        navegador.get(f'https://www.bing.com/search?q={key}&form=QBLH&sp=-1&ghc=1&lq=0&pq=abv&sc=11-3&qs=n&sk=&cvid=50BB67DB030845CC8E0DDD29B4DB9775&ghsh=0&ghacc=0&ghpl=')
        if i == 0:
            sleep(8)
        else:
            sleep(3)
        lista_palavras.remove(key)
        pagina = navegador.window_handles
        navegador.switch_to.window(pagina[1])
        navegador.close()
        navegador.switch_to.window(paginaInicial)
        sleep(1)

main()