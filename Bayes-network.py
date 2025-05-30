# Priors
P_B, P_E = 0.001, 0.002
P_notB, P_notE = 1 - P_B, 1 - P_E

# Conditional Probabilities
P_A = {(1,1): 0.95, (1,0): 0.94, (0,1): 0.29, (0,0): 0.001}
P_J = {1: 0.9, 0: 0.05}
P_M = {1: 0.7, 0: 0.01}

def compute_joint_probability(b, e, a, j, m):
    pb = P_B if b else P_notB
    pe = P_E if e else P_notE
    pa = P_A[(b, e)] if a else 1 - P_A[(b, e)]
    pj = P_J[a] if j else 1 - P_J[a]
    pm = P_M[a] if m else 1 - P_M[a]
    return pb * pe * pa * pj * pm

def main():
    print("Welcome to the Burglary Alarm Joint Probability Calculator!\n")
    get = lambda q: input(q).strip().lower() == 'yes'
    b, e, a, j, m = map(get, [
        "Did a burglary occur? (yes/no): ",
        "Did an earthquake occur? (yes/no): ",
        "Did the alarm sound? (yes/no): ",
        "Did John call? (yes/no): ",
        "Did Mary call? (yes/no): "
    ])
    jp = compute_joint_probability(b, e, a, j, m)
    print(f"\nThe joint probability of the observed events is: {jp:.8f}")

if __name__ == "__main__":
    main()
