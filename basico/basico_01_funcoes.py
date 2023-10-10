import requests
from bs4 import BeautifulSoup

def acessar_pag(url):
    html=requests.get(url)
    bs=BeautifulSoup(html.content, "html.parser")
    http_code=html.status_code
    #print (http_code)
    #print(bs)
    return bs, http_code



def extrair_infos(lista_links):
    for link in lista_links:
        pagina=acessar_pag(link)[0]
        titulo= pagina.h1.text
        print(titulo)   


def montar_urls(url):
    radical=url
    pagina=0
    lista_links=[]
    while pagina<120:
        url_completa=radical+(str(pagina))
        pagina+=30
        lista_links.append(url_completa)
        print(url_completa)
    print(lista_links)
    return lista_links


def main():
    url="https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int="
    lista_de_links= montar_urls(url)
    extrair=extrair_infos(lista_de_links)
    #pagina= acessar_pag(url)
    #https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int=90

if __name__=="__main__":
    main()
