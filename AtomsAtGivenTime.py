import numpy as np    
from fractions import Fraction         
import matplotlib.pyplot as plt   


# //=================================================\\
# ||            +++ READ THIS FIRST +++              ||
# ||=================================================||
# || This program plot out the function:             ||
# ||                                                 ||
# ||          N = N0*e^(-lamda/t)                    ||
# ||                                                 ||
# || for lamda = ln(2)/t'                            ||
# \\=================================================// 


# Functions Used in The Program
# -----------------------------

# Function that Calculate the Number of Atoms at a Given Time
# ------------------------------------------------------------
def f(time, iAtoms, hLife):
    return iAtoms*(np.e)**( (-np.log(2)/hLife) * time)


# Function that Plot and Format the Graph 
# ---------------------------------------
def drawLine(hLife, iAtoms, gColor, gMarker, gStyle, gWidth, gLabel, gPercentage):
    # Plot actual lines
    # -----------------
    # Generate an Array of Atom Values
    atom = f(time, iAtoms, hLife)

    if gPercentage == 1:
        plt.plot(time, (atom/iAtoms)*100, color = gColor, marker = gMarker, linestyle = gStyle, linewidth = gWidth, label = gLabel, zorder = 4)
    else:
        plt.plot(time, atom, color = gColor, marker = gMarker, linestyle = gStyle, linewidth = gWidth, label = gLabel, zorder = 4)       
    

# Function that Draw a Point in Desired Location
def drawPoint(xCoord, yCoord, pColor, pSize):
    # Plot marker at the point where the number of atoms is halved 
    # ------------------------------------------------------------
    plt.scatter(xCoord, yCoord, pSize*20, color = pColor, zorder = 5)


    # Plot dash-lines that connect the point above to both axes
    # ---------------------------------------------------------
    if pSize - 2 != 0:
        # Horizontal line
        plt.plot([xMin-offset, xCoord],[yCoord, yCoord], color = '#000000', marker = 'none', linestyle = '--', linewidth = pSize - 2, zorder = 3)
        # Vertical line
        plt.plot([xCoord, xCoord], [yCoord, yMin-offset], color = '#000000', marker = 'none', linestyle = '--',  linewidth = pSize - 2, zorder = 3)
    else:
        # Horizontal line
        plt.plot([xMin-offset, xCoord],[yCoord, yCoord], color = '#000000', marker = 'none', linestyle = '--', linewidth = 1, zorder = 3)
        # Vertical line
        plt.plot([xCoord, xCoord], [yCoord, yMin-offset], color = '#000000', marker = 'none', linestyle = '--',  linewidth = 1, zorder = 3)


# Set Values
# ----------
# X-axis
xMin = 0 
xMax = int(input()) if int(input("Do you want to modify the maximum value of the x-axis? (default = 1000)\n 1) Yes\n 2) No\n => ")) == 1 else 1000
# Y-axis
yMin = 0
yMax = int(input()) if int(input("Do you want to modify the maximum value of the y-axis? (default = 100)\n 1) Yes\n 2) No\n => ")) == 1 else 100
# Offset (better to set it to 0)
offset = 0
# Axes Scale
scale = xMax/yMax
# Tick Frequency on Both Axes
xTicksFrequency = xMax/10
yTicksFrequency = yMax/10
# Figure Size
figWidth = 5
figHeight = 5
# Arrays to Store User Inputs
inHalfLife = []
inInitialAtoms = []
inColor = []
inLabel = []
# Generate an Array of Time Values for Later Use
time = np.linspace(0, xMax, num = 1000)


# Configure Output Figure
# -----------------------
fig, graph = plt.subplots(figsize=(figWidth, figHeight))
# Set Scales for Both Axes
# CAUTION:  Be careful when read the graph, the scaling will be xMax : yMax so keep that in mind, 
#           you can change the "aspect = <something_else>" or change the "scale" variable above 
#           to avoid mis-calculation
graph.set(xlim=(xMin-offset, xMax+offset), ylim=(yMin-offset, yMax+offset), aspect= scale)
# Create custom major ticks to determine position of tick labels
xTicks = np.arange(xMin, xMax+1, xTicksFrequency)
yTicks = np.arange(yMin, yMax+1, yTicksFrequency)
graph.set_xticks(xTicks)
graph.set_yticks(yTicks)


# Start Plotting Here
# -------------------
option = int(input("Choose an option:\n 1) Draw pre-made graph\n 2) Draw your own graph\n => "))

if option == 1:

    print("Option 1 chosen")
    print("\n=======================================\n")

    # Define properties for the graphs
    # Format of the followig arrays: array = [of_graph_1, of_graph_2, of_graph_3, of_graph_4]
    inHalfLife = [50.0, 100.0, 200.0, 300.0]
    inInitialAtoms = [100, 100, 100, 100]
    inColor = ['#4b8bbe', '#ffd43b', '#0bd051', '#d00b8a']
    inLabel = ["Half-life = 50 years", "Half-life = 100 years", "Half-life = 200 years", "Half-life = 300 years"]

    for i in range(4):

        # Draw the graphs from user's inputs, NOTE: This option show NUMBER 
        # drawLine Format: drawLine(hLife, iAtoms, gColor, gMarker, gStyle, gWidth, gLabel)
        graph = drawLine(inHalfLife[i], inInitialAtoms[i], inColor[i], 'none', '-', 3, inLabel[i], 0)
        # Draw a point where the initial number of atoms is havled
        # drawPoint Format: drawPoint(xCoord, yCoord, pColor, pSize)
        graph = drawPoint(inHalfLife[i], inInitialAtoms[i]/2, inColor[i], 3)  

        graph = plt.legend()

elif option == 2:

    print("Option 2 chosen")
    print("\n=======================================\n")

    num = int(input("Type in the number of functions you want to plot: "))

    # These Loops Allow User to Format Some Properties of Each Graph
    # --------------------------------------------------------------
    # Loop for half-life inputs
    for i in range(num):

        # Take in user's desired half-life as a float
        inHalfLife.append(float(input("Type in half-life of graph #" + str(i+1) + ": ")))

    print("=========")
    # Loop for initial atoms inputs
    for i in range(num):
        # Take in user's desired number of initial atoms as an integer
        inInitialAtoms.append(int(input("Type in number of initial atoms of graph #" + str(i+1) + ": ")))

    print("=========")
    # Loop for color input
    for i in range(num):
        # Take in user's desired color as a hex color format string
        inColor.append(str(input("Type in hex color format (ex: #ffffff) for graph #" + str(i+1) + ": ")))

    print("=========")
    # Loop for label inputs
    for i in range(num):
        # Take in user's desired label as a string
        inLabel.append(str(input("Type in label of graph #" + str(i+1) + ": ")))

    print("\n=======================================\n")

    option = int(input("How do you want to plot it?\n 1) The number of atoms over time\n 2) The percentage of number of atoms over time\n => "))

    if option == 1:

        print("Option 1 chosen")
        print("\n=======================================\n")

        for i in range(num):

            # Draw the graphs from user's inputs, NOTE: This option show NUMBER 
            # drawLine Format: drawLine(hLife, iAtoms, gColor, gMarker, gStyle, gWidth, gLabel)
            graph = drawLine(inHalfLife[i], inInitialAtoms[i], inColor[i], 'none', '-', 3, inLabel[i], 0)
            # Draw a point where the initial number of atoms is havled
            # drawPoint Format: drawPoint(xCoord, yCoord, pColor, pSize)
            graph = drawPoint(inHalfLife[i], inInitialAtoms[i]/2, inColor[i], 3)  
            graph = plt.legend()

    elif option == 2:

        print("Option 2 chosen")
        print("\n=======================================\n")

        for i in range(num):

            # Draw the graphs from user's inputs, NOTE: This option show PERCENTAGE 
            # drawLine Format: drawLine(hLife, iAtoms, gColor, gMarker, gStyle, gWidth, gLabel)
            graph = drawLine(inHalfLife[i], inInitialAtoms[i], inColor[i], 'none', '-', 3, inLabel[i], 1)
            # Draw a point where the initial number of atoms is havled
            # drawPoint Format: drawPoint(xCoord, yCoord, pColor, pSize)
            graph = drawPoint(inHalfLife[i], 50, inColor[i], 3)  
            graph = plt.legend()

    else:

        print("Invalid input")
        print("\n=======================================\n")
        exit()

else:

    print("Invalid input")
    print("\n=======================================\n")
    exit()


# Making the Graph More Readable by Adding Labels
# -----------------------------------------------
if option == 1:

    graph = plt.title('Number of Atoms at Any Given Time (' + str(Fraction(scale).numerator) + ':' + str(Fraction(scale).denominator) + ')')
    graph = plt.ylabel("Number of Atoms")

elif option == 2:

    graph = plt.title('Percentage of Number of Atoms at Any Given Time (' + str(Fraction(scale).numerator) + ':' + str(Fraction(scale).denominator) + ')')
    graph = plt.ylabel("Percentage of Number of Atoms (%)")

graph = plt.xlabel("Time (years)")

graph = plt.grid()
graph = plt.tight_layout()

graph = plt.savefig('AtomsAtGivenTimeFig.png')

plt.show()