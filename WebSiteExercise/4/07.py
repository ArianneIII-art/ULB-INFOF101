def rac_eq_2nd_deg(a: int, b: int, c: int) -> tuple:
    delta = b**2 - 4*a*c
    if delta < 0:
        return ()
    elif delta == 0:
        return (-b/2*a,)
    else:
        if a == 1:
            return ((-b-delta**0.5)/(2*a), (-b+delta**0.5)/(2*a),)
        else:
            return ((-b+delta**0.5)/(2*a), (-b-delta**0.5)/(2*a),)