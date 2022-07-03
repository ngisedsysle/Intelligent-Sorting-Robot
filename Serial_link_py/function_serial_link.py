

def f_moteur_0(deg0):
    a = -3.4
    b = 977

    return (int(a*deg0+b))

def pose_cube(deg0):
    f_moteur_0(deg0)
    return(deg0)