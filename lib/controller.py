__author__ = 't35khan'

# fetch plateau boundaries and get rover initial locations and move commands


class Controller:
    def __init__(self, input_file_path):
        with open(input_file_path) as input_file:
            self.input_commands = input_file.readlines()
        self.x_plateau_lower, self.y_plateau_lower = 0, 0
        self.x_plateau_upper, self.y_plateau_upper = 5, 5

    def get_plateau_bounds(self):
        try:
            bounds = self.input_commands[0].strip().split(" ")
            self.x_plateau_upper, self.y_plateau_upper = int(bounds[0]), int(bounds[1])
            return self.x_plateau_lower, self.y_plateau_lower, self.x_plateau_upper, self.y_plateau_upper
        except Exception as ex:
            template = "An exception of type {0} occurred."
            message = template.format(type(ex).__name__, ex.args)
            print(message, "Could not get plateau boundaries.\nUsing default values.")
            return self.x_plateau_lower, self.y_plateau_lower, self.x_plateau_upper, self.y_plateau_upper

    def get_rover_commands(self):
        rover_commands = []
        for line in self.input_commands[1:]:
            if line != "\n" and line != " ":
                line = line.strip().split(" ")
                rover_commands.append(line)
        return rover_commands
