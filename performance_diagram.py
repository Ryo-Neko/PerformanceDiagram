import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MaxNLocator
from matplotlib.colors import BoundaryNorm


class PerformanceDiagram():
    def __init__(self):
        pod = np.arange(0, 1.01, 0.01)
        sr = np.arange(0, 1.01, 0.01)
        pod_mesh, sr_mesh = np.meshgrid(pod, sr)
        csi_mesh = csi(pod_mesh, sr_mesh)

        self.fig = plt.figure(figsize=(6, 5), dpi=150)
        self.ax = self.fig.add_subplot()
        ct = self.ax.contour(pod_mesh, sr_mesh, csi_mesh, cmap='gnuplot2', vmin=0, vmax=1, alpha=0.8, linewidths=0.6, levels=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
        ctf = self.ax.contourf(pod_mesh, sr_mesh, csi_mesh, cmap='gnuplot2', vmin=0, vmax=1, alpha=0.1, levels=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
        self.ax.clabel(ct)
        # cbar = plt.colorbar()
        # cbar.ax.set_yticklabels(np.arange(10)) 
        for bias in biaslines():
            self.ax.plot(bias[0], bias[1], color='gray', linestyle='--', linewidth=0.7)
            # print(bias[0][1], bias[1][1])
            self.ax.text(bias[0][1], bias[1][1]+0.01, f'{(bias[1][1] / bias[0][1]): .2f}', horizontalalignment='center', color='gray')
        self.ax.set_ylabel('Probability of Detection')
        self.ax.set_xlabel('Success Ratio')
        self.ax.set_aspect('equal')
        
    def _csi(self, pod, sr):
        return 1/((1/sr)+(1/pod)-1)

    def _biaslines(self, ):
        sr = [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 0.9], [0, 0.7], [0, 0.5], [0, 0.3], [0, 0.1]]
        pod = [[0, 0.1], [0, 0.3], [0, 0.5], [0, 0.7], [0, 0.9], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]
        return zip(sr, pod)

    def drawdiagram(self, itraxes, save=True):
        for i in itraxes:
            self.ax.plot(i[0], i[1], marker='o', markersize='5')
            self.ax.text(i[0]+0.01, i[1]+0.01, i[2])
            
        if save:
            self.fig.savefig('aa.png')
        else:
            self.ax.show()
            
        return self.ax
        
        
        
        
        
