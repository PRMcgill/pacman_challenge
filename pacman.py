
# class and functions for Pacman
class Pacman:
    points = 5000
    lives = 3
    v_ghost = 200

    def lose_life():
        Pacman.lives -= 1
    
    def bonus_life():
        Pacman.lives += 1
    # this calculates how the fruit points are added
    def devour(fruit):
        Pacman.points += fruit
        return Pacman.points
    # this calculates how the vulnerable ghosts points work
    def devour_ghosts():
        Pacman.points += Pacman.v_ghost
        Pacman.v_ghost *= 2
        if Pacman.v_ghost == 1600:
            Pacman.v_ghost = 200
# valure for the new life threshold
new_life = 10000

fruit = {
    'dot' : 10,
    'cherry' : 100,
    'strawberry' : 300,
    'orange' : 500,
    'apple' : 700,
    'melon' : 1000,
    'galaxian' : 2000,
    'bell' : 3000,
    'key' : 5000,
    }



path = open('pacman.txt', 'r')
pathing = path.read().split(',')

for paths in pathing:
    score= paths.lower()

    if score == 'vulnerableghost':
        Pacman.devour_ghosts()
    elif score == 'invincibleghost':
        Pacman.lose_life()
    
    else:
        for key, value in fruit.items():
            if score == key:
                Pacman.devour(value)
    # calculates how to gain lives
    if Pacman.points >= new_life:
        Pacman.bonus_life()

        new_life += 10000
    if Pacman.lives == 0:
        break
# prints out the lives and score for each time an item is hit in pacman.txt file to get the final score
    print(f"Lives: {Pacman.lives}\n"
        f"Points: {Pacman.points}")

   
