from bs4 import BeautifulSoup
import requests
from Course import Course

""" List of Parsed Courses """
parsed_courses = []


def get_particular_course(initial, available):
    """
    Initial   - > String (Name of the Course ex: CSE231)
    Available - > Boolean (True or False)
    """
    courses = []

    lab = initial + "L"
    for course in parsed_courses:
        if initial in course.course:
            courses.append(course)

    if available:
        for c in courses:
            if c.seat_available:
                print(c)
    else:
        for c in courses:
            print(c)


def get_cse_course(num, available):
    """
    num       - > Int (Course code ex: 311 for Cse311)
    Available - > Boolean (True or False)
    """
    cse_courses = []

    requested_course = "CSE" + str(num)
    lab = requested_course + "L"
    for course in parsed_courses:
        if requested_course in course.course:
            cse_courses.append(course)

    if available:
        for c in cse_courses:
            if c.seat_available:
                print(c)
    else:
        for c in cse_courses:
            print(c)


def get_all_course():
    for course in parsed_courses:
        print(course.course)


def parse_course(offered_list):
    for i in range(0, len(offered_list), 7):
        curr_course = Course(offered_list[i], offered_list[i + 1], offered_list[i + 2], offered_list[i + 3],
                             offered_list[i + 4], offered_list[i + 5], offered_list[i + 6])
        parsed_courses.append(curr_course)


def fetch_courses(link):
    html_text = requests.get(link).text

    soup = BeautifulSoup(html_text, 'lxml')
    tags = soup.find_all('td')

    td_list = []
    for i in tags:
        td_list.append(i.text.strip())

    parse_course(td_list)


""" Write Your Codes Here """

# Fetching the courses from the Site and Storing inside the program
fetch_courses('https://rds2.northsouth.edu/index.php/common/showofferedcourses')
# get_all_course()
get_cse_course(311, True)
# get_particular_course("MAT361", True)
