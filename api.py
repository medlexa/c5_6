import requests
import json

def get_price(base,quote,amount):

    try:
        
        url = f"https://cash.rbc.ru/cash/json/converter_currency_rate/?currency_from={base}&currency_to={quote}&source=cbrf&sum={amount}&date="
        print(url)
        f = requests.get(url)
        if(f.status_code == 200):
            j = json.loads(f.content)
            return j
        else:
            return f.status_code
    
    except:
        return None


