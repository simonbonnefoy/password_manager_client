class String:
    @staticmethod
    def contains_chars_from_list(input_string:str, char_list: list):
        """
        Check if a string contains any of the characters from a list
        for example: string = 'ac' and char_list = ['a','b'] returns True
        string = 'ac' and char_list = ['d','e'] returns True
        @param input_string: string to check
        @param char_list: list containing the characters to check, whether present in the list or not
        @return:  bool
        """
        if any(c in char_list for c in input_string):
            return True

        return False
