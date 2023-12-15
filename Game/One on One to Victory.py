import pygame
import random

pygame.init()
pygame.display.set_caption("One on One to Victory")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player1 = pygame.Rect(300, 250, 50, 50)
player1_score = 0

player2 = pygame.Rect(500, 250, 50, 50)
player2_score = 0

enemies = []  # Daftar musuh

# Fungsi untuk membuat musuh baru
def create_enemy():
    x = random.randint(0, SCREEN_WIDTH - 50)
    y = random.randint(0, SCREEN_HEIGHT - 50)
    enemy = pygame.Rect(x, y, 50, 50)
    enemies.append(enemy)

# Fungsi untuk menggambar musuh
def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, (0, 250, 0), enemy)

create_enemy()  # Membuat musuh pertama

# Timer
timer_font = pygame.font.Font(None, 36)
timer = 30  # Waktu dalam detik
pygame.time.set_timer(pygame.USEREVENT, 1000)  # Setiap 1000 ms (1 detik), timer berkurang 1 detik

run = True
game_over = False
winner = None

restart_button = pygame.Rect(350, 300, 100, 50) # Membuat tombol restart

current_round = 1  # Tambahkan variabel ronde saat menginisialisasi

jumlah_ronde = 5  # Jumlah total ronde yang ingin dimainkan

while run and current_round <= jumlah_ronde:
    if not game_over:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (250, 0, 0), player1)
        pygame.draw.rect(screen, (0, 0, 250), player2)

        key = pygame.key.get_pressed()

        # Player 1 controls
        if key[pygame.K_a]:
            player1.move_ip(-1, 0)
        elif key[pygame.K_d]:
            player1.move_ip(1, 0)
        elif key[pygame.K_w]:
            player1.move_ip(0, -1)
        elif key[pygame.K_s]:
            player1.move_ip(0, 1)

        # Player 2 controls
        if key[pygame.K_LEFT]:
            player2.move_ip(-1, 0)
        elif key[pygame.K_RIGHT]:
            player2.move_ip(1, 0)
        elif key[pygame.K_UP]:
            player2.move_ip(0, -1)
        elif key[pygame.K_DOWN]:
            player2.move_ip(0, 1)

        # Gambar musuh
        draw_enemies()

        # Periksa tabrakan antara pemain dan musuh
        for enemy in enemies:
            if player1.colliderect(enemy):
                player1_score += 1
                enemies.remove(enemy)
                create_enemy()

            if player2.colliderect(enemy):
                player2_score += 1
                enemies.remove(enemy)
                create_enemy()

        # Gambar skor pemain
        font = pygame.font.Font(None, 36)
        text = font.render(f"Player 1 Score: {player1_score}  Player 2 Score: {player2_score}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        # Gambar timer
        timer_text = timer_font.render(f"Time: {timer}", True, (255, 255, 255))
        screen.blit(timer_text, (10, 40))

        # Periksa waktu berakhir
        if timer == 0:
            game_over = True
            if player1_score > player2_score:
                winner = "Player 1 wins!"
            elif player2_score > player1_score:
                winner = "Player 2 wins!"
            else:
                winner = "It's a draw!"

    # Tampilkan hasil kemenangan jika permainan selesai
    if game_over:
        font = pygame.font.Font(None, 72)
        text = font.render(winner, True, (255, 255, 255))
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

        # Menunggu beberapa detik sebelum ronde berikutnya
        pygame.display.update()
        pygame.time.wait(2000)  # Tunggu 2 detik sebelum ronde berikutnya

        # Reset kondisi permainan dan skor untuk ronde berikutnya
        player1 = pygame.Rect(300, 250, 50, 50)
        player2 = pygame.Rect(500, 250, 50, 50)
        player1_score = 0
        player2_score = 0
        timer = 30
        create_enemy()
        game_over = False
        winner = None

        current_round += 1  # Pindah ke ronde berikutnya

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.USEREVENT:  # Timer berkurang
            if not game_over:
                timer -= 1

    pygame.display.update()

pygame.quit()
