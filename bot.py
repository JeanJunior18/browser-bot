from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.msg = "Mensagem automática testando Bot, ignora aí"
        self.remet = ['Srta. Beatriz', 'Leandro', 'José Lucas']
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome()
        

    def SendMsg(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(10)
        for rmt in self.remet:
            person = self.driver.find_element_by_xpath(f"//span[@title='{rmt}']")
            time.sleep(3)
            person.click()
            chat = self.driver.find_element_by_class_name('_1Plpp')
            time.sleep(3)
            chat.click()
            chat.send_keys(self.msg)
            sendmsg = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            sendmsg.click()
            time.sleep(3)
        print('Finally')

bot = WhatsappBot()
bot.SendMsg()
