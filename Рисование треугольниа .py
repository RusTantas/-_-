import simple_draw as sd

# Нарисовать треугольник из точки (300, 300) с длиной стороны 200

#lenght = 200
#point = sd.get_point(300, 300)



# определить функцию рисования из заданной точки с заданным наклоном
def triangke(point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=4)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=200, width=4)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=200, width=4)
    v3.draw()

point_0 = sd.get_point(300, 300 )

for angel in range(0, 360, 30):
    triangke(point= point_0, angle=angel)


#triangke(point= point_0, angle=30)
#triangke(point= point_0, angle=60)
#triangke(point= point_0, angle=90)

sd.pause()
