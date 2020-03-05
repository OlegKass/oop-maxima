class Evaluator:
    @staticmethod
    def eval(x, y):
        raise NotImplementedError



class Adder(Evaluator):
    def foo(self):
        pass
    @staticmethod
    def eval(x, y):
        return x+y


class Substractor(Evaluator):
    @staticmethod
    def eval(x, y):
        return x - y


class Multiplier(Evaluator):
    @staticmethod
    def eval(x, y):
        return x * y


class Divizer(Evaluator):
    @staticmethod
    def eval(x, y):
        return x / y

dict_of_op = {
    "+": Adder,
    "-" : Substractor,
    "*": Multiplier,
    "/" : Divizer

}