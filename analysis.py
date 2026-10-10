import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")
chain = (
    df[df["algorithm"] == "minimum_chain"]
    .groupby("n")[["time_s", "memory_byte"]]
    .mean()
)
print(chain)

algorithms = {
    "minimum_cycle": "MINIMUM-CYCLE-EUCLIDEAN-TSP",
    "minimum_chain": "MINIMUM-CHAIN-EUCLIDEAN-TSP",
}

quantities = {
    "time_s": ("tempo di esecuzione [s]", "tempo di esecuzione"),
    "memory_byte": ("picco di memoria [byte]", "occupazione di memoria"),
}

for nome, titolo in algorithms.items():
    sub = df[df["algorithm"] == nome]
    for colonna, (etichetta, prefisso) in quantities.items():
        g = sub.groupby("n")[colonna].mean().reset_index()

        plt.figure(figsize=(7, 5))
        plt.plot(g["n"], g[colonna], "o")
        plt.xticks(range(2, 20, 2))
        plt.xlabel("n (numero di punti)")
        plt.ylabel(etichetta)
        plt.title(f"{titolo}: {prefisso}")
        plt.grid(True, which="both")
        plt.savefig(f"{prefisso}_{nome}.png", dpi=300)

plt.show()

