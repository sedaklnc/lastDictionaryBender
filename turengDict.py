import requests
from bs4 import BeautifulSoup as bs


def Turk_eng():

    general_meaning = webPage.find_all("td", {"class": "en"})
    general_eng_mean = webPage.find_all("td", {"class": "tr"})

    print(len(general_meaning))

    if len(general_meaning) < 5:
        for i in range(len(general_meaning)):
            print(general_eng_mean[i].text + " = " + general_meaning[i].text)

    else:
        for i in range(5):
            print(general_eng_mean[i].text + " = " + general_meaning[i].text)

    if len(general_meaning) == 0:
        suggest_word()


def suggest_word():
    liste = []
    print("ups! aradigin kelimeyi bulamadım acaba asagidakilerden biri mi?")
    suggest = webPage.select("ul.suggestion-list a")
    for i in suggest:
        print(i.text)
        liste.append(i.text)

    if len(liste) == 0:
        print("ne yazdın yahu oneri de bile bulunamıyorum")


def eng_Turk():

    general_meaning = webPage.find_all("td", {"class": "tr"})
    general_eng_mean = webPage.find_all("td", {"class": "en"})
    print(len(general_meaning))

    if len(general_meaning) < 5:
        for i in range(len(general_eng_mean)):
            print(general_eng_mean[i].text + "=" + general_meaning[i].text)

    else:
        for i in range(5):
            print(general_eng_mean[i].text + " = " + general_meaning[i].text)

    if len(general_meaning) == 0:
        suggest_eng_word()


def suggest_eng_word():
    list1 = []
    print("ups! I couldn't find the word could you please these words")
    suggest = webPage.select("ul.suggestion-list a")
    for i in suggest:
        print(i.text)
        list1.append(i.text)

    if len(list1) == 0:
        print("what did you write..I couldn't suggest any word")


print("**********Welcome to dictionary************")


whichLanguage = input("hangi dilden ceviri yapmak istersiniz E/T ?").upper()


if whichLanguage == "E":
    word = input("which word do you want to know meaning ? ").lower()
    url = requests.get("https://tureng.com/en/turkish-english/" + word)
    webPage = bs(url.content, "html.parser")
    eng_Turk()

else:

    word = input("hangi kelimenin anlamını öğrenmek istiyorsun ? ").lower()
    url = requests.get("https://tureng.com/en/turkish-english/" + word)
    webPage = bs(url.content, "html.parser")
    Turk_eng()
