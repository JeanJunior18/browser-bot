from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.msg = "Mensagem automática testando Bot, ignora aí"
        self.remet = ['Srta. Beatriz', 'Leandro', 'José Lucas']
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome()
        

    def SendMsg(self, rept):

        url = 'https://gshow.globo.com/realities/bbb/bbb20/votacao/paredao-bbb20-quem-voce-quer-eliminar-felipe-manu-ou-mari-a9f49f90-84e2-4c12-a9af-b262e2dd5be4.ghtml'
        
        self.driver.get(url)
        
        input('Autentique-se e pressione qualquer tecla para iniciar')
        print('Iniciando...')
        i = 0

        while i<rept:
            person = self.driver.find_element_by_class_name('_3XS4Y0WYa0gelPf1sxIlOX')
            time.sleep(1)
            person.click()

            print('Responda o captcha!!')
            time.sleep(10)
            print('Continuando...')

            again = self.driver.find_element_by_class_name('_2AF5RKGBZOsC82NsV8onjb')
            time.sleep(1)
            again.click()

            i = i+1

        print('Finally')

bot = WhatsappBot()
num = int(input('Repetir quantas vezes? '))
bot.SendMsg(num)
