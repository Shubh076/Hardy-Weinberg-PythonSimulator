import matplotlib.pyplot as plt

"""1.BASE"""
p = 0.6 #dominant allele
q = 1 - p  #recessive allele
print(f"p (allele A) = {p}")
print(f"q (allele A) = {q}")

"""2.EQUATION"""
AA = p ** 2 #homozygous dominant
Aa = 2 * p * q #heterozygous
aa = q ** 2  #homozygous recessive

print(f"AA (homozygous dominant) = {AA:.2f}")
print(f"Aa (heterozygous) = {Aa:.2f})")
print(f"aa (homozygous recessive) = {aa:.2f}")
print(f"TOTAl = {AA + Aa + aa:.2f}")

"""3.GRAPH"""
genot = ["AA", "Aa", "aa"]
freq = [AA, Aa, aa]
colors = ["red", "green", "blue"]
plt.figure(figsize=(7, 5))
bars = plt.bar(genot, freq, color=colors)
for bar, freq in zip(bars, freq):
    plt.text(bar.get_x() + bar.get_width() / 2, freq + 0.01,
             f"{freq:.2f}", ha="center", fontweight="bold")

plt.ylim(0, 1)
plt.ylabel("Frequency")
plt.title(f"Hardy-Weinberg Equilibrium (p={p}, q={q})")
plt.tight_layout()
plt.savefig("HW_sim.png", dpi=150)
plt.show()
print("Graph saved!")