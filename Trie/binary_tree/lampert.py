import numpy as np
import math  as m


#
# Remove the comment then copy these inputs to the consol
# -------Inputs--------
# 5000, 10000, 2100
# -14600, 2500, 7000
# -0.18877
# 2278.9
# 0.17457
# -------Inputs--------
#



# -------- #
# constans #
# -------- #
mu = 398600
py = 3.14


# -------- #
# The main #
# -------- #
def lambert(r1, r2, f, g, gdot):
    r1 = np.array(r1, dtype=float)
    r2 = np.array(r2, dtype=float)
    r1_abs = np.linalg.norm(r1)
    r2_abs = np.linalg.norm(r2)
    
    delta_theta = calc_theta_propagate(r1, r2, r1_abs, r2_abs)

    v1     = (r2 - f * r1) / g
    v1_abs = np.linalg.norm(v1)

    h_vec = np.cross(r1, v1)
    h_abs = np.linalg.norm(h_vec)
    a     = 1 / (2 / r1_abs - v1_abs**2 / mu)
    e_vec = (np.cross(v1, h_vec) / mu) - (r1 / r1_abs)
    e_abs = np.linalg.norm(e_vec)

    # Inclination
    i_rad = np.arccos(h_vec[2] / h_abs) if h_abs != 0 else 0.0
    i_deg = np.degrees(i_rad)

    # RAAN
    n = np.cross([0, 0, 1], h_vec)
    n_abs = abs(n)
    if n_abs == 0:
        raan_deg = 0.0
    else:
        cos_raan = n[0] / n_abs
        cos_raan = np.clip(cos_raan, -1.0, 1.0)
        raan_rad = m.acos(cos_raan)
        if n[1] < 0:
            raan_rad = 2 * m.pi - raan_rad
        raan_deg = m.degrees(raan_rad)

    # Argument of Perigee
    omega_deg = 0.0
    if e_abs != 0 and n_abs != 0:
        cos_omega = np.dot(n, e_vec) / (n_abs * e_abs)
        cos_omega = np.clip(cos_omega, -1.0, 1.0)
        omega_rad = m.acos(cos_omega)
        cross_ne = np.cross(n, e_vec)
        sign = np.dot(cross_ne, h_vec)
        if sign < 0:
            omega_rad = 2 * m.pi - omega_rad
        omega_deg = m.degrees(omega_rad)

    # True Anomaly
    nu_deg = 0.0
    if e_abs != 0:
        cos_nu = np.dot(e_vec, r1) / (e_abs * r1_abs)
        cos_nu = np.clip(cos_nu, -1.0, 1.0)
        nu_rad = m.acos(cos_nu)
        if np.dot(r1, v1) < 0:
            nu_rad = 2 * m.pi - nu_rad
        nu_deg = m.degrees(nu_rad)

    return {
        'h'    : h_abs,
        'a'    : a,
        'e'    : e_abs,
        'i'    : i_deg,
        'RAAN' : raan_deg,
        'omega': omega_deg,
        'nu'   : nu_deg
    }



# ---------------- #
# Helper Functions #
# ---------------- #
def abs(vector):
    scale  = sum(m.pow(x, 2) for x in vector)
    return m.sqrt(scale)

def calc_theta_propagate(r1, r2, r1_abs, r2_abs):
    theta = m.acos(np.dot(r1, r2) / (r1_abs*r2_abs))
    z_dir = np.cross(r1, r2)[-1] 
    return theta if z_dir >= 0 else 360 - theta
    


def run_code():
    r1   = list(map(float, input("Enter r1 vector (comma-separated): ").split(',')))
    r2   = list(map(float, input("Enter r2 vector (comma-separated): ").split(',')))
    f    = float(input("Enter value for f: "))
    g    = float(input("Enter value for g: "))
    gdot = float(input("Enter value for gdot: "))

    elements = lambert(r1, r2, f, g, gdot)
    
    print("\nOrbital Elements:")
    for key, value in elements.items():
        print(f"{key}: {value:.6f}")



if __name__ == '__main__':
    run_code()


