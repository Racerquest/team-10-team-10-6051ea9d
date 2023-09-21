class Character:
    name = ""

    def __init__(self, character_name):
        if character_name == '':
            character_name = "bobZilla"
        self.name = character_name
