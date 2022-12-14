import pygame
from settings import *

class UI:
    def __init__(self):
        # general
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

    def show_bar(self, current, max_amount, bg_rect, color):
        # draw bg
        pygame.draw.rect(screen, UI_BG_COLOR, bg_rect)

        # converting stat to pixel
        ratio = current / max_amount
        if ratio > 1:
            ratio = 1
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # drawing the bar
        pygame.draw.rect(screen, color, current_rect)
        pygame.draw.rect(screen, UI_BORDER_COLOR, bg_rect, 3)
        
    def advanced_health(self, player):
        transition_width = 0
        transition_color = (255, 0, 0)
        health_bar_rect = pygame.Rect(10, 10, player.current_health / player.health_ratio,BAR_HEIGHT)

        if player.current_health < player.health:
            player.current_health += player.health_change_speed
            transition_width = int((player.health - player.current_health) / (player.health_ratio))
            transition_color = (0, 255, 0) # green
        if player.current_health > player.health:
            if player.health < player.or_health / 3:
                # if player health lower than max health / 3 than speed up animation speed
                player.current_health -= player.health_change_speed * 5
            else:
                player.current_health -= player.health_change_speed
            transition_width = int((player.current_health - player.health) / (player.health_ratio))
            transition_color = (255, 255, 0) # yellow
            if health_bar_rect.right + transition_width > player.health_bar_length + 5:
                    transition_width = player.health_bar_length + 5 - health_bar_rect.right

        transition_bar_rect = pygame.Rect(health_bar_rect.right, 10, transition_width, BAR_HEIGHT)

        # black bg
        pygame.draw.rect(screen, UI_BG_COLOR, (10, 10, player.health_bar_length, BAR_HEIGHT))
        # health bar
        pygame.draw.rect(screen, HEALTH_COLOR, health_bar_rect)
        # health bar animation
        pygame.draw.rect(screen, transition_color, transition_bar_rect)
        # outline
        pygame.draw.rect(screen, UI_BORDER_COLOR, (10, 10, player.health_bar_length, BAR_HEIGHT), 3)
        health_value_surf = self.font.render(str(int(player.current_health)) + '/' + str(player.or_health), False, UI_BG_COLOR)
        health_value_rect = health_value_surf.get_rect(topleft = health_bar_rect.bottomleft + pygame.math.Vector2(0, 10))
        screen.blit(health_value_surf, health_value_rect)

    def display(self, player):
        # health and energy
        self.advanced_health(player) # hp bar with animation