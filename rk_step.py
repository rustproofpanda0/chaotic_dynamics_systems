class RKStep:
    def rk_step(self, func, x_0, t, step, *args):
        """
        func : callable
        x_0 : np.ndarray
        t : float
        step : float
        """
        k1 = func(t, x_0, args)
        k2 = func(t + step / 2, x_0 + step * 0.5 * k1, args)
        k3 = func(t + step / 2, x_0 + step * 0.5 * k2, args)
        k4 = func(t + step, x_0 + step * k3, args)
        return x_0 + (k1 + 2 * k2 + 2 * k3 + k4) * step / 6