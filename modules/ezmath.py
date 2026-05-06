def mapper(args):
    return args**2


def convert_to_f(args):
    return (args * 9 / 5) + 32


def filter_out(args):
    return args != 0


def larger(args):
    return args > 2


def positivity(args):
    return args >= 0


def uneventy(args):
    return args % 2 != 0
