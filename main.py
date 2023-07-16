from bs4 import BeautifulSoup
import requests

from Course import Course

parsed_courses = []


def available_course():
    for c in parsed_courses:
        if c.seat_available:
            print(c)


def parse_course(offered_list):
    row = {}

    for i in range(0, len(offered_list), 7):
        curr_course = Course(offered_list[i], offered_list[i+1], offered_list[i+2], offered_list[i+3], offered_list[i+4], offered_list[i+5], offered_list[i+6])

        # print(offered_list[i])
        # row["Index"] = offered_list[i]
        # row["Course"] = offered_list[i + 1]
        # row["Section"] = offered_list[i + 2]
        # row["Faculty"] = offered_list[i + 3]
        # row["Time"] = offered_list[i + 4]
        # row["Room"] = offered_list[i + 5]
        # row["Seats"] = offered_list[i + 6]
        parsed_courses.append(curr_course)
        row = {}


with open('home.html', 'r') as ht_file:
    content = ht_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('td')

    td_list = []
    for i in tags:
        td_list.append(i.text.strip())

    parse_course(td_list)

    # for course in parsed_courses:
    #     print(course)
    available_course()
