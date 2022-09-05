import numpy as np

def euclidean_alg(a, b):
    ao = abs(a)
    bo = abs(b)

    if ao > bo:
        ai = np.array([ao,bo])
    else:
        ai = np.array([bo,ao])

    qi = np.array([0])
    ri = np.array([1,0])
    si = np.array([0,1])

    i = 1
    while ai[i] != 0:
        ai = np.append(ai, ai[i-1]%ai[i])
        qi = np.append(qi, ai[i-1]//ai[i])
        if ai[i+1] != 0:
            ri = np.append(ri, ri[i-1]-ri[i]*qi[i])
            si = np.append(si, si[i-1]-si[i]*qi[i])
        i += 1

    if ao > bo:
        sol = {
            "r": ri[i-1],
            "s": si[i-1]
        }
    else:
        sol = {
            "r": si[i-1],
            "s": ri[i-1]
        }

    if a < 0:
        sol["r"]  = -sol["r"]
    if b < 0:
        sol["s"] = -sol["s"]

    return sol
