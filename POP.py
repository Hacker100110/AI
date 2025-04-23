def apply_operator(state, op):
    return ((state - op['del_effects']) | op['add_effects'], True) if op['preconditions'].issubset(state) else (state, False)

def achieve_goal(state, goal, operators):
    return next((op for op in operators if goal in op['add_effects']), None)

def resolve_threats(plan):
    print("Checking for and resolving threats in the plan...")
    return plan

def plan_steps(init_state, goal_state, operators):
    state, plan = set(init_state), []
    print("Initial State:", state)
    for goal in goal_state:
        if goal not in state:
            op = achieve_goal(state, goal, operators)
            if op:
                print(f"Applying: {op['name']}")
                plan.append(op['name'])
                state, ok = apply_operator(state, op)
                if not ok: print("Failed to apply operator for", goal)
                print("New State:", state)
    plan = resolve_threats(plan)
    print("Final Plan (after threat resolution):", plan)

# Example usage
parse = lambda s: set(s.replace(" ", "").replace("):", ")").split(','))
init_state = parse(input("Enter initial state: "))
goal_state = parse(input("Enter goal state: "))

operators = [
    {'name': 'Move(C, A, Table)', 'preconditions': {'On(C, A)', 'Clear(C)', 'Clear(Table)'}, 'add_effects': {'On(C, Table)', 'Clear(A)'}, 'del_effects': {'On(C, A)'}},
    {'name': 'Move(B, Table, C)', 'preconditions': {'On(B, Table)', 'Clear(B)', 'Clear(C)'}, 'add_effects': {'On(B, C)', 'Clear(Table)'}, 'del_effects': {'On(B, Table)'}},
    {'name': 'Move(A, Table, B)', 'preconditions': {'On(A, Table)', 'Clear(A)', 'Clear(B)'}, 'add_effects': {'On(A, B)', 'Clear(Table)'}, 'del_effects': {'On(A, Table)'}}
]

plan_steps(init_state, goal_state, operators)
