from transitions.extensions import GraphMachine
from utils import *
from pool import *
import random
#from bs4 import BeautifulSoup
import requests
target_url='https://movies.yahoo.com.tw/'

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

##### is going state
    def is_going_to_state1(self, event):
        text = event.message.text
        print("state1 text: "+text.lower())
        return text.lower() == "drink"

    def is_going_to_state2(self, event):
        if event.message.text:
            text = event.message.text
            print(event.message.text) # go to state2
            print("state2 text: "+text.lower())
            return text.lower() == "food"
        else: 
            return False

    def is_going_to_state3(self, event):
        if event.message.text:
            text = event.message.text
            print(event.message.text)
            print("state3 text: "+text.lower())
            return text.lower() == "breakfast"
        else:
            return False
    
    def is_going_to_state4(self, event):
        if event.message.text:
            text = event.message.text
            print("state4 text: "+text.lower())
            return text.lower() == "lunch"
        else:
            return False

    def is_going_to_state5(self, event):
        if event.message.text:
            text = event.message.text
            print("state5 text: "+text.lower())
            return text.lower() == "dinner"
        else:
            return False
    def is_going_to_state6(self, event):
        if event.message.text:
            text = event.message.text
            print("state6 text: "+text.lower())
            return text.lower() == "coffee"
        else:
            return False
    def is_going_to_state7(self, event):
        if event.message.text:
            text = event.message.text
            print("state7 text: "+text.lower())
            return text.lower() == "tea"
        else:
            return False
    def is_going_to_state8(self, event):
        if event.message.text:
            text = event.message.text
            print("state8 text: "+text.lower())
            return text.lower() == "movie"
        else:
            return False
    def is_going_to_state9(self,event):
        if event.message.text:
            text = event.message.text
            return text.lower() == "start"
        else:
            return False

######### reply section #########
######
    def on_enter_state1(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token, "coffee or tea")
        #self.go_back()

    #def on_exit_state1(self):
        #print("Leaving state1")
######
    def on_enter_state2(self, event):
        print("I'm entering state2")
        reply_token = event.reply_token
        send_text_message(reply_token, "please choose breakfast/lunch/dinner")
        #self.go_back()

    #def on_exit_state2(self):
        #print("Leaving state2")
######
    def on_enter_state3(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        bf = ['omelet','toast','croissant','pancake','bagel','sandwish']
        ran = random.randint(0,5)
        send_text_message(reply_token, bf[ran]+'\nplease choose food or drink\nif you want to exit\nplease ignore me')
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")
######
    def on_enter_state4(self, event):
        print("I'm entering state4")
        reply_token = event.reply_token
        lun = ['steak','pizza','oyakodon','sushi','spaghtti','fried rice']
        ran = random.randint(0,5)
        send_text_message(reply_token, lun[ran]+'\nplease choose food or drink\nif you want to exit\nplease ignore me')
        self.go_back()

    def on_exit_state4(self):
        print("Leaving state4")
######
    def on_enter_state5(self, event):
        print("I'm entering state5")
        reply_token = event.reply_token
        din = ['7-11','McDonald','fried chicken','lasagna','beef noodle']
        ran = random.randint(0,4)
        send_text_message(reply_token, din[ran]+'\nplease choose food or drink\nif you want to exit\nplease ignore me')
        self.go_back()

    def on_exit_state5(self):
        print("Leaving state5")
######
    def on_enter_state6(self, event):
        print("I'm entering state6")
        reply_token = event.reply_token
        coff = ['espresso','Americano','latte','mocha','cappuccino']
        ran = random.randint(0,4)
        send_text_message(reply_token, coff[ran]+'\nplease choose food or drink\nif you want to exit\nplease ignore me')
        self.go_back()

    def on_exit_state6(self):
        print("Leaving state6")
######
    def on_enter_state7(self, event):
        print("I'm entering state7")
        reply_token = event.reply_token
        tea = ['black tea','green tea','milk tea','matcha','jasmine tea']
        ran = random.randint(0,4)
        send_text_message(reply_token, tea[ran]+'\nplease choose food or drink\nif you want to exit\nplease ignore me')
        #send_text_message(reply_token,StickerSendMessage(package_id=1, sticker_id=2))
        self.go_back()

    def on_exit_state7(self):
        print("Leaving state7")
######
    def on_enter_state8(self, event):
        print("I'm entering state8")
        reply_token = event.reply_token
        #rs=requests.session()
        #res=rs.get(target_url, verify=False)
        #res.enconding='utf-8'
        #soup=BeautifulSoup(res.text, 'html.parser')
        #context=""
        #for index, data in enumerate(soup.select('div.movielist_info h2 a')):
        #    title=data.text
        #    link=data['href']
        #    context+='{}\n{}\n'.format(title,link)
        
        #send_text_message(reply_token,context)
        self.go_back()

    def on_exit_state8(self):
        print("Leaving state8")
######
    def on_enter_state9(self, event):
        reply_token = event.reply_token
        send_template_message(reply_token,get_center_msg())
        self.go_back()

    def on_exit_state9(self):
        print("Leaving state9")
        