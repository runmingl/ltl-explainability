from dataclasses import dataclass


@dataclass
class Regex:
    def __str__(self) -> str:
        return regex_to_string(self)


@dataclass(eq=True)
class Epsilon(Regex):
    pass


@dataclass(eq=True)
class Empty(Regex):
    pass


@dataclass(eq=True)
class Symbol(Regex):
    symbol: str


@dataclass(eq=True)
class Concat(Regex):
    left: Regex
    right: Regex


@dataclass(eq=True)
class Union(Regex):
    left: Regex
    right: Regex


@dataclass(eq=True)
class Star(Regex):
    regex: Regex


def regex_to_string(regex: Regex) -> str:
    match regex:
        case Epsilon():
            return 'ε'
        case Empty():
            return '∅'
        case Symbol(s):
            return f'({s})'
        case Concat(r1, r2):
            return f'({regex_to_string(r1)}{regex_to_string(r2)})'
        case Union(r1, r2):
            return f'({regex_to_string(r1)}|{regex_to_string(r2)})'
        case Star(r):
            return f'({regex_to_string(r)})*'
        case _:
            raise TypeError(f'Unknown regex type: {type(regex)}')


@dataclass
class OmegaRegex:
    def __str__(self) -> str:
        return omega_regex_to_string(self)


@dataclass(eq=True)
class Repeat(OmegaRegex):
    regex: Regex


@dataclass(eq=True)
class ConcatOmega(OmegaRegex):
    left: Regex
    right: OmegaRegex


@dataclass(eq=True)
class UnionOmega(OmegaRegex):
    left: OmegaRegex
    right: OmegaRegex


def omega_regex_to_string(omega_regex: OmegaRegex) -> str:
    match omega_regex:
        case Repeat(r):
            return f'({regex_to_string(r)})w'
        case ConcatOmega(r1, r2):
            return f'({regex_to_string(r1)}{omega_regex_to_string(r2)})'
        case UnionOmega(r1, r2):
            return f'({omega_regex_to_string(r1)}|{omega_regex_to_string(r2)})'
        case _:
            raise TypeError(f'Unknown omega regex type: {type(omega_regex)}')
