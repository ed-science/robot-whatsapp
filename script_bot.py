#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 01:51:43 2021

@author: edlinux
"""
# Importar pacotes necessãrios
from time import sleep
from whatsapp_api import WhatsApp

# Inicializar o WhatsApp
wp = WhatsApp()


# Esperar que Enter seja pressionado
input("Pressione enter após escanear o QR Code")

# Lista de nomes ou numeros de telefone a pesquisar
# IMPORTANTE: O nome não deve ser genérico pois retornará o primeiro resultado
nomes_palavras_chaves =['Teste Bot', 'Teste 2 Bot', 'Elias Bot', 'Amor']

# lista dos nomes de referência na mensagem
# primeiros_nomes = [n.split(' ') [0] for n in nomes_palavras_chaves]
primeiros_nomes = ['Teste', 'Teste', 'Elias', 'Amor']

lista_produtos = ['Big Mac', 'Melancia', 'Pêssego', 'Abacate']

# Loop para mandar mensagens 
for primeiro_nome, nome_pesquisar, produto in zip(primeiros_nomes, nomes_palavras_chaves,
                                         lista_produtos):
    
    # Pesquisar pelo contato e esperar 2 segundos antes da continuação do código
    wp.search_contact(nome_pesquisar)
    sleep(2)
    
    # Mensagem a ser enviada
    mensagem = f'Olá {primeiro_nome}! Obrigado por comprar {produto}. Este é um Teste Robot'
    
    # Enviar mensagens
    wp.send_message(mensagem)


# Esperar 10 segundos e fechar
sleep(10)
wp.driver.close()

