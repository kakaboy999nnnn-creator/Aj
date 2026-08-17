import math
import colorsys
import turtle

def draw_fractal_geometry():
    # إعداد شاشة الرسم
    screen = turtle.Screen()
    screen.setup(width=1000, height=1000)
    screen.bgcolor("#0a0a12")
    screen.title("Generative Sacred Geometry - AHMEDAJ")

    # إعداد القلم وتسريع الرسم
    t = turtle.Turtle()
    t.hideturtle()
    screen.tracer(0, 0)
    t.speed(0)
    t.width(1.2)

    layers = 90
    petals = 12
    points = 200

    for i in range(layers):
        # حساب التدرج اللوني النيون
        hue = (i / layers) * 1.5
        r, g, b = colorsys.hsv_to_rgb(hue % 1.0, 0.85, 1.0)
        t.pencolor(r, g, b)

        t.penup()

        for j in range(points + 1):
            angle = (j / points) * 2 * math.pi
            
            # معادلات هندسية فكتالية
            r_base = (i * 4.5) + 15
            wave1 = math.sin(petals * angle) * 50
            wave2 = math.cos(4 * angle) * 25
            r_final = r_base + wave1 + wave2

            rotation = i * 0.04
            x = r_final * math.cos(angle + rotation)
            y = r_final * math.sin(angle + rotation)

            if j == 0:
                t.goto(x, y)
                t.pendown()
            else:
                t.goto(x, y)

    screen.update()
    screen.exitonclick()

if __name__ == "__main__":
    draw_fractal_geometry()
  
