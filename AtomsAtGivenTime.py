import numpy as np                
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
def plotThis(iAtoms, hLife, gMarker, gStyle, gColor, gLabel, gWidth):
    # Plot actual lines
    # -----------------
    atom = f(time, iAtoms, hLife)
    plt.plot(time, atom, marker = gMarker, color = gColor, linestyle = gStyle, label = gLabel, linewidth = gWidth, zorder = 4)

    # Plot marker at the point where the number of atoms is halved 
    # ------------------------------------------------------------
    plt.scatter(hLife, iAtoms/2, gWidth*20, color = gColor, zorder = 5)

    # Plot dash-lines that connect the point above to both axes
    # ---------------------------------------------------------
    if gWidth - 2 != 0:
        # Horizontal line
        plt.plot([xMin, hLife],[iAtoms/2, iAtoms/2], color = '#000000', linestyle = '--', linewidth = gWidth - 2, zorder = 3)
        # Vertical line
        plt.plot([hLife, hLife], [iAtoms/2, yMin], marker = 'none', color = '#000000', linestyle = '--',  linewidth = gWidth - 2, zorder = 3)
    else:
        # Horizontal line
        plt.plot([xMin, hLife],[iAtoms/2, iAtoms/2], color = '#000000', linestyle = '--', linewidth = 1, zorder = 3)
        # Vertical line
        plt.plot([hLife, hLife], [iAtoms/2, yMin], marker = 'none', color = '#000000', linestyle = '--',  linewidth = 1, zorder = 3)


# Customizations
# --------------
# X-axis
xMin = 0 
xMax = 1000
# Y-axis
yMin = 0
yMax = 500
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
INITIAL_ATOMS = 500     # Can set its value the same as xMax's


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
plotThis(INITIAL_ATOMS, 50, 'none', '-', '#4b8bbe', "Half-life = 50 years", 3)


# Plot for Half-life = 100 years
# ------------------------------
plotThis(INITIAL_ATOMS, 100, 'none', '-', '#ffd43b', "Half-life = 100 years", 3)


# Plot for Half-life = 200 years
# ------------------------------
plotThis(INITIAL_ATOMS, 200, 'none', '-', '#0bd051', "Half-life = 200 years", 3)


# Plot for Half-life = 300 years
# ------------------------------
plotThis(INITIAL_ATOMS, 300, 'none', '-', '#d00b8a', "Half-life = 300 years", 3)


# Making the Graph More Readable by Adding Labels
# -----------------------------------------------
plt.title('Number of Atoms at Any Given Time ')
plt.xlabel('Time (years)')
plt.ylabel('Number of Atoms')
plt.legend()

plt.grid()
plt.tight_layout()

plt.savefig('AtomsAtGivenTimeFig.png')

plt.show()