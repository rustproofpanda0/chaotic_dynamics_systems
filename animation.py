import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from lorenz_system import LorenzSystem
from rossler_system import RosslerSystem
from duffing_system import DuffingSystem


# system = LorenzSystem(sigma=10, r=28, b=8/3)
# system = RosslerSystem()
system = DuffingSystem()

time = 500
step = 0.01
n_steps = int(time / step)

x, time = system.solve(
    # xyz_0 = np.array([10., 10., 10.]),
    # xyz_0 = np.array([8.5, 7.8, 23]),
#     xyz_0 = [8.5, 7.8, 100],
    # xyz_0 = [8.5, 7.8, 23.],
    xyz_0 = [5, 5, 5],
    step=step,
    n_steps=n_steps
)



fig = plt.figure()
ax = fig.add_subplot(projection='3d')
line = ax.plot([], [], [])[0]

def update_lines(num, x, line):
    line.set_data(x[:num, :2].T)
    line.set_3d_properties(x[:num, 2])
    return line

ax.set(xlim3d=(-20, 20), xlabel='X')
ax.set(ylim3d=(-20, 20), ylabel='Y')
ax.set(zlim3d=(0, 40), zlabel='Z')

ani = animation.FuncAnimation(fig, update_lines, n_steps, fargs=(x, line),
                    interval=1)
plt.show()