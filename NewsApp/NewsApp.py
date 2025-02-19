import os
import requests
from tkinter import *
from textwrap import wrap
import requests

try:
    data = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2023-10-08&sortBy="
                        "publishedAt&apiKey=a974d5f88b904b13b16808e710fb51c4").json()
    counter = 0


    def showdata_n():
        global counter
        print(counter)
        print(f"Author : {data['articles'][counter]['author']}")
        print(f"Title : {data['articles'][counter]['title']}")
        print(f"Description : {data['articles'][counter]['description']}")
        print(f"PublishedAt : {data['articles'][counter]['publishedAt']}")
        print(f"Content : {data['articles'][counter]['content']}\n\n")
        counter += 1
        print(counter)
        print(f"Author : {data['articles'][counter]['author']}")
        print(f"Title : {data['articles'][counter]['title']}")
        print(f"Description : {data['articles'][counter]['description']}")
        print(f"PublishedAt : {data['articles'][counter]['publishedAt']}")
        print(f"Content : {data['articles'][counter]['content']}\n\n")
        counter += 1
        print(counter)
        print(f"Author : {data['articles'][counter]['author']}")
        print(f"Title : {data['articles'][counter]['title']}")
        print(f"Description : {data['articles'][counter]['description']}")
        print(f"PublishedAt : {data['articles'][counter]['publishedAt']}")
        print(f"Content : {data['articles'][counter]['content']}\n\n")
        counter += 1


    def showdata_p():
        global counter
        if counter == 0 or counter < 3:
            pass
        else:
            counter -= 1
            print(counter)
            print(f"Author : {data['articles'][counter]['author']}")
            print(f"Title : {data['articles'][counter]['title']}")
            print(f"Description : {data['articles'][counter]['description']}")
            print(f"PublishedAt : {data['articles'][counter]['publishedAt']}")
            print(f"Content : {data['articles'][counter]['content']}\n\n")
            counter -= 1
            print(counter)
            print(f"Author : {data['articles'][counter]['author']}")
            print(f"Title : {data['articles'][counter]['title']}")
            print(f"Description : {data['articles'][counter]['description']}")
            print(f"PublishedAt : {data['articles'][counter]['publishedAt']}")
            print(f"Content : {data['articles'][counter]['content']}\n\n")
            counter -= 1
            print(counter)
            print(f"Author : {data['articles'][counter]['author']}")
            print(f"Title : {data['articles'][counter]['title']}")
            print(f"Description : {data['articles'][counter]['description']}")
            print(f"PublishedAt : {data['articles'][counter]['publishedAt']}")
            print(f"Content : {data['articles'][counter]['content']}\n\n")


    showdata_n()


    def previous():
        global counter
        if counter == 0 or counter < 3:
            pass
        else:
            showdata_p()


    def next_():
        global counter
        showdata_n()


    # print(f"{data['articles'][0]['title']}")
    # for i in data['articles'][0]:
    #     print(f"{i} : {data['articles'][0][i]}")
    root = Tk()
    root.geometry("500x500")
    pre = Button(root, text="Previous", command=previous)
    pre.pack()
    nex = Button(root, text="Next", command=next_)
    nex.pack()
    root.mainloop()
except Exception as er:
    print(er)
