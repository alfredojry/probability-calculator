import copy
import random
# Consider using the modules imported above.

class Hat(object):

    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            self.contents += [k] * v

    def draw(self, n):
        if n > len(self.contents):
            return self.contents
        else:
            index_list = []
            balls = []
            for i in range(n):
                x = random.randrange(len(self.contents))
                balls.append(self.contents[x])
                self.contents = self.contents[:x] + self.contents[x + 1:]
            return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for i in range(num_experiments):
        copied_hat = copy.deepcopy(hat)
        drawn_balls = copied_hat.draw(num_balls_drawn)
        flag_fav = True
        for k, v in expected_balls.items():
            if drawn_balls.count(k) < v:
                flag_fav = False
        if flag_fav:
            M += 1
    return M / num_experiments

