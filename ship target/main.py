import pgzrun
import random 
import itertools

HEIGHT = 500
WIDTH = 500

block = Actor("block",center=(50,50))
ship = Actor("ship",center=(250,250))

BLOCK_POSITIONS = [(450,50),(450,450),(50,450),(50,50)]
block_positions=itertools.cycle(BLOCK_POSITIONS) 

def move_block():
    animate(block,"bounce_end",duration=1,pos=next(block_positions))


move_block()
clock.schedule_interval(move_block,2)

def next_ship_target():
    x=random.randint(100,400)
    y=random.randint(100,400)
    ship.target=x,y
    target_angle=ship.angle_to(ship.target)
    target_angle += 360*((ship.angle-target_angle+180)//360)
    animate(ship,angle=target_angle,duration=0.3,on_finished=move_ship)

def move_ship():
    animate(ship,tween = "accel_decel",pos=ship.target,duration=ship.distance_to(ship.target)/200,on_finished=next_ship_target)

next_ship_target()


def draw():
    screen.clear()
    block.draw()
    ship.draw()


pgzrun.go()