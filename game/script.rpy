# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define jay = Character("Jay")
define razz = Character("Razz")
define josh = Character("Josh")

label start:
    scene bg street

    "It's a dark and cloudy night over Hunter's Green"
    "A night like this could remind you of another night, where three friends went for a drive..."
    "...hoping to see the only abandoned house in Hunter's Green."
    play sound car_pulling_up
    queue sound turning_off_car
    "A car pulls up to the driveway."
    "Razz, Jay, and Josh exit the car."
    stop sound

    show razz smirk

    razz "So, legend has it the previous inhabitants 'passed away of mysterious causes.'"

    show jay unimpressed

    jay "Yeah, legend. {i}Myth.{/i}"
    
    return
