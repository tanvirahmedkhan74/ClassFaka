from datetime import datetime, timedelta


class ClassRoom:
    map_days = {'S': "Sunday", "M": "Monday", "T": "Tuesday", "W": "Wednesday", "R": "Thursday", "A": "Saturday"}

    def __init__(self, room, day_time):
        self.room = room
        self.classTimes = {'S': [], "M": [], "T": [], "W": [], "R": [], "A": [], "F": []}

        if day_time != "TBA":
            day, time = ClassRoom.parse_day_time(day_time)

            # Convert the string to a datetime object
            # print(day_time)
            start_time_str, end_time_str = time.split('-')
            start_time = datetime.strptime(start_time_str, '%I:%M%p').time()
            end_time = datetime.strptime(end_time_str, '%I:%M%p').time()

            for d in day:
                self.classTimes[d].append([start_time, end_time])

        for day in self.classTimes:
            self.classTimes[day] = sorted(self.classTimes[day], key=lambda x: x[0])

    def add_day_times(self, day_time):
        if day_time == "TBA":
            return
        day, time = ClassRoom.parse_day_time(day_time)

        # print(day_time)
        # Convert the string to a datetime object
        start_time_str, end_time_str = time.split('-')
        start_time = datetime.strptime(start_time_str, '%I:%M%p').time()
        end_time = datetime.strptime(end_time_str, '%I:%M%p').time()

        for d in day:
            self.classTimes[d].append([start_time, end_time])

        for day in self.classTimes:
            self.classTimes[day] = sorted(self.classTimes[day], key=lambda x: x[0])

    @staticmethod
    def parse_day_time(day_time):
        day_on = True

        day = ""
        time = ""

        for i in day_time:
            if i == ' ':
                day_on = False
                continue
            if day_on:
                day += i
            else:
                time += i
        return day, time

    def get_vacant_times(self, day):
        vacant_times = []

        room = self.room
        occupied_times = self.classTimes[day]

        curr_start = datetime.strptime("8:00AM", '%I:%M%p').time()
        end_time = datetime.strptime("7:00PM", '%I:%M%p').time()

        min_vacant_time = timedelta(minutes=11)
        last_end = end_time

        if len(occupied_times) == 0:
            vacant_times.append([curr_start, end_time])
        else:
            for t in occupied_times:
                st = t[0]
                last_end = t[1]

                if datetime.combine(datetime.today(), st) - datetime.combine(datetime.today(),
                                                                             curr_start) >= min_vacant_time:
                    vacant_times.append([curr_start, st])

                curr_start = last_end

            if last_end is not None and datetime.combine(datetime.today(), end_time) - datetime.combine(datetime.today(),
                                                                                                        last_end) >= min_vacant_time:
                vacant_times.append([last_end, end_time])

        return vacant_times
