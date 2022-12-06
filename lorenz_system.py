import numpy as np

from rk_step import RKStep


class LorenzSystem(RKStep):
    def __init__(self, sigma, r, b):
        self.sigma = sigma
        self.r = r
        self.b = b

    def __x_equation(self):
        """
        dx/dt = sigma * (y - x)
        args[0] - y
        """
        def func(t, x, args):
            return self.sigma * (args[0] - x)
        return func

    def __y_equation(self):
        """
        dy/dt = x * (r - z) - y
        args[0] - x
        args[1] - z
        """
        def func(t, y, args):
            return args[0] * (self.r - args[1]) - y
        return func

    def __z_equation(self):
        """
        dz/dt = x * y - b * z
        args[0] - x
        args[1] - y
        """
        def func(t, z, args):
            return args[0] * args[1] - self.b * z
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
                                     t, step, y0)
            y1 = self.rk_step(self.__y_equation(), y0,
                                     t, step, x0, z0)
            z1 = self.rk_step(self.__z_equation(), z0,
                                     t, step, x0, y0)
            t += step
            x0 = x1
            y0 = y1
            z0 = z1

            trajectory.append([x1, y1, z1])
            time.append(t)
        return np.array(trajectory), np.array(time)