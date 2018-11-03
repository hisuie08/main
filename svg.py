from sky import Sky
s = Sky(400)
s.read_frame()
s.print_progress(1, 3)
s.read_line()
s.print_progress(2, 3)
s.read_star()
s.print_progress(3, 3)
s.print_time()
s.init_area(1, s.fs[1], s.fs[2], s.fs[3], s.fs[4], s.fs[5], s.fs[6], s.fs[7], 6)
s.draw_alpha_lines(15)
s.draw_delta_lines(10)
s.draw_constellation_lines()
s.draw_star()
s.draw_legend()
s.draw_alpha_text(15)
s.draw_delta_text(10)
s.draw_header_link(1, 0)
for k, v in s.f1.items():
    if v[0] == 1:s.draw_frame_link(k, v[1], v[3], v[4], v[6])
s.draw_frame(True, False, False, False)
s.save_img()
s.init_area(2, s.fn[1], s.fn[2], s.fn[3], s.fn[4], s.fn[5], s.fn[6], s.fn[7], 6)
s.draw_alpha_lines(15)
s.draw_delta_lines(10)
s.draw_constellation_lines()
s.draw_star()
s.draw_legend()
s.draw_alpha_text(15)
s.draw_delta_text(10)
s.draw_header_link(2, 1)
for k, v in s.f1.items():
    if v[0] == 2:s.draw_frame_link(k, v[1], v[3], v[4], v[6])
s.draw_frame(False, False, True, False)
s.save_img()
i = 0
n = len(s.f1)
for k, v in s.f1.items():
    s.init_area(k, v[1], v[2], v[3], v[4], v[5], v[6], v[7], 9)
    s.draw_alpha_lines(15)
    s.draw_delta_lines(5)
    s.draw_constellation_lines()
    s.draw_star()
    s.draw_legend()
    s.draw_alpha_text(15)
    s.draw_delta_text(5)
    s.draw_header_link(k, 2)
    for fk, fv in s.f2.items():
        if fv[0] == k:s.draw_frame_link(fk, fv[1], fv[3], fv[4], fv[6])
    s.draw_frame(True, True, True, True)
    s.save_img()
    i = i + 1
    s.print_progress(i, n)
s.print_time()
i = 0
n = len(s.f2)
for k, v in s.f2.items():
    d = abs(v[5])
    if d < 50:
        d = 1.25
    elif d < 60:
        d = 2.5
    elif d < 65:
        d = 3.75
    elif d < 75:
        d = 5
    elif d < 80:
        d = 7.5
    else:
        d = 15
    s.init_area(k, v[1], v[2], v[3], v[4], v[5], v[6], v[7], 16)
    s.draw_alpha_lines(d)
    s.draw_delta_lines(1)
    s.draw_constellation_lines()
    s.draw_star()
    s.draw_legend()
    s.draw_alpha_text(d)
    s.draw_delta_text(1)
    s.draw_header_link(k, 3)
    s.draw_frame(True, True, True, True)
    s.save_img()
    i = i + 1
    s.print_progress(i, n)
s.print_time()