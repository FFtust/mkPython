

class led_c():

    def __init__(self):
        request("2eacefd9a69c9d858e68ad3e94691bf9", ())

    def show_all(self, r, g, b, percentage):
        request("1cbdb2953d92c3e10c8e2deeda188cee", ( r, g, b, percentage))

    def show_single(self, index, r, g, b):
        request("a581882c591598190744c5a2966554cd", ( index, r, g, b))

    def move(self, offset):
        request("3734a903022249b3010be1897042568e", ( offset))

    def off_single(self, led_id):
        request("44c010a12ca2d7f2c4dbef562e4aafe2", ( led_id))

    def off_all(self):
        request("317dc2aa04b0f93ef2d4cc071ad0a4de", ())

    def clear(self):
        request("01bc6f8efa4202821e95f4fdf6298b30", ())

    def show_ring(self, color, offset = 0):
        request("33c7c3da13b8092ea0aba22a8c5b3820", ( color, offset = 0))

    def ring_graph(self, pct):
        request("12b28ad7db42f18ac72cf391943d710b", ( pct))

    def show_animation(self, name, wait = True):
        request("14e116547c19444be327cb603ba4c4cc", ( name, wait = True))

    def show_full_color(self, data, offset = 0):
        request("978e3bbc7af8d29a108cb3b121d18c97", ( data, offset = 0))



class button_c():

    def __init__(self):
        request("2eacefd9a69c9d858e68ad3e94691bf9", ())

    def is_pressed(self, index = 0):
        return get_value("53826c458e60223a09b69fa64eb8d251", ( index = 0))


led = ledc()
button = button_c()