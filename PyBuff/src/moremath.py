from math import sin, cos, tan, radians, pi

def tanPos(angle, length, pos = (0, 0)):
    flip = -1
    while angle > 90:
        angle -= 180
        flip *= -1
    while angle < -90:
        angle += 180
        flip *= -1
    adj = cos(radians(flip*angle)) * length
    opp = sin(radians(flip*angle)) * length
    return (pos[0]+adj, pos[1]+opp)