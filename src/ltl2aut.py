import spot

from dataclasses import dataclass, field
from typing import List, Dict, Set
from ltl_regex import *


@dataclass(eq=True)
class Edge:
    src: int
    dst: int
    label: Regex


@dataclass(eq=True)
class Vertex:
    number: int
    out_edges: List[Edge] = field(default_factory=list)
    in_edges: List[Edge] = field(default_factory=list)


@dataclass
class Graph:
    num_states: int
    initial_state: int
    final_states: Set[int] = field(default_factory=set)
    vertices: Dict[int, Vertex] = field(default_factory=dict)

    def __init__(self, num_states: int, initial_state: int):
        self.num_states = num_states
        self.initial_state = initial_state
        self.final_states = set()
        self.vertices = {i: Vertex(i) for i in range(num_states)}

    def get_init(self) -> Vertex:
        return self.vertices[self.initial_state]

    def get_finals(self) -> List[Vertex]:
        return [self.vertices[v] for v in self.final_states]

    def get_vertex(self, v: int) -> Vertex:
        return self.vertices[v]

    def add_edge(self, src: int, dst: int, label: Regex):
        e = Edge(src, dst, label)
        self.vertices[src].out_edges.append(e)
        self.vertices[dst].in_edges.append(e)


def ltl_to_aut(ltl_formula: str):
    return spot.automaton(spot.translate(ltl_formula, 'buchi', 'sbacc').to_str('spin'))


def aut_to_graph(aut):
    assert aut.num_sets() == 1
    bdict = aut.get_dict()
    graph = Graph(aut.num_states(), aut.get_init_state_number())
    for s in range(graph.num_states):
        for t in aut.out(s):
            graph.add_edge(t.src, t.dst, Symbol(
                spot.bdd_format_formula(bdict, t.cond)))
            if t.acc.is_singleton():
                graph.final_states.add(t.src)

    return graph
