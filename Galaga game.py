import pgzrun
import random
HEIGHT = 400
WIDTH = 600
TITLE = "Galaga"

alien = Actor("alien galaga")
spaceship = Actor("spaceship")
spaceship.pos = 350,350
alien.pos = 300,30
bullets = []
score = 0 
def draw():
    
    screen.fill("blue")
    spaceship.draw()
    alien.draw()
    screen.draw.text("Score: " + str(score), (50,50), color = "white")
    
    for bullet in bullets :
        bullet.draw()
        


def on_key_down(key) :
    if key == keys.SPACE :
        bullet = Actor("bullet")
        bullet.pos = spaceship.x,spaceship.y - 20
        bullets.append(bullet)

    
        



def update():
    
    
     
    for bullet in bullets :
        global score
        bullet.y -= 2
        if bullet.colliderect(alien) :
            alien.y = 0
            alien.x = random.randint(0,600)
            bullets.remove(bullet)
            score += 1
        if bullet.y < 0 :
            bullets.remove(bullet)    
    alien.y += 2
    if alien.y >= 400 :
        alien.y = 0
        alien.x = random.randint(0,600)
        score -= 5

    if keyboard.right :
        spaceship.x += 4
    if keyboard.left :
        spaceship.x -= 4    


pgzrun.go()        