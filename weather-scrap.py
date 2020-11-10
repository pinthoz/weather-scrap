import requests
from bs4 import BeautifulSoup


def tempoamanha(cidade):
    headers = {
        'User-Agent' : '"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"'
    }
    url = f"https://www.google.com/search?q=tempo+para+amanha in {cidade}"
    r = requests.get(url, headers=headers)
    a = BeautifulSoup(r.text, "html.parser")
    temperaturaamanha = a.find("div", class_="Ab33Nc").text #BNeawe tAd8D AP7Wnd
    return temperaturaamanha


def tempohoje(cidade):
    url = f"https://www.google.com/search?q=tempo in {cidade}"
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    temperaturahoje = s.find("div", class_="BNeawe").text 
    return temperaturahoje


while True:
    if __name__ == "__main__":
        print('---------------------------------------')
        print('--------------Meteorologia-------------')
        print('---------------------------------------')
        op = int(input("Quer saber o tempo para que dia? \nHoje   [1] \nAmanhã [2] \nOpção: "))
        if op == 1:
            cidade = str(input("Quer saber a temperatua atual de que cidade? "))
            print('---------------------------------------')
            print(f"Em {cidade} estão {tempohoje(cidade)}!!")
            print('---------------------------------------')
            continuar = (str(input('Quer saber a temperatura de mais alguma cidade? [S/N] ')))
            if continuar not in'NnSs':
                print('Erro!! A sua resposta tem de ser S/N. Por favor tente novamente.')
                break
            if continuar in 'Nn':
                break
        elif op == 2:
            cidade = str(input("Quer saber a temperatua para amanhã para que cidade? "))
            print('---------------------------------------')
            print(f"Em {cidade} amanhã vão estar {tempoamanha(cidade)[:2]}°C!!")
            print('---------------------------------------')
            continuar = (str(input('Quer saber a temperatura para amanhã para mais alguma cidade? [S/N] ')))
            if continuar not in'NnSs':
                print('Erro!! A sua resposta tem de ser S/N. Por favor tente novamente.')
                break
            if continuar in 'Nn':
                break
        else:
            print('Número inválido!!')
            break


print('---------------------------------------') 
print('Volte sempre!!')