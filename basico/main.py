from basico_01_funcoes import montar_urls, extrair_infos
from basico_03 import inserir_dados

def main():
    url="https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int="
    lista_de_links= montar_urls(url)
    extrair=extrair_infos(lista_de_links)
    inserir_dados=inserir_dados(extrair)
    
if __name__=="__main__":
    main()