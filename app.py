from flask import Flask, jsonify, render_template
from flask_restful import Api, Resource
from bs4 import BeautifulSoup
from Course import Course
from ClassRoom import ClassRoom
from tabulate import tabulate
from datetime import datetime

app = Flask(__name__, template_folder="./templates")
api = Api(app)

# All The Course Objects
parsed_courses = []

# Room Objects dictionary
rooms = {}

saturday_vacant = []
sunday_vacant = []
monday_vacant = []
tuesday_vacant = []
wednesday_vacant = []
thursday_vacant = []


def parse_course(offered_list):
    row = {}

    for i in range(0, len(offered_list), 7):
        curr_course = Course(offered_list[i], offered_list[i + 1], offered_list[i + 2], offered_list[i + 3],
                             offered_list[i + 4], offered_list[i + 5], offered_list[i + 6])

        rooms[offered_list[i + 5]] = None
        parsed_courses.append(curr_course)


@app.route("/")
def scrap_rds():
    with open('rds2.html', 'r') as ht_file:
        content = ht_file.read()

        soup = BeautifulSoup(content, 'lxml')
        tags = soup.find_all('td')

        td_list = []
        for i in tags:
            td_list.append(i.text.strip())

        parse_course(td_list)

        # Creating ClassRoom Objects
        for r in parsed_courses:
            if rooms[r.room] is not None:
                rooms[r.room].add_day_times(r.time)
            else:
                rooms[r.room] = ClassRoom(r.room, r.time)

        # json = {}
        # for i, j in rooms.items():
        #     json[i] = 1
        # Add a button for redirecting to /vacant
    return f'<form action="/vacant"><button type="submit">View Vacant Rooms</button></form>'


@app.route('/vacant')
def get_all_vacant_room():
    map_days = {'S': "Sunday", "M": "Monday", "T": "Tuesday", "W": "Wednesday", "R": "Thursday", "A": "Saturday",
                'F': "Friday"}
    days = "ASMTWRF"

    vacant_rooms = []

    for d in days:
        for room, cls in rooms.items():
            vacs = cls.get_vacant_times(d)
            for v in vacs:
                start_time = datetime.strptime(str(v[0]), '%H:%M:%S').strftime('%I:%M %p')
                end_time = datetime.strptime(str(v[1]), '%H:%M:%S').strftime('%I:%M %p')
                vacant_rooms.append({
                    'day': map_days[d],
                    'room': room,
                    'start_time': start_time,
                    'end_time': end_time
                })

    return render_template('vacant.html', table=vacant_rooms)


if __name__ == "__main__":
    app.run(debug=True)
