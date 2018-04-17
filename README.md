# Root Challenge

The way I went about this problem was breaking it up into 3 parts: extracting the commands from a file, converting the commands into the appropriate objects, and outputing the object information into a file.

The first part of extracting the command was relatively easy. I just had to open the file using f.open, and use the readlines command to get an array of commands.

In the next part, I had to think of how I was going to model my data. I thought that making a Trip object, and a Driver object would make the most sense and each Driver object would have a variable number of trip objects.

The trip object would need a speed (so that way when you assign a trip to a driver, you check for whether the speed is between 5 and 100 and thus know whether to include it or not), as well as a total time and total milage so that way you can add those things to the drivers total time and total milage.

The problem description asks that for each driver, we output their name, total milage, and average speed so we include those as member variables in the driver object. In addition, we include an array of trips and total time so we can calculate average speed. We also include an add_trip function and we made it a member function since it's always going to be part of a driver object. In the add_trip function, it first checks if the speed is between 5 and 100 mph before including it, and then afterwards it appends the trip and adds that particular trips time and milage to the drivers total time and milage and recalculates the average speed the driver goes.

The brains of the operation is the compute_commands function. It goes through each command and checks if it's a Driver command (meaning it creates a new Driver object) or if it's a Trip command (meaning it creates a new Trip object). It checks if it's a Driver or Trip command by checking the first 5 or 7 letters and seeing if they match "Trip " or "Driver ". If it's a driver command and the driver hasn't been added yet (it checks using the driver_is_new helper function), then it creates a new Driver object adding the drivers name which it stripped from the command by taking the second word from the command. The new driver is then appended to the list of drivers. If it's a trip command, the start time, stop time, and total miles are extracted from the command as the 3rd, 4th, and 5th words in the command and a new Trip object is created using those parameters. Then using the name given in the trip command, we search through the list of drivers finding the driver whose name matches the trips driver name and for that particular driver, we call the add_trip function inserting the new trip object.

After all of the commands have been computed, we sort the drivers based on total miles in reverse (meaning highest to lowest).

Finally, we call the output_driver_info function which outputs the information we want, in the format we want, to the filename "output.txt". It does this by calling open on that filename with the option "w+". It goes through each driver and formats it differently based on if there are any trips (where it includes mph) or if there are no trips (where it doesn't include mph since 0 miles were traveled). It then closes the file.



To run the unit tests: navigate into the main directory (first level of root_challenge), and run "python -m unittest discover -v"
To run the code, navigate into the "root_challenge/root_challenge" directory, edit the "input.txt" file based on what you want the drivers and trips to be, run "python drive_tracking.py", and then check the "output.txt" file.
