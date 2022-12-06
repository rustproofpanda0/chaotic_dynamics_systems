import numpy as np

from rk_step import RKStep


class RosslerSystem(RKStep):
    def __init__(self, a=0.2, b=0.2, c=5.7):
        self.a = a
        self.b = b
        self.c = c

    def __x_equation(self):
        """
        dx/dt = -y - z
        args[0] - y
        args[1] - z
        """
        def func(t, x, args):
            return -args[0] - args[1]
        return func

    def __y_equation(self):
        """
        dy/dt = x + a * y
        args[0] - x
        """
        def func(t, y, args):
            return args[0] + self.a * y
        return func

    def __z_equation(self):
        """
        dz/dt = b + z * (x - c)
        args[0] - x
        """
        def func(t, z, args):
            return self.b + z * (args[0] - self.c)
        return func

    def solve(self, xyz_0, step, n_steps):
        x0 = xyz_0[0]
        y0 = xyz_0[1]
        z0 = xyz_0[2]
        trajectory = [xyz_0]
        t = 0
        time = [t]

        for _ in range(n_steps):
            x1 = self.rk_step(self.__x_equation(), x0,
                                     t, step, y0, z0)
            y1 = self.rk_step(self.__y_equation(), y0,
                                     t, step, x0)
            z1 = self.rk_step(self.__z_equation(), z0,
                                     t, step, x0)
            t += step
            x0 = x1
            y0 = y1
            z0 = z1

            trajectory.append([x1, y1, z1])
            time.append(t)
        return np.array(trajectory), np.array(time)