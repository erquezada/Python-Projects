import turtle

def draw_wave(t, amplitude, wavelength, cycles):
    for _ in range(cycles):
        t.circle(amplitude, 180)
        t.circle(-amplitude, 180)

# Main script
t = turtle.Turtle()
t.speed("fastest")

draw_wave(t, amplitude=50, wavelength=100, cycles=10)

turtle.done()
