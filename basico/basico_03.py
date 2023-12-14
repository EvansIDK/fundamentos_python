from tinydb import TinyDB, Query


def inserir_dados(titulo, link, data, hora, numero_nota, paragrafos_so_texto):
    db=TinyDB("dados.json", indent=4,ensure_ascii=False)
    buscar=Query()
    verificar_bd=db.contains(buscar.link==link)
    if not verificar_bd:
      print("inserindo informações na base")
      db.insert({
        "titulo":titulo,
        "link":link,
        "data":data,
        "hora":hora,
        "numero_nota":numero_nota,
        "paragrafos_so_texto":paragrafos_so_texto
    })
    else:
        print("já está na base")


def main():
    from basico_01_funcoes import montar_urls, extrair_infos
    url="https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int="
    lista_de_links= montar_urls(url)
    extrair=extrair_infos(lista_de_links)
    inserir_dados=inserir_dados(extrair)
    
if __name__=="__main__":
    main()