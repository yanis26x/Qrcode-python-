import qrcode
import pygame
import sys
import pyperclip

pygame.init()

# Paramètres
WIDTH, HEIGHT = 500, 300
WHITE, BLACK, RED = (255, 255, 255), (0, 0, 0), (255, 0, 0)

# Initialisation de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("QR Code Generator")
font = pygame.font.Font(None, 32)

# Charger l'image de fond avec opacité après l'initialisation de l'affichage
background = pygame.image.load("sang.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

def draw_text(text, x, y, color=WHITE):
    screen.blit(font.render(text, True, color), (x, y))

def generate_qr(url):
    qr = qrcode.make(url, box_size=10, border=5)
    qr.save("qrcode.png")

def main():
    input_box = pygame.Rect(50, 100, 400, 32)
    active, text = False, ""
    
    while True:
        screen.blit(background, (0, 0))  # Afficher l'image de fond
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))  # Ajouter un voile semi-transparent (50% d'opacité)
        screen.blit(overlay, (0, 0))
        
        draw_text("Entrez un lien et appuyez sur Entrée", 50, 50)
        pygame.draw.rect(screen, RED, input_box, 2)  # Bordure rouge
        pygame.draw.rect(screen, WHITE, input_box)  # Fond blanc
        draw_text(text, input_box.x + 5, input_box.y + 5, BLACK)  # Texte noir
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                active = input_box.collidepoint(event.pos)
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        generate_qr(text)
                        print("QR Code généré : qrcode.png")
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        text += pyperclip.paste()  # Coller le texte depuis le presse-papier
                    else:
                        text += event.unicode

if __name__ == "__main__":
    main()