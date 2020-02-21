# 크롤링 라이브러리 import
import requests
from bs4 import BeautifulSoup


def today_humor() :
    # 엔터치기
    req = requests.get('http://www.todayhumor.co.kr/board/list.php?kind=search&table=humorbest&search_table_name=humorbest&keyfield=subject&keyword=%ED%9B%84%EB%B0%A9&Submit=%EA%B2%80%EC%83%89')

    # 이런 식으로 HTML에 있는 코드를 다 가져온다
    soup = BeautifulSoup(req.text, 'html.parser')

    myList = []
    myList_href = []

    for i in soup.find_all("td", class_="subject") :
        myList.append(i.text)
        myList_href.append("http://www.todayhumor.co.kr/" + i.find("a")["href"])

    return myList,myList_href


def clien():
    # 엔터치기
    req = requests.get('https://www.clien.net/service/search/board/park?sk=title&sv=%ED%9B%84%EB%B0%A9')

    # 이런 식으로 HTML에 있는 코드를 다 가져온다
    soup = BeautifulSoup(req.text, 'html.parser')

    myList = []
    myList_href = []

    for i in soup.find_all("span", class_="subject_fixed") :
        myList.append(i.text)

    for i in soup.find_all("a", class_="list_subject") :
        myList_href.append("https://www.clien.net/" + i["href"])

    return myList, myList_href