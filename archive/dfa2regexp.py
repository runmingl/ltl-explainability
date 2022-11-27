
num_states = 4
start = 0
transitions = {0 : {("!p", 1), ("p", 2)}, \
               1 : {("p", 2), ("", 3)}, \
               2 : {("!p", 1), ("", 3)}, \
               3 : set()}

adj  = [["~", "!p", "p", "~"],
        ["~",  "~", "p", ""],
        ["~", "!p", "~", ""],
        ["~", "~" , "~", "~"]]
accept = 3

def reduce_dfa():
    internal_states = set(range(num_states)) - {start, accept}
    while internal_states:
        q = internal_states.pop()
        for b, r_out in enumerate(adj[q]):
            for a, r_in in enumerate([adj[i][q] for i in range(num_states)]):
                if r_out != "~" and r_in != "~" and a != q and b != q:
                    print(a, q, b, r_in, r_out, adj[q][q], adj[a][b])
                    r = r_in
                    if adj[q][q] != "~" and adj[q][q] != "":
                        r += "(" + adj[q][q] + ")*"
                    r += r_out
                    
                    if adj[a][b] == "~":
                        adj[a][b] = r
                    else:
                        adj[a][b] = "(" + adj[a][b] + "|" + r + ")"
                    print(a, b, r_in, r_out, adj[a][b])
                    
        adj[q] = ["~"]*num_states
        for i in range(num_states):
            adj[i][q] = "~"
    print(adj[start][accept])
                
                    
                    
reduce_dfa()
            
