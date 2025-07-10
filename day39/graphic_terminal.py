#pip install plotext

import plotext as plt

power_levels = {
    "Goku": 9000,
    "Vegeta": 8500,
    "Frieza": 12000,
    "Piccolo": 6000,
    "Gohan": 7500
}

characters = list(power_levels.keys())
power = list(power_levels.values())

plt.title("Power Levels of Dragon Ball Z Characters")

plt.xlabel("Characters")
plt.ylabel("Power Level")

plt.bar(characters, power, label="Power Level")

plt.show()
