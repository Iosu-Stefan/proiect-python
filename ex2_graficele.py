import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv('data.csv')

df[["Calorii"]].plot(color=["orange"])
plt.title("Toate valorile")
plt.ylabel("Valori")
plt.legend(title="Parametrii")
plt.show()

df[:4].plot()
plt.title("Primele 4 valori")

plt.ylabel("Valori")
plt.legend(title="Parametrii")
plt.show()

df[-12:].plot()
plt.title("Ultimele 12 valori")
plt.ylabel("Valori")
plt.legend(title="Parametrii")
plt.show()