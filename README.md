# project
bcog200 spring 2024 project

**Overview** <br/>
I will be developing a mood tracker that will ask the user to log their daily emotions. The user will be asked about a hardcoded list of emotions, and to rate how strongly they felt each emotion each day. At the end of the week, the user can graph the intensity of each of the emotions over time.

**Functions** <br/>
draw_axis: Will be used to create the basics of a graph. This will use turtle to draw the lines and another function will be used to plot the data onto this graph. <br/>
plot__data(emotion): Will be used to plot a specific emotion's data onto a previously made graph using turtle. <br/>
get_values: Will be defined in the class "Emotions" and will gather data for each mood per day. <br/>

**Note** <br/>
This project would obviously require some sort of database to store user data from each day over multiple days. Ideally, I would be able to host this program on a server so that users can log in and update their data, but I simply do not have that. I am also not going to require users to run the program in the background for multiple days, so the program will be run locally and will require the user to provide all their data for the week at once.

**Note 2.0** <br/>
To better recreate the process of collecting data in the real world, this program will have separate functions for inputing data and showing data to the user. When opened, the user can choose between the two options; if they decide to input data, they can put in the information, it will be stored in a csv file on their computer, and they can close the program. If they decide they want to see a graph overview of their mood, they can select that option, view, and close the program.


