from pyscript import display
import numpy as np
import matplotlib.pyplot as plt
import logging
import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore", message="Matplotlib is building the font cache")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
attendance = np.array([0, 0, 0, 0, 0])


def update_graph(event=None):
    from js import document

    day = document.getElementById("day").value
    absentees = document.getElementById("absentees").value.strip()

    # VALIDATION
    if absentees == "":
        display("Please enter a value", target="graph", append=False)
        return

    if not absentees.isdigit():
        display("Whole numbers only", target="graph", append=False)
        return

    absentees = int(absentees)

    if absentees < 0:
        display("Absences cannot be negative", target="graph", append=False)
        return

    # UPDATE DATA
    index = days.index(day)
    attendance[index] = absentees

    # PLOT GRAPH
    plt.clf()
    plt.plot(days, attendance, marker='o')
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Number of Absences")
    plt.grid(True)

    display(plt, target="graph", append=False)


# EXPOSE FUNCTION
import js
js.window.update_graph = update_graph
