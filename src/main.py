import fire

from ltl_regex import *
from ltl2aut import ltl_to_aut, aut_to_graph
from aut2regex import aut_to_regex
from vis import make_graph, post_process_latex
import subprocess
import os

def clean_up(filename: str):
    if os.path.exists(filename):
        os.remove(filename)


class Ltl2Regex(object):
    def ltl2regex(self, formula: str):
        return aut_to_regex(aut_to_graph(ltl_to_aut(formula)))

    def ltl2timeline(self, formula: str, filename: str = "ltl", output_format: str = "pdf"):
        g = make_graph(aut_to_regex(aut_to_graph(
            ltl_to_aut(formula))), filename, output_format)
        g.render()
        if output_format == 'latex':
            gv_file = open(f"{filename}1.gv", "w")
            tex_file = open(f"{filename}.tex", "w")
            subprocess.run(['dot2tex', '--preproc', f"{filename}.gv"], stdout=gv_file)
            subprocess.run(['dot2tex', '-tmath', f"{filename}1.gv"], stdout=tex_file)
            gv_file.close()
            tex_file.close()
            clean_up(f"{filename}.gv.pdf")
            clean_up(f"{filename}1.gv")
            post_process_latex(filename)
        print(f"Image file `{filename}` generated.")


if __name__ == '__main__':
    fire.Fire(Ltl2Regex)
