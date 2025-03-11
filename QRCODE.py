import qrcode
import pygame
import sys
import pyperclip
from tkinter import Tk, filedialog

pygame.init()

# Paramètres
WIDTH, HEIGHT = 800, 500
WHITE, BLACK, RED, FUSHIA = (255, 255, 255), (0, 0, 0), (255, 0, 0), (255, 0, 255)

def draw_glowing_text(text, x, y, color, glow_color, intensity=5, center=True):
    font = pygame.font.Font(None, 40)
    for i in range(intensity, 0, -1):
        glow_surface = font.render(text, True, glow_color)
        screen.blit(glow_surface, (x - glow_surface.get_width() // 2 - i, y - i))
        screen.blit(glow_surface, (x - glow_surface.get_width() // 2 + i, y + i))
    text_surface = font.render(text, True, color)
    if center:
        screen.blit(text_surface, (x - text_surface.get_width() // 2, y))
    else:
        screen.blit(text_surface, (x, y))

# Initialisation de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("QRCode26x ")
font = pygame.font.Font(None, 40)

# Charger l'image de fond avec opacité après l'initialisation de l'affichage
background = pygame.image.load("sang.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

save_button = None

def draw_text(text, x, y, color=WHITE, center=True):
    text_surface = font.render(text, True, color)
    if center:
        screen.blit(text_surface, (x - text_surface.get_width() // 2, y))
    else:
        screen.blit(text_surface, (x, y))

def generate_qr(url):
    qr = qrcode.make(url, box_size=10, border=5)
    qr.save("qrcode26x.png")
    global save_button
    save_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 100, 200, 50)

def save_qr():
    root = Tk()
    root.withdraw()  # Cacher la fenêtre Tkinter
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        pygame.image.save(pygame.image.load("qrcode26x.png"), file_path)
        print(f"QR Code enregistré sous : {file_path}")

def main():
    input_box = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 - 30, 400, 50)
    active, text = False, ""
    
    while True:
        screen.blit(background, (0, 0))  # Afficher l'image de fond
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))  # Ajouter un voile semi-transparent (50% d'opacité)
        screen.blit(overlay, (0, 0))
        
        draw_glowing_text("     -yanis26x", 50, 20, FUSHIA, (255, 0, 255, 100), intensity=1)  # Texte en haut à gauche avec glow
        draw_text("3NTr3z uN L1EN eT appuy3z Sur 3NTEr !", WIDTH // 2, 100)  # Titre légèrement plus bas
        pygame.draw.rect(screen, RED, input_box, 3)  # Bordure rouge
        pygame.draw.rect(screen, WHITE, input_box)  # Fond blanc
        draw_text(text, WIDTH // 2, input_box.y + 10, BLACK)  # Texte noir
        
        if save_button:
            pygame.draw.rect(screen, RED, save_button, border_radius=10)
            draw_text("Enregistrer l'image !", WIDTH // 2, save_button.y + 10)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                elif save_button and save_button.collidepoint(event.pos):
                    save_qr()
                else:
                    active = False
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