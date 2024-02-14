class Line:
    def __init__(self, slope, intercept):
        self.slope = slope
        self.intercept = intercept

    def get_y(self, x):
        return self.slope * x + self.intercept

    def move(self, delta_x):
        self.intercept += delta_x * self.slope

    def get_slope(self):
        return self.slope

    def get_intercept(self):
        return self.intercept