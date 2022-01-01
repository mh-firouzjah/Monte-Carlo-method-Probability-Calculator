import copy
import random
from functools import reduce


class Hat:
    def __init__(self, **kwargs):
        self.contents = reduce(lambda a, b: a + b,
                               [[k] * kwargs[k] for k in kwargs.keys()])

    def draw(self, n: int):
        if n >= len(self.contents):
            random.shuffle(self.contents)
            return self.contents

        return [self.contents.pop(
                random.randint(0, len(self.contents) - 1))
                for _ in range(n)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hatset = set(hat.contents)
    hatd = {key: hat.contents.count(key) for key in hatset}
    for key in expected_balls.keys():
        if key not in hatd.keys() or hatd[key] < expected_balls[key]:
            return 0

    matched = 0
    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        fortune = new_hat.draw(num_balls_drawn)
        result = {it: fortune.count(it) for it in fortune}
        try:
            if all(result[key] >= value for key,
                   value in expected_balls.items()):
                matched += 1
        except KeyError:
            pass
    return matched / num_experiments
