import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

R = list(range(100, 900, 100))
I = np.array([63.2, 41.6, 31.0, 24.7, 20.5, 17.6, 15.3, 13.6]) / 1000
I_Reversed = [x ** -1 for x in I]

coefficients = np.polyfit(I_Reversed, R, 1)
k, b = coefficients

x = [0.00, max(I_Reversed)]
y = [elem * k + b for elem in x]

font_size = 28
plt.rcParams.update({'font.size': font_size})
plt.rcParams["font.family"] = "monospace"

plt.xlabel("1/I (1/А)", fontsize=font_size)
plt.ylabel("R (Ом)", fontsize=font_size)

undefined = 1/100*0.4
info = [f"\u0394I{i+1} = {round(undefined/(I[i] ** 2))} mkA" for i in range(len(I))]

plt.text(
    2, 590,
f"""\u0394I  = {round(undefined * 1000)} mА
{str(chr(10)).join(info)}"""
)


plt.xlim([-0.01, 105])
plt.plot(x, y, label="test")
plt.scatter(I_Reversed, R, color='orange')

plt.scatter([-b/k], [0], color='red', s=100)
plt.text(-b/k + 5, -30, f"Ток короткого закмыкание {round(-k/b * 1000)} мА", color='red')

t1 = plt.Polygon(
    [[I_Reversed[-2], R[-2]], [I_Reversed[-1], R[-2]], [I_Reversed[-1], R[-1]]],
    color="green", lw=1, fill=False, label="test"
)

plt.text(I_Reversed[-1] + 3, R[-2] + 30, f"ЭДС = {round(k)} В,\nr = {round(abs(b))} Ом")

plt.gca().add_patch(t1)

plt.tick_params(axis='both', which='major', labelsize=font_size)
plt.tick_params(axis='both', which='minor', labelsize=font_size-2)
plt.show()
