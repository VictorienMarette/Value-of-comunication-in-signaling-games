import copy
from polyhedrons import canonicalize_v_rep


#ptet mieux de stocker les vertex ailleur et de garder que les index

def face_iterator(vertexes):
    faces = []
    return faces


def _face_iterator(C, V, faces):
    if len(C) == 0:
        return

    c = C[0]
    faces.append(c)

    newV = copy.deepcopy(V)


def vertex_to_poly_active(vertex):
    return ([vertex[0]], vertex[1])


def poly_active_to_active(poly_active):
    return poly_active[1]


# vraiment douteux ca
def active_to_poly_active(active, vertexes):
    V = []
    for v in vertexes:
        if v[1] >= active:
            V.append(v[0])
    V, _, _ = canonicalize_v_rep(V, [], [])
    return V
