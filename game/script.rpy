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

    show razz smug
    razz "So, legend has it the previous inhabitants 'passed away of mysterious causes.'"
    show jay unimpressed
    hide razz
    play sound car_door_shut
    jay "Yeah, legend. {i}Myth.{/i}"

    show josh
    play sound car_door_shut
    josh "Anyway, now that we're actually here..."
    # TODO: play car locking sfx?
    # TODO: display the house
    josh "Time to find out if this place is haunted."
    show josh at left
    with move
    show razz at left
    with moveinleft
    show jay smug at right 
    with move
    jay "Or not..."


    return
