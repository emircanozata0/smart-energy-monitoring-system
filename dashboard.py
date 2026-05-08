import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import random

st.set_page_config(page_title="Smart Energy Monitoring System", layout="wide")

st.title("⚡ Smart Energy Monitoring System")

voltage_data = []
current_data = []
power_data = []
time_data = []

chart_placeholder = st.empty()

for i in range(30):

    voltage = random.randint(210, 230)
    current = round(random.uniform(0.5, 1.5), 2)
    power = round(voltage * current, 2)

    voltage_data.append(voltage)
    current_data.append(current)
    power_data.append(power)
    time_data.append(i)

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(time_data, voltage_data, label="Voltage (V)")
    ax.plot(time_data, current_data, label="Current (A)")
    ax.plot(time_data, power_data, label="Power (W)")

    ax.set_title("Real-Time Energy Monitoring")
    ax.set_xlabel("Time")
    ax.set_ylabel("Values")
    ax.legend()
    ax.grid(True)

    chart_placeholder.pyplot(fig)

    if power > 280:
        st.warning("⚠ High Power Consumption Detected!")

    time.sleep(1)