# project
bcog200 spring 2024 project

**Overview** <br/>
I will be developing a mood tracker that will ask the user to log their daily emotions. The user will firstly be asked whether they wish to input data or view data. If they choose to input data, they will be asked about a hardcoded list of emotions, and to rate how strongly they felt each emotion each day. If they choose to view data, the program will plot the intensity of each of the emotions per day, showing a week at a time.

**Functions** <br/>
main: Will call the GUI and the input_data and view_data functions based on user response.
GUI: Create tkinter object, create three screens (an opening screen, an input data screen, and a data viewing screen), and will automatically load the opening screen first. Takes root as a parameter, where root is a tkinter object.
input_data1: Will call the GUI function, load input screen, and open a csv file (will create or append depending on context). The csv file will have to be in the same folder as the python file for the program to work. Will ask user for integer data (specifically the date), store data as tuples in the csv file, and then use tkinter to close application via an on-screen button. Takes root, two labels, and two buttons as parameters, defined in GUI.
input_data2: Will call the GUI function, load input screen, and open a csv file (will create or append depending on context). The csv file will have to be in the same folder as the python file for the program to work. Will ask user for integer data (specifically the date), store data as tuples in the csv file, and then use tkinter to close application via an on-screen button. Takes root, a label, and a button as parameters, defined in input_data1.
view_data: Will call GUI function, load data viewing screen, read csv file, and plot using matplot, and close application via an on-screen button. Takes root, two labels, and two buttons as parameters, definined in GUI.

**Note** <br/>
This project would obviously require some sort of database to store user data from each day over multiple days. Ideally, I would be able to host this program on a server so that users can log in and update their data, but I simply do not have that. I am also not going to require users to run the program in the background for multiple days, so the program will be run locally and will require the user to provide all their data for the week at once.

**Note 2.0** <br/>
To better recreate the process of collecting data in the real world, this program will have separate functions for inputing data and showing data to the user. When opened, the user can choose between the two options; if they decide to input data, they can put in the information, it will be stored in a csv file on their computer, and they can close the program. If they decide they want to see a graph overview of their mood, they can select that option, view, and close the program.



