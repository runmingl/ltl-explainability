from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class Regex:
    def __str__(self) -> str:
        return regex_to_string(self)

    def __len__(self) -> int:
        return regex_tllen(self)


@dataclass(eq=True, frozen=True)
class Epsilon(Regex):
    pass


@dataclass(eq=True, frozen=True)
class Empty(Regex):
    pass


@dataclass(eq=True, frozen=True)
class Symbol(Regex):
    symbol: str


@dataclass(eq=True, frozen=True)
class Concat(Regex):
    left: Regex
    right: Regex


@dataclass(eq=True, frozen=True)
class Union(Regex):
    left: Regex
    right: Regex


@dataclass(eq=True, frozen=True)
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
            raise Typeerror(f'Unknown regex type: {type(regex)}')

def regex_tllen(regex: Regex) -> int:
    # currently returns timeline length of regex
    match regex:
        case Epsilon():
            return 0
        case Empty():
            return -1
        case Symbol(s):
            return 1
        case Concat(r1, r2):
            return regex_tllen(r1) + regex_tllen(r2)
        case Union(r1, r2):
            return max(regex_tllen(r1), regex_tllen(r2))
        case Star(r):
            return 2 * regex_tllen(r) + 1
        case _:
            raise TypeError(f'Unknown regex type: {type(regex)}')


@dataclass(eq=True, frozen=True)
class OmegaRegex:
    def __str__(self) -> str:
        return omega_regex_to_string(self)
    def __len__(self) -> int:
        return omega_regex_tllen(self)

@dataclass(eq=True, frozen=True)
class Repeat(OmegaRegex):
    regex: Regex


@dataclass(eq=True, frozen=True)
class ConcatOmega(OmegaRegex):
    left: Regex
    right: OmegaRegex


@dataclass(eq=True, frozen=True)
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


def omega_regex_tllen(omega_regex: OmegaRegex) -> int:
    match omega_regex:
        case Repeat(r):
            return regex_tllen(r)
        case ConcatOmega(r1, r2):
            return regex_tllen(r1) + omega_regex_tllen(r2)
        case UnionOmega(r1, r2):
            return max(omega_regex_tllen(r1), omega_regex_tllen(r2))
        case _:
            raise TypeError(f'Unknown omega regex type: {type(omega_regex)}')
