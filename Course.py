class Course:
    def __init__(self, index, course, section, faculty, time, room, seats):
        self.index = index
        self.course = course
        self.section = section
        self.faculty = faculty
        self.time = time
        self.room = room
        self.seats = seats

        if int(self.seats) > 0:
            self.seat_available = True
        else:
            self.seat_available = False

    def __str__(self):
        return f"{self.index} -> \nCourse : {self.course}  --  Section: {self.section}\nTime: {self.time}\nSeats: {self.seats}\nFaculty: {self.faculty}  --  Room: {self.room} \n"
