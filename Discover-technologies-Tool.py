#!/usr/bin/env python
#_*_ coding: utf8 _*_

#author: Rodrigo Hernandez Carmona

from Wappalyzer import Wappalyzer,WebPage
import argparse

#parseamos para generar un panel de ayuda
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="objetivo")
parser= parser.parse_args()


#funcion principal
def main():
    if parser.target:
        #instancia de objeto Wappalyzer
        analyzer = Wappalyzer.latest()
        #abrimos la solicitud a loa pagina web que el usuario indique
        url = WebPage.new_from_url(parser.target)
        #analizamos la respuesta
        u= analyzer.analyze(url)
        
        #recorremos con for para mostrar cada tecnologia descubierta
        for i in u:
             print("\t","*********************************")
             print("\t","tecnologia detectada {}".format(i))



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt :
        print("saliendo...")
        exit() 

    

