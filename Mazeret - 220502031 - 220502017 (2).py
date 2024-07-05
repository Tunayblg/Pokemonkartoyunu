import pygame
import sys
import random
from abc import ABC, abstractmethod
# Favicon'u yükle
favicon = pygame.image.load('favicon.ico')

# Favicon'u ayarla
pygame.display.set_icon(favicon)
# Pygame'i başlat
pygame.init()

# Ekran boyutlarını belirle
screen_width = 1000
screen_height = 800

# Ekran oluştur
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokémon Kart Oyunu")

# Renk tanımlamaları
white = (255, 255, 255)
darkblue = (28, 15, 69)
blue = (0, 0, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

# Resimleri yükle (varsayılan boyutları kullanıyoruz)
logo = pygame.image.load('logo.png')
play_button = pygame.image.load('play_button.png')
exit_button = pygame.image.load('exit3.png')
exit_button2 = pygame.image.load('exit2.png')
kartdagit_button = pygame.image.load('kartdagit.png')
pikachu = pygame.image.load('pikachu.png')
charmander = pygame.image.load('charmander.png')
jigglypuff = pygame.image.load('jigglypuff.png')
golbat = pygame.image.load('golbat.png')
ekans = pygame.image.load('ekans.png')
eevee = pygame.image.load('eevee.png')
squirtle = pygame.image.load('squirtle.png')
meowth = pygame.image.load('meowth.png')
bulbasaur = pygame.image.load('bulbasaur.png')
charizard = pygame.image.load('charizard.png')
kartarka = pygame.image.load('kartarka.png')
pcvsbutton = pygame.image.load('pcvspc.png')
pikachukapak = pygame.image.load('pikachukapak.png')
kapak2 = pygame.image.load('kapak2.png')
kapak3 = pygame.image.load('kapak3.png')


# Resimlerin boyutlarını ayarla (gerekirse)
logo = pygame.transform.scale(logo, (400, 200))
play_button = pygame.transform.scale(play_button, (300, 150))
pcvsbutton = pygame.transform.scale(pcvsbutton, (300, 130))
exit_button = pygame.transform.scale(exit_button, (300, 150))
exit2_button = pygame.transform.scale(exit_button2, (100, 100))
kartdagit_button = pygame.transform.scale(kartdagit_button, (100, 100))
kartarka = pygame.transform.scale(kartarka, (150, 150))
kartarka_kucuk = pygame.transform.scale(kartarka, (75, 75))  # Küçük boyutlu arka yüz
kartarka_orta = pygame.transform.scale(kartarka, (100, 100))  # Orta boyutlu arka yüz
pikachukapak = pygame.transform.scale(pikachukapak, (400, 400)) 
kapak2 = pygame.transform.scale(kapak2, (400, 400)) 
kapak3  = pygame.transform.scale(kapak3, (300, 700)) 






#Ozel kartlar PokemonCard ust sinifindan kalitiyoruz

#Ayni zamanda public private ozelliklerini kullandik kapsulleme icin

#Kalitim ve cok Bicimlilik kullanan turetilmis siniflar

# Kart sinifi (Encapsulation)
class PokemonCard:
    def __init__(self, name=None, image=None, guc=0):
        if name is None and image is None:
            # Parametresiz yapici metot
            self._name = "Default Name"
            self._image = None  # Varsayilan bir resim burada ayarlanabilir
            self._guc = 0
        else:
            # Parametreli yapici metot
            self._name = name
            self._image = image
            self._guc = guc

    def get_name(self):
        return self._name

    def get_image(self):
        return self._image

    def set_image(self, image):
        self._image = image

    def get_guc(self):
        return self._guc

    def set_guc(self, guc):
        self._guc = guc

    def display(self):
        print(f"{self._name} karti, guc: {self._guc}")

# Kartlari olustur (Inheritance ve Polymorphism)
pikachu_card = PokemonCard('Pikachu', pygame.transform.scale(pikachu, (200, 200)), 99)
charmander_card = PokemonCard('Charmander', pygame.transform.scale(charmander, (200, 200)), 85)
jigglypuff_card = PokemonCard('Jigglypuff', pygame.transform.scale(jigglypuff, (200, 200)), 68)
golbat_card = PokemonCard('Golbat', pygame.transform.scale(golbat, (200, 200)), 73)
ekans_card = PokemonCard('Ekans', pygame.transform.scale(ekans, (200, 200)), 82)
eevee_card = PokemonCard('Eevee', pygame.transform.scale(eevee, (200, 200)), 79)
squirtle_card = PokemonCard('Squirtle', pygame.transform.scale(squirtle, (200, 200)), 75)
meowth_card = PokemonCard('Meowth', pygame.transform.scale(meowth, (200, 200)), 77)
bulbasaur_card = PokemonCard('Bulbasaur', pygame.transform.scale(bulbasaur, (200, 200)), 80)
charizard_card = PokemonCard('Charizard', pygame.transform.scale(charizard, (200, 200)), 94)
default_card = PokemonCard()  # Parametresiz yapici metot ile olusturulan kart

kartlar = [pikachu_card, charmander_card, jigglypuff_card, golbat_card, ekans_card, eevee_card, squirtle_card, meowth_card, bulbasaur_card, charizard_card]
kart_orta = {
    pikachu: {"image": pygame.transform.scale(pikachu, (200, 200)), "guc": 99},
    charmander: {"image": pygame.transform.scale(charmander, (200, 200)), "guc": 85},
    jigglypuff: {"image": pygame.transform.scale(jigglypuff, (200, 200)), "guc": 68},
    golbat: {"image": pygame.transform.scale(golbat, (200, 200)), "guc": 73},
    ekans: {"image": pygame.transform.scale(ekans, (200, 200)), "guc": 82},
    eevee: {"image": pygame.transform.scale(eevee, (200, 200)), "guc": 79},
    squirtle: {"image": pygame.transform.scale(squirtle, (200, 200)), "guc": 75},
    meowth: {"image": pygame.transform.scale(meowth, (200, 200)), "guc": 77},
    bulbasaur: {"image": pygame.transform.scale(bulbasaur, (200, 200)), "guc": 80},
    charizard: {"image": pygame.transform.scale(charizard, (200, 200)), "guc": 94},
}

#Resimlerin alannini ve yerini belirliyoruzu
logo_rect = logo.get_rect(center=(screen_width / 2, screen_height / 4))
play_button_rect = play_button.get_rect(center=(screen_width / 2, screen_height / 1.95))
exit_button_rect = exit_button.get_rect(center=(screen_width / 2, screen_height / 1.50))
kartdagit_button_rect = kartdagit_button.get_rect(center=(screen_width / 19, screen_height / 2))
exit2_button_rect = exit2_button.get_rect(center=(screen_width / 1.05, screen_height / 2))
pcvsbutton_rect = pcvsbutton.get_rect(center=(screen_width / 2, screen_height / 1.2))
pikachukapak_rect = pikachukapak.get_rect(center=(screen_width / 7.6, screen_height / 1.2))
kapak2_rect = kapak2.get_rect(center=(screen_width / 1., screen_height / 1.2))
kapak3_rect = kapak3.get_rect(center=(screen_width / 1.15, screen_height / 1.6))


kartlar = [pikachu, charmander, jigglypuff, golbat, ekans, eevee, squirtle, meowth, bulbasaur, charizard]

# Oyuncu ve bilgisayarın kartları için boş listeler
oyuncu_kartlari = []
bilgisayar_kartlari = []
destede_kalan_kartlar = []
oyuncu_secili_kart = None
bilgisayar_secili_kart = None
oyuncu_puan = 0
bilgisayar_puan = 0

pygame.mixer.music.load('oyun.mp3')
pygame.mixer.music.play(-1)
# Kartlari dagitan fonksiyon
def kartlari_dagit():
    global oyuncu_kartlari, bilgisayar_kartlari, destede_kalan_kartlar
    kart_destesi = random.sample(kartlar, 10)
    oyuncu_kartlari = kart_destesi[:3]
    bilgisayar_kartlari = kart_destesi[3:6]
    destede_kalan_kartlar = kart_destesi[6:]
    print("Kartlar dağıtıldı: Oyuncu kartları:", oyuncu_kartlari, "Bilgisayar kartları:", bilgisayar_kartlari)

# Tiklandiginde desteden kart secicek
def desteden_kart_sec():
    global oyuncu_kartlari, bilgisayar_kartlari, destede_kalan_kartlar
    if screen_width // 4 - (len(destede_kalan_kartlar) * 20) <= event.pos[0] <= screen_width // 4 + (len(destede_kalan_kartlar) * 20) and screen_height // 2 - 37 <= event.pos[1] <= screen_height // 2 + 37:
        if len(destede_kalan_kartlar) >= 2:
            oyuncu_kartlari.append(destede_kalan_kartlar.pop(0))
            bilgisayar_kartlari.append(destede_kalan_kartlar.pop(0))
            print("Desteden kart seçildi: Oyuncu kartları:", oyuncu_kartlari, "Bilgisayar kartları:", bilgisayar_kartlari)
        else:
            print("Destede yeterli kart yok!")
    else:
        print("Lütfen desteden kart seçmek için doğru alanı tıklayın.")

# Kazanani ekrana yazdir
def restart_game():
    global oyuncu_kartlari, bilgisayar_kartlari, destede_kalan_kartlar, oyuncu_secili_kart, bilgisayar_secili_kart, oyuncu_puan, bilgisayar_puan, main_menu, game_running
    oyuncu_kartlari = []
    bilgisayar_kartlari = []
    destede_kalan_kartlar = []
    oyuncu_secili_kart = None
    bilgisayar_secili_kart = None
    oyuncu_puan = 0
    bilgisayar_puan = 0
    main_menu = True
    game_running = False

def pc_vs_pc_start():
    global game_running, pc_vs_pc_running
    pc_vs_pc_running = True
    kartlari_dagit()  # Kartları dağıt
    pygame.time.set_timer(pygame.USEREVENT, 2000)  # 2 saniyede bir kart seçilsin

def check_empty_deck():
    global oyuncu_kartlari, bilgisayar_kartlari, destede_kalan_kartlar

    if len(destede_kalan_kartlar) == 0:
        print("Destede kart kalmadı. Otomatik olarak 2 kart dağıtılıyor.")

        # Oyuncuya 2 kart dağıt
        if len(kartlar) >= 2:
            oyuncu_kartlari.append(kartlar.pop(0))
            oyuncu_kartlari.append(kartlar.pop(0))
        else:
            print("Yeterli kart yok!")

        # Bilgisayara 2 kart dağıt
        if len(kartlar) >= 2:
            bilgisayar_kartlari.append(kartlar.pop(0))
            bilgisayar_kartlari.append(kartlar.pop(0))
        else:
            print("Yeterli kart yok!")

        # Yeni kartlar dağıtıldıktan sonra durumu kontrol et
        print("Yeni kartlar dağıtıldı: Oyuncu kartları:", oyuncu_kartlari, "Bilgisayar kartları:", bilgisayar_kartlari)

        # Oyun durumunu kontrol et
        check_game_end()

def pc_vs_pc_turn():
    global oyuncu_kartlari, bilgisayar_kartlari, oyuncu_puan, bilgisayar_puan

    if len(bilgisayar_kartlari) > 0 and len(oyuncu_kartlari) > 0:  # Kartlar varsa devam et
        oyuncu_secili_kart = random.choice(oyuncu_kartlari)
        oyuncu_kartlari.remove(oyuncu_secili_kart)

        bilgisayar_secili_kart = random.choice(bilgisayar_kartlari)
        bilgisayar_kartlari.remove(bilgisayar_secili_kart)

        # Kart güçlerini karşılaştırarak puan ekle
        if kart_orta[oyuncu_secili_kart]["guc"] > kart_orta[bilgisayar_secili_kart]["guc"]:
            oyuncu_puan += 10
            print("Oyuncu kazandı! Puan:", oyuncu_puan)
        elif kart_orta[oyuncu_secili_kart]["guc"] < kart_orta[bilgisayar_secili_kart]["guc"]:
            bilgisayar_puan += 10
            print("Bilgisayar kazandı! Puan:", bilgisayar_puan)
        else:
            print("Berabere!")

        # Seçilen kartları ortada yan yana göster (orta boyutlu)
        screen.blit(kart_orta[bilgisayar_secili_kart]["image"], (screen_width // 2 + 50, screen_height // 3 - 75))
        screen.blit(kart_orta[oyuncu_secili_kart]["image"], (screen_width // 2 + 50, 2 * screen_height // 3 - 75))
        pygame.display.flip()  # Ekranı güncelle

        pygame.time.wait(1000)  # 1 saniye beklet

        # Oyun bitimini kontrol et
        check_game_end()

    else:
        print("Kartlar kalmadı veya bir tarafta kart kalmadı!")
        if len(oyuncu_kartlari) == 0 and len(destede_kalan_kartlar) >= 2:
            oyuncu_kartlari.append(destede_kalan_kartlar.pop(0))
            oyuncu_kartlari.append(destede_kalan_kartlar.pop(0))
            print("Oyuncuya 2 kart dağıtıldı:", oyuncu_kartlari)
        if len(bilgisayar_kartlari) == 0 and len(destede_kalan_kartlar) >= 2:
            bilgisayar_kartlari.append(destede_kalan_kartlar.pop(0))
            bilgisayar_kartlari.append(destede_kalan_kartlar.pop(0))
            print("Bilgisayara 2 kart dağıtıldı:", bilgisayar_kartlari)
        pygame.time.wait(1000)  # 1 saniye beklet
def check_game_end():
    global game_running, pc_vs_pc_running
    if len(oyuncu_kartlari) == 0 and len(bilgisayar_kartlari) == 0 and len(destede_kalan_kartlar) == 0:
        game_running = False
        pc_vs_pc_running = False
        # Kazananı ekrana yazdır
        font_winner = pygame.font.Font(None, 64)
        if oyuncu_puan > bilgisayar_puan:
            winner_text = font_winner.render("Oyuncu Kazandı!", True, yellow)
        elif oyuncu_puan < bilgisayar_puan:
            winner_text = font_winner.render("Bilgisayar Kazandı!", True, yellow)
        else:
            winner_text = font_winner.render("Berabere!", True, yellow)
        winner_text_rect = winner_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.fill(black)
        screen.blit(winner_text, winner_text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)  # 3 saniye beklet
        restart_game()
        main_menu = True  # Ana menüye dön

    

# Müziği yükle ve başlat
pygame.mixer.music.load('oyun.mp3')
pygame.mixer.music.play(-1)  # -1 müziği sürekli çalması için

# Ana menü ve oyun durumu
main_menu = True
game_running = False

# Ana döngü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if main_menu:
                if play_button_rect.collidepoint(event.pos):
                    main_menu = False
                    game_running = True
                elif exit_button_rect.collidepoint(event.pos):
                    running = False
                elif pcvsbutton_rect.collidepoint(event.pos):
                    main_menu = False
                    game_running = True
                    pc_vs_pc_start()  # Otomatik oyunu başlat
            elif game_running:
                if kartdagit_button_rect.collidepoint(event.pos):
                    print("Kart Dağıt butonuna tıklandı")
                    kartlari_dagit()
                    oyuncu_secili_kart = None
                    bilgisayar_secili_kart = None
                elif exit2_button_rect.collidepoint(event.pos):
                    running = False
                elif screen_width // 4 - (len(destede_kalan_kartlar) * 20) <= event.pos[0] <= screen_width // 4 + (len(destede_kalan_kartlar) * 20) and screen_height // 2 - 37 <= event.pos[1] <= screen_height // 2 + 37:
                    desteden_kart_sec()
                else:
                    for i, kart in enumerate(oyuncu_kartlari):
                        kart_rect = pygame.Rect(150 + i * 160, screen_height - 200, 150, 150)
                        if kart_rect.collidepoint(event.pos):
                            oyuncu_secili_kart = kart
                            oyuncu_kartlari.remove(kart)  # Oyuncu kartlar listesinden seçilen kartı çıkar
                            bilgisayar_secili_kart = random.choice(bilgisayar_kartlari)
                            bilgisayar_kartlari.remove(bilgisayar_secili_kart)  # Bilgisayar kartlar listesinden rastgele seçilen kartı çıkar
                            
                            # Kart güçlerini karşılaştırarak puan ekle
                            if kart_orta[oyuncu_secili_kart]["guc"] > kart_orta[bilgisayar_secili_kart]["guc"]:
                                oyuncu_puan += 10
                                print("Oyuncu kazandı! Puan:", oyuncu_puan)
                            elif kart_orta[oyuncu_secili_kart]["guc"] < kart_orta[bilgisayar_secili_kart]["guc"]:
                                bilgisayar_puan += 10
                                print("Bilgisayar kazandı! Puan:", bilgisayar_puan)
                            else:
                                print("Berabere!")

                            # Oyuncu ve bilgisayarın kartları bittiyse ve destede kartlar varsa, yeni kartlar çek
                            if len(oyuncu_kartlari) == 0 and destede_kalan_kartlar:
                                desteden_kart_sec()

                            # Oyun bitimini kontrol et
                            if len(oyuncu_kartlari) == 0 and len(bilgisayar_kartlari) == 0 and len(destede_kalan_kartlar) == 0:
                                game_running = False
                                # Kazananı ekrana yazdır
                                font_winner = pygame.font.Font(None, 64)
                                if oyuncu_puan > bilgisayar_puan:
                                    winner_text = font_winner.render("Oyuncu Kazandı!", True, yellow)
                                elif oyuncu_puan < bilgisayar_puan:
                                    winner_text = font_winner.render("Bilgisayar Kazandı!", True, yellow)
                                else:
                                    winner_text = font_winner.render("Berabere!", True, yellow)
                                winner_text_rect = winner_text.get_rect(center=(screen_width // 2, screen_height // 2))
                                screen.fill(black)
                                screen.blit(winner_text, winner_text_rect)
                                pygame.display.flip()
                                pygame.time.wait(3000)  # 3 saniye beklet
                                restart_game()
                                main_menu = True  # Ana menüye dön
                
        elif event.type == pygame.USEREVENT and pc_vs_pc_running:
            pc_vs_pc_turn()
    # Ekranı mavi ile dolduruyoruz
    screen.fill(blue)

    if main_menu:
        # Ana menüde logoyu ve butonları ekrana çiz
        screen.blit(logo, logo_rect)
        screen.blit(play_button, play_button_rect)
        screen.blit(exit_button, exit_button_rect)
        screen.blit(pcvsbutton, pcvsbutton_rect)
        screen.blit(pikachukapak, pikachukapak_rect)
        # screen.blit(kapak2,kapak2_rect)
        screen.blit(kapak3,kapak3_rect)


    elif game_running:
        # Oyun ekranında yatay bölmeleri çiz
        screen.fill(blue)
        pygame.draw.line(screen, white, (0, screen_height // 3), (screen_width, screen_height // 3), 5)
        pygame.draw.line(screen, white, (0, 2 * screen_height // 3), (screen_width, 2 * screen_height // 3), 5)
        screen.blit(exit2_button, exit2_button_rect)
        screen.blit(kartdagit_button, kartdagit_button_rect)
        
        # Dağıtılan kartları ekranda kapalı şekilde göster
        for i, kart in enumerate(oyuncu_kartlari):
            screen.blit(kartarka, (150 + i * 160, screen_height - 200))

        for i, kart in enumerate(bilgisayar_kartlari):
            screen.blit(kartarka, (150 + i * 160, 50))
        
        # Dağıtılmayan kartları ortada kenarda göster (küçük boyutlu)
        ortada_kart_x = screen_width // 4 - (len(destede_kalan_kartlar) * 20)
        for i, kart in enumerate(destede_kalan_kartlar):
            screen.blit(kartarka_kucuk, (ortada_kart_x + i * 40, screen_height // 2 - 37))
        
        # Seçilen kartları ortada yan yana göster (orta boyutlu)
        if bilgisayar_secili_kart:
            screen.blit(kart_orta[bilgisayar_secili_kart]["image"], (screen_width // 2 + 50, screen_height // 3 - 75))
        if oyuncu_secili_kart:
            screen.blit(kart_orta[oyuncu_secili_kart]["image"], (screen_width // 2 + 50, 2 * screen_height // 3 - 75))

        # Kart sayılarını ve puanları göster
        font = pygame.font.Font(None, 36)
        oyuncu_kart_sayisi = len(oyuncu_kartlari)
        bilgisayar_kart_sayisi = len(bilgisayar_kartlari)
        destede_kalan_kart_sayisi = len(destede_kalan_kartlar)
        oyuncu_kart_sayisi_text = font.render(f"Oyuncu Kartları: {oyuncu_kart_sayisi}", True, white)
        bilgisayar_kart_sayisi_text = font.render(f"Bilgisayar Kartları: {bilgisayar_kart_sayisi}", True, white)
        destede_kalan_kart_sayisi_text = font.render(f"Destede Kalan Kartlar: {destede_kalan_kart_sayisi}", True, white)
        oyuncu_puan_text = font.render(f"Oyuncu Puan: {oyuncu_puan}", True, white)
        bilgisayar_puan_text = font.render(f"Bilgisayar Puan: {bilgisayar_puan}", True, white)
        screen.blit(oyuncu_kart_sayisi_text, (20, 20))
        screen.blit(bilgisayar_kart_sayisi_text, (20, 60))
        screen.blit(destede_kalan_kart_sayisi_text, (20, 100))
        screen.blit(oyuncu_puan_text, (20, 140))
        screen.blit(bilgisayar_puan_text, (20, 180))

    # Ekranı güncelle
    pygame.display.flip()

# Pygame'i kapat
pygame.mixer.music.stop()
pygame.quit()
sys.exit()