import unittest
from root_challenge import drive_tracking


class TestDriveTracking(unittest.TestCase):

    def test_get_commands(self):
        f = open("../root_challenge/root_challenge/input2.txt", "w+")
        f.write("Driver 1\n")
        f.write("Driver 2\n")
        f.write("Driver 3\n")
        f.close()
        lines = drive_tracking.get_commands("../root_challenge/root_challenge/input2.txt")
        self.assertTrue(len(lines) == 3)
        self.assertTrue(lines[0] == 'Driver 1')
        self.assertTrue(lines[1] == 'Driver 2')
        self.assertTrue(lines[2] == 'Driver 3')

    def test_time_in_hours(self):
        self.assertAlmostEqual(drive_tracking.time_in_hours('14:30'), 14.50)
        self.assertAlmostEqual(drive_tracking.time_in_hours('14:00'), 14.00)
        self.assertAlmostEqual(drive_tracking.time_in_hours('14:59'), 14.98333333333)
        self.assertAlmostEqual(drive_tracking.time_in_hours('01:00'), 1)

    def test_driver(self):
        driver = drive_tracking.Driver('Mark')
        self.assertTrue(driver.name == 'Mark')
        self.assertTrue(driver.trips == [])
        self.assertEqual(driver.total_miles, 0)
        self.assertEqual(driver.total_time, 0)
        self.assertEqual(driver.total_speed, 0)

    def test_trip(self):
        trip = drive_tracking.Trip(14.5, 15.0, 17.5)
        self.assertEqual(trip.total_time, 0.5)
        self.assertEqual(trip.average_speed, 17.5)
        self.assertEqual(trip.total_miles, 8.75)

    def test_add_trip(self):
        driver = drive_tracking.Driver('Mark')

        trip = drive_tracking.Trip(14.5, 15.0, 2)
        driver.add_trip(trip)
        self.assertTrue(driver.trips == [])

        trip = drive_tracking.Trip(14.5, 15.0, 101)
        driver.add_trip(trip)
        self.assertTrue(driver.trips == [])

        trip = drive_tracking.Trip(14.5, 15.0, 5)
        driver.add_trip(trip)
        self.assertEqual(len(driver.trips), 1)
        self.assertEqual(driver.total_miles, 2.5)
        self.assertEqual(driver.total_time, 0.5)
        self.assertEqual(driver.total_speed, 5)

        trip = drive_tracking.Trip(1.5, 15.0, 100)
        driver.add_trip(trip)
        self.assertEqual(len(driver.trips), 2)
        self.assertEqual(driver.total_miles, 1352.5)
        self.assertEqual(driver.total_time, 14)
        self.assertAlmostEqual(driver.total_speed, 96.607142857)

    def test_driver_is_new(self):
        self.assertTrue(drive_tracking.driver_is_new('Mark', []))
        self.assertTrue(drive_tracking.driver_is_new('Mark', [drive_tracking.Driver('Bob'),
                                                              drive_tracking.Driver('Al'),
                                                              drive_tracking.Driver('Bill')]))
        self.assertFalse(drive_tracking.driver_is_new('Mark', [drive_tracking.Driver('Mark')]))

    def test_output_driver_info(self):
        trip1 = drive_tracking.Trip(1.5, 15.0, 100)
        trip2 = drive_tracking.Trip(11.5, 15.0, 10)
        trip3 = drive_tracking.Trip(13.5, 15.0, 50)
        driver1 = drive_tracking.Driver('Mark')
        driver2 = drive_tracking.Driver('Bill')
        driver3 = drive_tracking.Driver('Jim')
        driver1.add_trip(trip1)
        driver2.add_trip(trip2)
        driver2.add_trip(trip3)
        drivers = [driver1, driver2, driver3]
        drive_tracking.output_driver_info(drivers, "../root_challenge/root_challenge/output2.txt")
        lines = drive_tracking.get_commands("../root_challenge/root_challenge/output2.txt")
        self.assertTrue(len(lines) == 3)
        self.assertTrue(lines[0] == "Mark: 1350 miles @ 100 mph")
        self.assertTrue(lines[1] == "Bill: 110 miles @ 22 mph")
        self.assertTrue(lines[2] == "Jim: 0 miles")

    def test_compute_commands(self):
        commands = drive_tracking.get_commands('../root_challenge/root_challenge/test_input.txt')
        _drivers = drive_tracking.compute_commands(commands)
        drive_tracking.output_driver_info(_drivers, "../root_challenge/root_challenge/test_output.txt")
        with open("../root_challenge/root_challenge/test_output.txt") as f:
            lines = f.readlines()
        lines = [x.strip() for x in lines]
        self.assertTrue(len(lines) == 6)
        self.assertTrue(lines[0] == "A: 22 miles @ 65 mph")
        self.assertTrue(lines[1] == "D: 17 miles @ 35 mph")
        self.assertTrue(lines[2] == "E: 4 miles @ 6 mph")
        self.assertTrue(lines[3] == "F: 1 miles @ 60 mph")
        self.assertTrue(lines[4] == "B: 0 miles")
        self.assertTrue(lines[5] == "C: 0 miles")


if __name__ == '__main__':
    unittest.main()
