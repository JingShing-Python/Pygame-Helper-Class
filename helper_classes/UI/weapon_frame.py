import pygame
from settings import *

class UI:
    def __init__(self):
        # general
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # bar setup
        # self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        # self.energy_bar_rect = pygame.Rect(10, 34, ENERGY_BAR_WIDTH, BAR_HEIGHT)
        # self.stamina_bar_rect = pygame.Rect(10, 58, ENERGY_BAR_WIDTH, BAR_HEIGHT)

        # convert weapon dictionary
        self.weapon_graphics = []
        for weapon in weapon_data.keys():
            path = 'assets/graphics/weapon/' + weapon + '.png'
            weapon = pygame.image.load(resource_path(path)).convert_alpha()
            weapon = pygame.transform.scale(weapon, (64, 64))
            self.weapon_graphics.append(weapon)

    def selection_box(self, left, top, has_switched):
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(screen, UI_BG_COLOR, bg_rect)
        if has_switched:
            pygame.draw.rect(screen, UI_BORDER_COLOR_ACTIVE, bg_rect, 3)
        else:
            pygame.draw.rect(screen, UI_BORDER_COLOR, bg_rect, 3)
        return bg_rect

    def weapon_overlay(self, weapon_index, has_switched):
        bg_rect = self.selection_box(10, screen.get_size()[1] - 90, has_switched) # weapon
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center = bg_rect.center)

        screen.blit(weapon_surf, weapon_rect)

    def display(self, player):
        # health and energy        
        self.weapon_overlay(player.weapon_index, not(player.can_switch_weapon))
