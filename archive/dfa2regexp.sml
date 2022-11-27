

datatype RegExp = Empty
	| Atom of string (* p, not p *)
	| Concat of regexp * regexp
	| Or of regexp * regexp
	| Star of regexp 
	| Omega of regexp 

type State = int
type Dfa = {states: State list, start: State, fin: State, delta : State -> (RegExp * State) list}
(* use more lookup-friendly data structure for delta *)
type Dfa = {states: State list, start: State, fin: State, delta : State -> State -> RegExp option}

fun dfa2regexp dfa = 
	let
		
		fun rip_next_state [] = []
	      | rip_next_state [(regexp, state)] = [(regexp, state)]
	      | rip_next_state ((regexp, state) :: transitions) = 
			  if state == dfa.fin 
			     then (r_in, state) :: (rip_next_state transitions)
			  else 
			    (* get regexp *)
				SOME r_out = 
				SOME r_out = List.find (fn (_, s) => (s == dfa.fin)) (dfa.delta state) 
				
				
			  end
	in
		#0 (List.hd o rip_next_state o dfa.delta dfa.start) 
	end


while internal_states

val p = Atom "p"
val notp = Atom "!p"
val eg_always_true = Omega p
val eg_infinitely_often = Omega (Concat (Star notp, p))
val eg_oscillate_every_step = Concat (Or(Empty, p) , Omega(Concat(notp, p)))


val dfa_oscillate_every_step = {states: 3, start: 0, transition: 
	{ 0 : [(false, 1), (true, 2)], 
	  1 : [(true, 2)], 
	  2 : [(false, 1)]}, 
	accept: [1, 2]}