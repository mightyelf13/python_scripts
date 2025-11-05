def do_segments_intersect(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy):
    def orientation(px, py, qx, qy, rx, ry):
        val = (qy - py) * (rx - qx) - (qx - px) * (ry - qy)
        if val == 0:
            return 0
        return 1 if val > 0 else 2

    def on_line(px, py, qx, qy, rx, ry):
        return (qx <= max(px, rx) and qx >= min(px, rx) and
                qy <= max(py, ry) and qy >= min(py, ry))

    o1 = orientation(Ax, Ay, Bx, By, Cx, Cy)
    o2 = orientation(Ax, Ay, Bx, By, Dx, Dy)
    o3 = orientation(Cx, Cy, Dx, Dy, Ax, Ay)
    o4 = orientation(Cx, Cy, Dx, Dy, Bx, By)

    if (o1 != o2 and o3 != o4) or \
            (o1 == 0 and on_line(Ax, Ay, Bx, By, Cx, Cy)) or \
            (o2 == 0 and on_line(Ax, Ay, Bx, By, Dx, Dy)) or \
            (o3 == 0 and on_line(Cx, Cy, Dx, Dy, Ax, Ay)) or \
            (o4 == 0 and on_line(Cx, Cy, Dx, Dy, Bx, By)):
        return "ANO"
    else:
        return "NE"
def main():
    Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, input().split())
    result = do_segments_intersect(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy)
    print(result)
if __name__ == "__main__":
    main()