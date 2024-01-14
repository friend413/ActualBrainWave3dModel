import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


N = 5000
rnd = np.random.RandomState(12345)

brain_signal = np.sin(np.linspace(0, 1000, N)) + rnd.uniform(0, 1, N)
widths = np.arange(1, N//8)
cwtmatr = signal.cwt(brain_signal, signal.ricker, widths)

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(10, 6))
axes = ax.flatten()

sns.lineplot(np.linspace(0, 1000, N), brain_signal, ax=axes[0], lw=2)
sns.heatmap(cwtmatr, cmap='Spectral', ax=axes[1])

axes[0].set_title('Brain signal')
axes[1].set_title('CWT of brain signal')

plt.tight_layout()