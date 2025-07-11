def draw_text(screen, text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))