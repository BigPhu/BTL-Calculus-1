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


# Function that Calculate the Number of Atoms at a Given Time
# ------------------------------------------------------------
def f(time, iAtoms, hLife):
    return iAtoms*(np.e)**( (-np.log(2)/hLife) * time)


# Function that Plot and Format the Graph 
# ---------------------------------------
def drawLine(hLife, iAtoms, gColor, gMarker, gStyle, gWidth, gLabel):
    # Plot actual lines
    # -----------------
    atom = f(time, iAtoms, hLife)
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
        plt.plot([xMin, xCoord],[yCoord, yCoord], color = '#000000', marker = 'none', linestyle = '--', linewidth = pSize - 2, zorder = 3)
        # Vertical line
        plt.plot([xCoord, xCoord], [yCoord, yMin], color = '#000000', marker = 'none', linestyle = '--',  linewidth = pSize - 2, zorder = 3)
    else:
        # Horizontal line
        plt.plot([xMin, xCoord],[yCoord, yCoord], color = '#000000', marker = 'none', linestyle = '--', linewidth = 1, zorder = 3)
        # Vertical line
        plt.plot([xCoord, xCoord], [yCoord, yMin], color = '#000000', marker = 'none', linestyle = '--',  linewidth = 1, zorder = 3)


# Customizations
# --------------
# X-axis
xMin = 0 
xMax = 1000
# Y-axis
yMin = 0
yMax = 100
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


# Set Values
# ----------
time = np.linspace(0, xMax, num = 1000)
INITIAL_ATOMS = 100     # Can set its value the same as xMax's


# Configure Output Graph
# ----------------------
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
# Plot for Half-life = 50 years
# -----------------------------
# drawLine Format: drawLine(hLife, iAtoms, gColor, gMarker, gStyle, gWidth, gLabel)
drawLine(50, INITIAL_ATOMS, '#4b8bbe', 'none', '-', 3, "Half-life = 50 years")
# drawPoint Format: drawPoint(xCoord, yCoord, pColor, pSize)
drawPoint(50, INITIAL_ATOMS/2, '#4b8bbe', 3)


# Plot for Half-life = 100 years
# ------------------------------
# drawLine Format: drawLine(hLife, iAtoms, gColor, gMarker, gStyle, gWidth, gLabel)
drawLine(100, INITIAL_ATOMS, '#ffd43b', 'none', '-', 3, "Half-life = 100 years")
# drawPoint Format: drawPoint(xCoord, yCoord, pColor, pSize)
drawPoint(100, INITIAL_ATOMS/2, '#ffd43b', 3)


# Plot for Half-life = 200 years
# ------------------------------
# drawLine Format: drawLine(hLife, iAtoms, gColor, gMarker, gStyle, gWidth, gLabel)
drawLine(200, INITIAL_ATOMS, '#0bd051', 'none', '-', 3, "Half-life = 200 years")
# drawPoint Format: drawPoint(xCoord, yCoord, pColor, pSize)
drawPoint(200, INITIAL_ATOMS/2, '#0bd051', 3)


# Plot for Half-life = 300 years
# ------------------------------
# drawLine Format: drawLine(hLife, iAtoms, gColor, gMarker, gStyle, gWidth, gLabel)
drawLine(300, INITIAL_ATOMS, '#d00b8a', 'none', '-', 3, "Half-life = 300 years")
# drawPoint Format: drawPoint(xCoord, yCoord, pColor, pSize)
drawPoint(300, INITIAL_ATOMS/2, '#d00b8a', 3)


# Making the Graph More Readable by Adding Labels
# -----------------------------------------------
plt.title('Number of Atoms at Any Given Time (' + str(Fraction(scale).numerator) + ':' + str(Fraction(scale).denominator) + ')')
plt.xlabel('Time (years)')
plt.ylabel('Number of Atoms')
plt.legend()

plt.grid()
plt.tight_layout()

plt.savefig('AtomsAtGivenTimeFig.png')

plt.show()