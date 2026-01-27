import turtle

NUM_CIRCLES = 576
RADIUS = 100
ANGLE = 0.625
ANIMATION_SPEED = 0

turtle.speed(ANIMATION_SPEED)

for i in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)
turtle.done()
