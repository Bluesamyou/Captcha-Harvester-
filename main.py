from twocaptcha import TwoCaptcha
from time import strftime
import json
from random import randint
from datetime import  datetime, timedelta
import requests
import traceback
from bs4 import BeautifulSoup
import threading
from time import sleep
import json


class Harvestor():
    def __init__(self):



        self.S = requests.Session()


    def getSitekey(self,url=""):
        self.tokens = []

        try:
            if url == "":
                print("No URL provided to fetch sitekey, Please enter it manually")
            else:
                try:
                    sitekeyPage = self.S.get(url)

                    soup = BeautifulSoup(sitekeyPage.text, 'html.parser')

                    sitekey = soup.find('div', {'class': 'g-recaptcha'})['data-sitekey']

                    print('Sitekey found : {}'.format(sitekey))

                    return sitekey

                except Exception:

                    sitekey = input('Unable to fetch sitekey, Please enter it manually below: ')

                    while sitekey != "":
                        sitekey = input('Sitekey cannot be blank')

                    return sitekey




        except Exception :
            print('Unable to fetch Sitekey, please enter it manually')



    def startHarvestor(self, url="", apikey="", threads=2, sitekey=""):

        print(url, apikey)

        if apikey == "":
            print('Please enter a 2captcha api key')
            exit()

        if sitekey == "":
            print("Attempting to fetch Sitekey from URL provided")
            sitekey = self.getSitekey(url)

        if url =="":
            print("Please provide a URL to fetch Captcha tokens for")
            exit()

        tasks = threads


        threads = []
        count = 0

        print('Starting with apiKey : {}'.format(apikey))

        for item in range(tasks):
            t = threading.Thread(target=self.harverstor, args=(apikey,sitekey, url))
            threads.append(t)
            threads[count].start()
            sleep(2)
            count += 1

    def getToken(self):

        return (self.tokens)




    def harverstor(self, apikey,sitekey,url):

        try:

            # print(self.S.get('http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}&here=now'.format(apikey,sitekey,url)).text)
            #
            # twoCaptcha = TwoCaptcha(apikey)
            # recaptcha_token = twoCaptcha.solve_captcha(site_key=sitekey, page_url=url)

            token = {
                        "time" : datetime.now().strftime('%y %m %d %I:%M%p'),
                        "token" : randint(0,100),
                        "claimed"  : False
                    }

            self.tokens.append(token)

            with open('tokens.json', 'w') as outfile:
                json.dump(self.tokens, outfile)

            print(self.tokens)

        except Exception:

            traceback.print_exc()

            print("Unable to fetch tokens, restarting...")


            self.harverstor(url, apikey,sitekey)

    def getTokens(self):
        with open('tokens.json') as tokens:
            data = json.load(tokens)

        print(data)

        for tokens in range(len(data)):

            if datetime.now()  < datetime.strptime(data[tokens]['time'], '%y %m %d %I:%M%p') - timedelta(hours=0, minutes=1) and data[tokens]['claimed'] == False:
                token = data[tokens]['token']
                data[tokens]['claimed'] = True

                print(token)

            else:
                print('idk')







        # class GetTokens():
#
#     def recieveTokens(self,tokensArray):
#         self.tokensArray  = tokensArray
#
#     def getTokens(self):
#         print(self.tokensArray)

    #
    # checkTime = datetime.now() - timedelta(hours=0, minutes=2)
    # print(checkTime)
    #
    # print(range(len(self.tokens)))
    #
    # for tokens in range(len(self.tokens)):
    #
    #     print(self.tokens[tokens]['token'])
    #
    #     if checkTime != self.tokens[tokens]['time'] and self.tokens[tokens]['claimed'] == False:
    #         token = self.tokens[tokens]['token']
    #         self.tokens[tokens]['claimed'] = True
    #
    #         print(token)
    #
    #     else:
    #         print('idk')

