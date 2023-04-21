import requests
from pprint import pprint as print
from Name import reply_name
space="                                                                                                                             "
def reply_answer(sura,oyat):
            try:   
                url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{sura}/{oyat}.json"
                responce = requests.get(url)
                res = responce.json()
            except TypeError:
                  return "Бундай сура ёки оят  мавжуд емас"
            result=f"{space}"
            result+=res['text']
            return  result      
