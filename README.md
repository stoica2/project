# project
bcog200 spring 2024 project

**Overview** __
I will be developing a mood tracker that will ask the user to log their daily emotions. The user will be asked about a hardcoded list of emotions, and to rate how strongly they felt each emotion each day. At the end of the week, the user can graph the intensity of each of the emotions over time.

**Functions** __
draw_axis: Will be used to create the basics of a graph. This will use turtle to draw the lines and another function will be used to plot the data onto this graph.
plot__data(emotion): Will be used to plot a specific emotion's data onto a previously made graph using turtle.
get_values: Will be defined in the class "Emotions" and will gather data for each mood per day.

**Note** __
This project would obviously require some sort of database to store user data from each day over multiple days. Ideally, I would be able to host this program on a server so that users can log in and update their data, but I simply do not have that. I am also not going to require users to run the program in the background for multiple days, so the program will be run locally and will require the user to provide all their data for the week at once.


