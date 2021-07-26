from math import sin, cos, tan, radians, pi

def tanPos(angle, length, pos = (0, 0)):
    adj = cos(radians(angle)) * length
    opp = sin(radians(angle)) * length
    return (pos[0]+adj, pos[1]+opp)