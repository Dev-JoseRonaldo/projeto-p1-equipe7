from assets.scripts.Score import *

class Button():
    def __init__(self, position_click, postion_button_play, postion_button_menu, button_width, button_height, score):
        self.position_click = position_click
        self.postion_button_play = postion_button_play
        self.postion_button_menu = postion_button_menu
        self.button_width = button_width
        self.button_height = button_height
        self.score = score

    def mouse_click_game_over(self):
        click_x, click_y = self.position_click
        button_x, button_y = self.postion_button_play
        button_a, button_b = self.postion_button_menu
        if button_x - (self.button_width//2) < click_x < button_x + (self.button_width//2) and button_y - (self.button_height//2) < click_y < button_y + (self.button_height//2):
            return False, False
        elif button_a - (self.button_width//2) < click_x < button_a + (self.button_width//2) and button_b - (self.button_height//2) < click_y < button_b + (self.button_height//2):
            return False, True
        return True, False
    
    def mouse_click_menu(self):
        click_x, click_y = self.position_click
        button_x, button_y = self.postion_button_play
        button_a, button_b = self.postion_button_menu
        if button_x - (self.button_width//2) < click_x < button_x + (self.button_width//2) and button_y - (self.button_height//2) < click_y < button_y + (self.button_height//2):
            return False, True
        elif button_a - (self.button_width//2) < click_x < button_a + (self.button_width//2) and button_b - (self.button_height//2) < click_y < button_b + (self.button_height//2):
            return True, False
        return True, True