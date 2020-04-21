%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
import time
def graphique(M,cmap='cividis',):
    ax.tick_params(top=False, bottom=False, right=False, left=False, labelleft=False, labelbottom=False)
    ax.imshow(M,cmap=cmap)
    fig.canvas.draw()
fig, ax = plt.subplots(1,1)
mondes = synchronisation(35,5,270)
for m in mondes:
    graphique(m)
    time.sleep(0.5)
    


