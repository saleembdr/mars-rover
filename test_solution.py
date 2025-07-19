
from solution import Rover, process_plateau_rovers

def test_rover_direction_change_north_east():
    
    rover = Rover(0, 0, 'N', (10,10))
    rover.process_command('R')
    
    assert rover.direction == 'E'

def test_rover_direction_change_east_south():
    
    rover = Rover(0, 0, 'E', (10,10))
    rover.process_command('R')
    
    assert rover.direction == 'S'

def test_rover_direction_change_west_south():
    
    rover = Rover(0, 0, 'W', (10,10))
    rover.process_command('L')
    
    assert rover.direction == 'S'

def test_rover_move_north():
    
    rover = Rover(0, 0, 'N', (10,10))
    rover.process_command('M')
    
    assert rover.x == 0 and rover.y == 1

def test_rover_move_east():
    
    rover = Rover(2, 3, 'E', (10,10))
    rover.process_command('M')
    
    assert rover.x == 3 and rover.y == 3

def test_rover_move_south():
    
    rover = Rover(5, 4, 'S', (10,10))
    rover.process_command('M')
    
    assert rover.x == 5 and rover.y == 3

def test_rover_move_west():
    
    rover = Rover(6, 2, 'W', (10,10))
    rover.process_command('M')
    
    assert rover.x == 5 and rover.y == 2

def test_rover_rotate_right_move():
    
    rover = Rover(0, 0, 'N', (10,10))
    rover.process_command('R')
    rover.process_command('M')
    
    assert rover.x == 1 and rover.y == 0

def test_rover_move_north_limit():
    
    rover = Rover(0, 10, 'N', (10,10))
    rover.process_command('M')
    
    assert rover.y == 10

def test_rover_move_south_limit():
    
    rover = Rover(0, 0, 'S', (10,10))
    rover.process_command('M')
    
    assert rover.y == 0

def test_rover_move_west_limit():
    
    rover = Rover(0, 5, 'W', (10,10))
    rover.process_command('M')
    
    assert rover.x == 0

def test_rover_rotate_right_move_sequence():
    
    rover = Rover(0, 0, 'N', (10,10))
    rover.process_command_sequence('RM')
    
    assert rover.x == 1 and rover.y == 0

def test_rover_get_position_text():
    
    rover = Rover(0, 0, 'N', (10,10))
    
    actual_position_text = rover.get_position_text()
    expected_position_text = "0 0 N"
    
    assert actual_position_text == expected_position_text
    
def test_process_plateau_rovers():
    
    input_text = "\n".join([
        "5 5",
        "1 2 N",
        "LMLMLMLMM",
        "3 3 E",
        "MMRMMRMRRM"
    ])
    
    actual_output_text = process_plateau_rovers(input_text)
    
    expected_output_text = "\n".join([
        "1 3 N",
        "5 1 E"
    ])
    
    assert actual_output_text == expected_output_text
