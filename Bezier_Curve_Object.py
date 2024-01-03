import matplotlib.pyplot as plt


class BezierCurve:
    def lerp(self, a, b, t):
        return ((1-t)*a[0] + t*b[0], (1-t)*a[1] + t*b[1])

    def __init__(self, points, repeat_mode=0):
        self.points = points
        self.repeat_mode = repeat_mode
        self.t = 0

    @property
    def y(self):
        if self.repeat_mode == 1:
            return self._get_y(self.t)
        elif self.repeat_mode == 2:
            if self.t % 2 < 1:
                return self._get_y(self.t % 1)
            else:
                return self._get_y(1-self.t % 1)
        return self._get_y(self.t % 1)

    def _get_y(self, t):
        p = sorted(self.points, key=lambda x: x[0])
        while len(p) > 1:
            p = [self.lerp(a, b, t) for a, b in zip(p, p[1:])]
        return p[0]

    def _gen_pnts(self):
        return [self._get_y(x/100) for x in range(100)]

    def view(self):
        x_values, y_values = zip(*self._gen_pnts())
        plt.scatter(x_values, y_values, color='blue', label='Points')
        x_values, y_values = zip(*self.points)
        plt.scatter(x_values, y_values, color='red', label='Points')
        plt.xlabel('t')
        plt.ylabel('y')
        plt.title('Bezier')
        plt.show()


if __name__ == '__main__':
    ps = BezierCurve([(0, 0), (1, 1), (0.2, 0.5), (0.7, 0.2), (0.75, 0.7), (0.1, 2)], repeat_mode=2)
    ps.view()
