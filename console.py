class Console:
    @staticmethod
    def print_string(string):
        print(string)

    @staticmethod
    def prompt_input(string):
        result = input(string)
        return int(result)
