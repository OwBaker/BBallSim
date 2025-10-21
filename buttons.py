'''
File dedicated to outlining the button classes

ImageButton
Button

'''

import pygame

class ImageButton:
    '''class for creating buttons with specific textures'''

    def __init__(self, file, x_cord, y_cord, x_scale, y_scale, centered=True, right=False):

        '''
        args:
            file: image location
            x_cord: x location of center of image
            y_cord: y location of center of image

        '''
        
        self.x = x_cord
        self.y = y_cord
        self.x_scale = x_scale
        self.y_scale = y_scale
        self.centered = centered
        self.right = right
        self.surface = pygame.image.load(file).convert_alpha()

    @property
    def rect(self):
        
        if self.centered is True:
            rect = self.surface.get_rect(center=(self.x, self.y))
        else:
            rect = self.surface.get_rect(x=self.x, y=self.y)
            if self.right == True:
                rect = self.surface.get_rect()
                rect.topright = (self.x, self.y)

        return rect

    def render_button(self, screen):
        
        screen.blit(pygame.transform.scale_by(self.surface, (self.x_scale, self.y_scale)),
                    self.rect.scale_by(self.x_scale, self.y_scale))
    
    def rotate_img(self, amt):

        self.surface = pygame.transform.rotate(self.surface, amt)
    
    def scale_img(self, factor):

        self.surface = pygame.transform.scale_by(self.surface, factor)



class TextButton:
    '''class for creating rectangular buttons with or without text'''

    def __init__(self, x_cord, y_cord, text, size, font=None, text_color="black", centered=True):
        
        self.x = x_cord
        self.y = y_cord
        self.font_obj = pygame.font.SysFont(font, size)
        self.text_render = self.font_obj.render(text, False, text_color)

        if centered is True:
            self.rect = self.text_render.get_rect(center=(self.x, self.y))
        else:
            text_size = self.text_render.size
            self.rect = pygame.rect.Rect((self.x, self.y), text_size)

    def render_button(self, screen):
        '''renders the button on screen'''

        screen.blit(self.text_render, self.rect)