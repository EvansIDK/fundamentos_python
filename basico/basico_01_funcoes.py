import requests
import re
from basico_03 import inserir_dados
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
        notas_imprensa=pagina.find("div",attrs={"id":"content-core"}).find_all("article")
        for  nota_imprensa in notas_imprensa:
            titulo=nota_imprensa.h2.text.strip()
            link=nota_imprensa.a["href"]
            data=nota_imprensa.find_all("span", attrs={"class":"summary-view-icon"})[0].text.strip()
            hora=nota_imprensa.find_all("span", attrs={"class":"summary-view-icon"})[1].text.strip()
            numero_nota=nota_imprensa.find("span", attrs={"class":"subtitle"}).text.strip()
            numeros_inteiros = re.findall(r'\d+', numero_nota)
            numero_nota=' '.join(numeros_inteiros)
            conteudo= acessar_pag(link)[0]
            paragrafos=conteudo.find("div",attrs={"id":"content-core"}).find_all("p")
            paragrafos_so_texto=[]
            for paragrafo in paragrafos:
                info=paragrafo.text.strip()
                paragrafos_so_texto.append(info)
                #property="rnews:articleBody"
               # print(info)
            print(titulo)
            print(link)
            print(data)
            print(hora)
            print(numero_nota)
            print(paragrafos_so_texto)
            print("###")
            inserir_dados(titulo, link, data, hora, numero_nota, paragrafos_so_texto)
            #for lide in lista_lide:
             #   hora=[]

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
