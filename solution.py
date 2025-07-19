import math

class Rover:
    
    def __init__(self, x, y, direction, plateau_upper_right):
        
        self.x = x
        self.y = y
        self.direction = direction
        self.plateau_upper_right = plateau_upper_right
        
    def process_command(self, command):
        
        if command in ["R","L"]:
            
            self.process_direction_command(command)
        
        elif command == "M":
        
            self.process_move_command(command)
        
    def process_direction_command(self, command):
        
        direction_list = ["N", "E", "S", "W"]
        command_increment = 1 if command == "R" else -1
        current_direction_index = direction_list.index(self.direction)
        new_direction_index = (current_direction_index + command_increment) % 4
        self.direction = direction_list[new_direction_index]
        
    def process_move_command(self, command):
        
        x_increment = 0
        y_increment = 0
        
        match self.direction:
            case "N":
                x_increment = 0
                y_increment = 1
            case "E":
                x_increment = 1
                y_increment = 0
            case "S":
                x_increment = 0
                y_increment = -1
            case "W":
                x_increment = -1
                y_increment = 0

        new_x = self.x + x_increment
        new_y = self.y + y_increment
        
        new_x = self.get_limited_coordinate(new_x, self.plateau_upper_right[0])       
        new_y = self.get_limited_coordinate(new_y, self.plateau_upper_right[1])       
        
        self.x = new_x
        self.y = new_y
        
    def get_position_text(self):
        
        return f"{self.x} {self.y} {self.direction}"
            
    def get_limited_coordinate(self, coordinate, cooridnate_limit):
        
        new_coordinate = coordinate
        
        if coordinate < 0:
            new_coordinate = 0        
        if coordinate > cooridnate_limit:
            new_coordinate = cooridnate_limit
            
        return new_coordinate

    def process_command_sequence(self, command_sequence):
        
        command_list = list(command_sequence)
        
        for command in command_list:
            
            self.process_command(command)
            
def process_plateau_rovers(input_text):

    input_lines = input_text.split("\n")
    
    plateau_upper_right = [int(coordinate) for coordinate in input_lines[0].split(" ")]
    
    rovers = []
    
    number_of_rovers = math.ceil((len(input_lines)-1)/2)
    
    for rover_index in range(0,number_of_rovers):
        input_line_index = rover_index*2 + 1
    
        rover_position_line = input_lines[input_line_index]
        rover_position_elements = rover_position_line.split(" ")
        
        rover = Rover(int(rover_position_elements[0]), int(rover_position_elements[1]), rover_position_elements[2], plateau_upper_right)
        rovers.append(rover)
        
        rover_commands_line = input_lines[input_line_index+1]
        rover.process_command_sequence(rover_commands_line)
        
    output_lines = [rover.get_position_text() for rover in rovers]
    output_text = "\n".join(output_lines)
    
    return output_text
