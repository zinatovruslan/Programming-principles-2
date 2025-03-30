#2
import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Музыкальный плеер")

MUSIC_FOLDER = "music"
if not os.path.exists(MUSIC_FOLDER):
    os.makedirs(MUSIC_FOLDER)
    print("Создана папка 'music'. Положите в неё MP3-файлы и перезапустите программу.")

tracks = []
for file in os.listdir(MUSIC_FOLDER):
    if file.endswith(".mp3"):
        tracks.append(file)

current_track = 0
music_stopped = False

def play_track(index):
    global music_stopped
    if len(tracks) > 0:
        pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, tracks[index]))
        pygame.mixer.music.play()
        music_stopped = False
        print("Играет:", tracks[index])

if len(tracks) > 0:
    play_track(current_track)
else:
    print("Добавьте MP3-файлы в папку 'music' и перезапустите программу.")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not music_stopped:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                music_stopped = True
            elif event.key == pygame.K_n:
                if len(tracks) > 0:
                    current_track = (current_track + 1) % len(tracks)
                    play_track(current_track)
            elif event.key == pygame.K_p:
                if len(tracks) > 0:
                    current_track = (current_track - 1) % len(tracks)
                    play_track(current_track)
    pygame.time.delay(100)

pygame.quit()
