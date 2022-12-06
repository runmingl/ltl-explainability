import copy

from typing import List, Tuple, Optional
from ltl_regex import *
from ltl2aut import *
from util import simplify


def find_path(g: Graph, v_start: int, v_end: int) -> Optional[Regex]:
    g = copy.deepcopy(g)
    v_rip = find_rip_vertex(g, v_start, v_end)
    while v_rip is not None:
        rip(g, v_rip)
        g = combine_duplicate_edge(g)
        v_rip = find_rip_vertex(g, v_start, v_end)
    r1 = None
    r2 = None
    for e in g.vertices[v_start].out_edges:
        if e.dst == v_start:
            r1 = e.label
        if e.dst == v_end:
            r2 = e.label
    r3 = None
    r4 = None
    for e in g.vertices[v_end].out_edges:
        if e.dst == v_start:
            r3 = e.label
        if e.dst == v_end:
            r4 = e.label
    if r2 is None:
        return None
    if v_start == v_end:
        return r2
    return combine_final(r1, r2, r3, r4)


def combine_final(r1: Optional[Regex], r2: Regex, r3: Optional[Regex], r4: Optional[Regex]) -> Regex:
    if r1 is None:
        return r2
    return Concat(Star(r1), r2)


def find_rip_vertex(g: Graph, v_start: int, v_end: int) -> Optional[int]:
    for v in g.vertices.keys():
        if v != v_start and v != v_end:
            return v
    return None


def contain_self_loop(g: Graph, v: int) -> Optional[Edge]:
    for e in g.vertices[v].out_edges:
        if e.src == e.dst:
            return e
    return None


def rip(g: Graph, v_rip: int):
    loop = contain_self_loop(g, v_rip)
    r_rip = loop.label if loop is not None else None
    added_edges: List[Tuple[int, int, Regex]] = []
    for e_in in g.vertices[v_rip].in_edges:
        for e_out in g.vertices[v_rip].out_edges:
            if e_in.src == v_rip or e_out.dst == v_rip:
                continue
            r_in = e_in.label
            r_out = e_out.label
            r = Concat(r_in, r_out) if r_rip is None else Concat(
                r_in, Concat(Star(r_rip), r_out))
            added_edges.append((e_in.src, e_out.dst, r))
    for e_in in g.vertices[v_rip].in_edges:
        g.vertices[e_in.src].out_edges.remove(e_in)
    for e_out in g.vertices[v_rip].out_edges:
        g.vertices[e_out.dst].in_edges.remove(e_out)
    for s, t, r in added_edges:
        g.add_edge(s, t, r)
    del g.vertices[v_rip]
    g.num_states -= 1


@simplify
def aut_to_regex(g: Graph) -> Optional[OmegaRegex]:
    g = combine_duplicate_edge(g)
    # g = add_episilon_final_state(g)
    all_paths: List[OmegaRegex] = []
    for f in g.final_states:
        path1 = find_path(g, g.initial_state, f)
        path2 = find_path(g, f, f)
        if path1 is not None and path2 is not None:
            all_paths.append(ConcatOmega(path1, Repeat(path2)))
    if len(all_paths) == 0:
        return None
    p = all_paths[0]
    for i in range(1, len(all_paths)):
        p = UnionOmega(p, all_paths[i])
    return p


def combine_duplicate_edge(g: Graph) -> Graph:
    def combine_one_duplicate_edge(g: Graph) -> bool:
        for v in g.vertices.values():
            for e1 in v.out_edges:
                for e2 in v.out_edges:
                    if e1 != e2 and e1.dst == e2.dst:
                        g.vertices[e1.dst].in_edges.remove(e1)
                        g.vertices[e1.dst].in_edges.remove(e2)
                        e1.label = Union(e1.label, e2.label)
                        v.out_edges.remove(e2)
                        g.vertices[e1.dst].in_edges.append(e1)
                        return True
        return False

    while combine_one_duplicate_edge(g):
        pass
    return g


def add_episilon_final_state(g: Graph) -> Graph:
    g.num_states += 1
    v = g.num_states
    g.vertices[v] = Vertex(v)
    for f in g.final_states:
        g.add_edge(f, v, Epsilon())
        g.add_edge(v, f, Epsilon())
    g.final_states = {v}
    return g
