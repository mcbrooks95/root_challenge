class Trip:
    def __init__(self, start_time, stop_time, average_speed):
        self.average_speed = average_speed
        self.total_time = stop_time - start_time
        self.total_miles = self.total_time * average_speed


class Driver:
    def __init__(self, name):
        self.name = name
        self.trips = []
        self.total_miles = 0
        self.total_time = 0
        self.total_speed = 0

    def add_trip(self, trip):
        if 5 <= trip.average_speed <= 100:
            self.trips.append(trip)
            self.total_miles += trip.total_miles
            self.total_time += trip.total_time
            self.total_speed = self.total_miles / self.total_time


def get_commands(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    return lines


def time_in_hours(time):
    hours = float(time.split(':')[0])
    minutes = float(time.split(':')[1])
    time_total = hours + (minutes / 60)
    return time_total


def driver_is_new(driver_name, drivers):
    for driver in drivers:
        if driver.name == driver_name:
            return False
    return True


def compute_commands(commands):
    drivers = []
    for c in commands:
        driver_name = c.split(' ')[1]
        if c[0:7] == "Driver " and driver_is_new(driver_name, drivers):
            driver = Driver(driver_name)
            drivers.append(driver)
        elif c[0:5] == "Trip ":
            start_time = time_in_hours(c.split(' ')[2])
            stop_time = time_in_hours(c.split(' ')[3])
            total_miles = float(c.split(' ')[4])
            speed = total_miles / (stop_time - start_time)
            trip = Trip(start_time, stop_time, speed)
            for driver in drivers:
                if driver.name == driver_name:
                    driver.add_trip(trip)
    drivers.sort(key=lambda x: x.total_miles, reverse=True)
    return drivers


def output_driver_info(drivers, filename):
    f = open(filename, "w+")
    for driver in drivers:
        if driver.trips:
            f.write(driver.name + ': ' + str(int(round(driver.total_miles))) +
                    ' miles @ ' + str(int(round(driver.total_speed))) + ' mph\n')
        else:
            f.write(driver.name + ': 0 miles\n')
    f.close()


def main():
    commands = get_commands('input.txt')
    drivers = compute_commands(commands)
    output_driver_info(drivers, 'output.txt')


if __name__ == "__main__":
    main()
