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