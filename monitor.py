import random
import csv
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

voltage_data = []
current_data = []
power_data = []
x_data = []

counter = 0

csv_file = "energy_data.csv"

if not os.path.exists(csv_file):
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Voltage", "Current", "Power"])

def generate_data():
    voltage = random.randint(210, 230)
    current = round(random.uniform(0.5, 1.5), 2)
    power = round(voltage * current, 2)
    return voltage, current, power

def update(frame):
    global counter

    voltage, current, power = generate_data()

    x_data.append(counter)
    voltage_data.append(voltage)
    current_data.append(current)
    power_data.append(power)

    counter += 1

    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([counter, voltage, current, power])

    if len(x_data) > 20:
        x_data.pop(0)
        voltage_data.pop(0)
        current_data.pop(0)
        power_data.pop(0)

    plt.cla()

    plt.plot(x_data, voltage_data, label="Voltage (V)")
    plt.plot(x_data, current_data, label="Current (A)")
    plt.plot(x_data, power_data, label="Power (W)")

    plt.xlabel("Time (s)")
    plt.ylabel("Value")
    plt.title("Smart Energy Monitoring System")
    plt.legend()
    plt.grid(True)

ani = FuncAnimation(plt.gcf(), update, interval=1000, cache_frame_data=False)

plt.tight_layout()
plt.show(block=True)