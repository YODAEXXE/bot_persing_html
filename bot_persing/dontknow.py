from bs4 import BeautifulSoup

import re

import requests

def requisição(url):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        print("connection established")
        print(resposta.text)
    else:
        print(f"request error: {resposta.status_code}")


def persing(url):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, "html.parser")
        print(soup.title.text)
    else:
        print(f"request error: {resposta.status_code}")


def achar_links(url):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, "html.parser")
        links = soup.find_all("a")
        for item in links:
            print(item.get("href"))
    else:
        print(f"request error: {resposta.status_code}")

def achar_telefone(url):
     resposta = requests.get(url)
     if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, "html.parser")
        padrao = r"\(?\d{2}\)?\s?\d{4,5}-?\d{4}"
        telefones = re.findall(padrao, resposta.text)
        print(telefones)
     else:
        print(f"request error: {resposta.status_code}")


while True:
    print("choose a option: ")
    print("---------------")
    print("to make a request type 1")
    print("---------------")
    print("for basic HTML parsing type 2")
    print("---------------")
    print("to find links in a domain type 3")
    print("---------------")
    print("to find phone numbers type 4")
    print("---------------")
    print("to exit type 0")

    opçao = input("enter an option: ").strip()

    if opçao == "0":
        print("exiting...")
        break

    if opçao not in {"1", "2", "3", "4"}:
        print("invalid option, try again.")
        continue

    URL = input("paste the URL: ")
    if not URL:
        print("invalid URL, try again.")
        continue

    if opçao == "1":
        requisição(URL)
    elif opçao == "2":
        persing(URL)
    elif opçao == "3":
        achar_links(URL)
    elif opçao == "4":
        achar_telefone(URL)
