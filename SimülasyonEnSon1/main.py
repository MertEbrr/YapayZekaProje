import pygame
import sys
import time


pygame.init()

#Penceremiz
genislik = 1600
yukseklik = 850
pencere = pygame.display.set_mode((genislik, yukseklik))

#RENKLER
arkaplan = (139, 169, 119)
pastel_pink = (255, 182, 193)
brown = (80, 40, 10)
dark_gray = (169, 169, 169)
tree_green = (34, 139, 34)  # Ağaç yeşili
curtain_color_1 = (255, 215, 0)  # Altın sarısı perde
curtain_color_2 = (255, 239, 204)  # Krem rengi perde
cornice_color = (139, 69, 19)  # Kahverengi korniş
asphalt_color = (50, 50, 50)  # Asfalt yol için koyu gri
black = (0, 0, 0)  # Tekerlekler için siyah ofis ve ev içinde kullanılıyor
silver = (192, 192, 192)  # Jant rengi
white = (255, 255, 255)  # Farlar, pencere çerçeveleri ve ön ızgara için white
yellow = (255, 255, 0)  # Sarı renk tanımlaması
red = (255, 0, 0)  # Kırmızı
green = (0, 255, 0)  # Yeşil
red_off = (100, 0, 0)
yellow_off = (100, 100, 0)
green_off = (0, 100, 0)
pink = (255, 192, 203)  # Pembe
havuz_mavisi = (0, 191, 255)  # MERKEZ DAİRE
stone_light = (169, 169, 169)  # Taşlı yol için açık gri
stone_dark = (105, 105, 105)  # Taşlı yol için koyu gri
small_building_color = (200,200,200)
building_color=(150,150,150)


# Yazı tipi ayarları
font = pygame.font.Font(None, 20)
garage_font = pygame.font.Font(None, 18)


#EKLENEN RESİMLER
cop_kutusu = pygame.image.load("cop_kutusu.png")
agac = pygame.image.load("agac.png")
kazi_alani=pygame.image.load("kazi_alani.png")
yolengel=pygame.image.load("yolengel.png")
isci=pygame.image.load("amele.png")










#BAŞLANGIÇ NOKTAMIZ OLAN GARJIMIZ VE GÜZEL EVİMİZ
#Home sweet home...
# Ev çizim fonksiyonu
def draw_house(x, y):
    house_width, house_height = 75, 75  # Küçültülmüş ev boyutları
    pygame.draw.rect(pencere, pastel_pink, (x, y, house_width, house_height))
    pygame.draw.polygon(pencere, brown, [(x, y), (x + house_width // 2, y - house_height // 2), (x + house_width, y)])
    pygame.draw.rect(pencere, dark_gray, (x + 26, y + 38, 23, 38))  # Kapı küçültüldü

    # Pencereler
    window_size = 15
    left_window = pygame.draw.rect(pencere, black, (x + 7, y + 15, window_size, window_size), 2)
    right_window = pygame.draw.rect(pencere, black, (x + 53, y + 15, window_size, window_size), 2)

    # Perdeler
    pygame.draw.rect(pencere, cornice_color, (left_window.x - 2, left_window.y - 5, window_size + 4, 5))
    pygame.draw.rect(pencere, cornice_color, (right_window.x - 2, right_window.y - 5, window_size + 4, 5))
    pygame.draw.rect(pencere, curtain_color_1, (left_window.x + 2, left_window.y + 2, window_size - 4, window_size // 2))
    pygame.draw.rect(pencere, curtain_color_2, (left_window.x + 2, left_window.y + window_size // 2 + 2, window_size - 4, window_size // 2))
    pygame.draw.rect(pencere, curtain_color_1, (right_window.x + 2, right_window.y + 2, window_size - 4, window_size // 2))
    pygame.draw.rect(pencere, curtain_color_2, (right_window.x + 2, right_window.y + window_size // 2 + 2, window_size - 4, window_size // 2))


#SİMÜLASYON BAŞLANGIÇ NOKTASI
# Araba Garajı çizim fonksiyonu
def draw_garage(x, y):
    garage_width, garage_height = 60, 45  # Küçültülmüş garaj boyutları
    pygame.draw.rect(pencere, black, (x, y, garage_width, garage_height))
    pygame.draw.rect(pencere, dark_gray, (x + 8, y + 15, garage_width - 16, garage_height - 20))

    # "GARAGE" yazısını ekle
    text = garage_font.render("GARAGE", True, white)
    text_rect = text.get_rect(center=(x + garage_width // 2, y + 8))
    pencere.blit(text, text_rect)


#SİMÜLASYON BİTİŞ NOKTASI
# Büyük işyeri binası çizim fonksiyonu
def draw_large_building(x, y):
    building_width, building_height = 90, 112  # Küçültülmüş boyutlar
    pygame.draw.rect(pencere, building_color, (x, y, building_width, building_height))
    pygame.draw.rect(pencere, black, (x, y - 15, building_width, 15))  # Düz çatı
    text = font.render("OFFICE", True, white)
    pencere.blit(text, (x + 15, y - 15))

    for i in range(3):
        for j in range(3):
            pygame.draw.rect(pencere, black, (x + 11 + i * 22, y + 15 + j * 30, 11, 11), 2)


# Küçük işyeri binası çizim fonksiyonu
def draw_small_building(x, y):
    building_width, building_height = 60, 75  # Küçültülmüş boyutlar
    pygame.draw.rect(pencere, small_building_color, (x, y, building_width, building_height))
    pygame.draw.rect(pencere, black, (x, y - 7, building_width, 15))  # Düz çatı
    text = font.render("OFFICE", True, white)
    pencere.blit(text, (x + 5, y - 8))

    for i in range(3):
        pygame.draw.rect(pencere, black, (x + 8 + i * 18, y + 15, 11, 11), 2)  # Üst pencereler
        pygame.draw.rect(pencere, black, (x + 8 + i * 18, y + 45, 11, 11), 2)  # Alt pencereler


#YOLLARIN VE ŞERİT ÇİZGİLERİNİN KALINLIĞI, ŞERİT ÇİZGİLERİ ARASI BOŞLUK
yol_width = 80
serit_width = 5
serit_gap = 45


# YOLLAR

#en üstte olan yatay yol
def draw_ust_yatay_road():
    pygame.draw.rect(pencere, asphalt_color, (0, 75, genislik, yol_width))  # üst yatay yol

#en altta olan yatay yol
def draw_alt_yatay_road():
    pygame.draw.rect(pencere, asphalt_color, (0, 615, genislik, yol_width))  # alt yatay yol

#evden çıkan en soldaki dikey yol
def draw_sol_dikey_road():
    pygame.draw.rect(pencere, asphalt_color, (150, 80, yol_width, yukseklik))  # sol dikey yol

#köpekli kadının geçtiği yol
def draw_sag_dikey_road():
    pygame.draw.rect(pencere, asphalt_color, (875, 80, yol_width, 650))  # sağ dikey yol
#alt kısmına yapılan ekleme minik yol
def draw_minikYol2():
    pygame.draw.rect(pencere, asphalt_color,(875,730,yol_width,300))
#sola dönüşün yasak olduğu, soldan ikinci dikey yol
def draw_ortayol1_road():
    pygame.draw.rect(pencere, asphalt_color, (400, 400, yol_width, 275))  # sol orta yolun dikey yolu
#alt kısmına yapılan ekleme minik yol
def draw_minikYol1():
    pygame.draw.rect(pencere,asphalt_color,(400,650,yol_width,300))
#yol çalışmasının olduğu yol
def draw_orta_yatay1_road():
    pygame.draw.rect(pencere, asphalt_color, (460, 400, 415, yol_width))  # sol orta yolun yatay yolu

#en sağdaki dikey yol
def draw_ortayol2_road():
    pygame.draw.rect(pencere, asphalt_color, (1400, 225, yol_width, 450))  # sağ orta yolun dikey yolu

#yukarıdan ikinci yol
def draw_orta_yatay2_road():
    pygame.draw.rect(pencere, asphalt_color, (935, 225, 525, yol_width))  # sağ orta yolun yatay yolu

#kavşağın çizimi
def draw_kavsak_ortası():
    pygame.draw.circle(pencere,havuz_mavisi,(190,650),20,0)# kavşağın ortasındaki mavi daire
#mavi daireyi çevreleyen beyaz çizgi
def draw_kavsakiccercevesi():
    pygame.draw.circle(pencere,white,(190,650),20,2)#mavi dairenin etrafındaki beyaz çember
# dairesel yol
def draw_daireselyol():
    pygame.draw.circle(pencere,asphalt_color,(190,650),100,0) #kavşak yolu



#ŞERİT ÇİZGİLERİNİN ÇİZİLMESİ

def draw_serit_cizgileri():
    for y in range(170, 535, serit_gap * 2):
        pygame.draw.rect(pencere, white, (187, y, serit_width, serit_gap))  # sol dikey yol
    for y in range(175, 600, serit_gap * 2):
        pygame.draw.rect(pencere, white, (912, y, serit_width, serit_gap))  # sağ dikey yol
    for x in range(290, 1600, serit_gap * 2):
        pygame.draw.rect(pencere, white, (x, 650, serit_gap, serit_width))  # alt yatay yol
    for x in range(0, 1600, serit_gap * 2):
        pygame.draw.rect(pencere, white, (x, 110, serit_gap, serit_width))  # üst yatay yol
    for y in range(445, 600, serit_gap * 2):
        pygame.draw.rect(pencere, white, (437, y, serit_width, serit_gap),)  # sağ orta yolun dikey yolu
    for y in range(265, 600, serit_gap * 2):
        pygame.draw.rect(pencere, white, (1438, y, serit_width, serit_gap))  # sol orta yolun dikey yolu
    for x in range(460, 875, serit_gap * 2):
        pygame.draw.rect(pencere, white, (x, 436, serit_gap, serit_width))  # sol orta yolun yatay yolu
    for x in range(970, 1415, serit_gap * 2):
        pygame.draw.rect(pencere, white, (x, 262, serit_gap, serit_width))  # sağ orta yolun yatay yolu
    for y in range(700,900,serit_gap*2):
        pygame.draw.rect(pencere,white,(437,y,serit_width,serit_gap))   #minikyol1 in şeritleri
    for y in range(700,900,serit_gap*2):
        pygame.draw.rect(pencere,white,(912,y,serit_width,serit_gap))   #minikyol2 nin şeritleri


#TRAFİK LEVHALARININ RESİMLERİNİN YÜKLEME ALANI

yaya_gecidi_img = pygame.image.load("yayagecidi.png")
tali_yol_img = pygame.image.load("yolver.png")
dur_img = pygame.image.load("durlevhasi.png")
yol_calismasi_img = pygame.image.load("yolcalismasi.png")
donel_kasvak = pygame.image.load("donelkavsak.png")
unlem = pygame.image.load("unlem.png")
duraklamakYasak= pygame.image.load("duraklamakYasak.png")
sagaDonusYasak=pygame.image.load("sagaDonusYasak.png")
solaDonusYasak=pygame.image.load("solaDonusYasak.png")

# EKLENEN GÖRSELLERİN BOYUT AYARLAMASI

scale_factor = 0.1  # Görsellerin boyutunu küçültmek için bir ölçek faktörü
yaya_gecidi_img = pygame.transform.scale(yaya_gecidi_img, (int(yaya_gecidi_img.get_width() * scale_factor), int(yaya_gecidi_img.get_height() * scale_factor)))
tali_yol_img = pygame.transform.scale(tali_yol_img, (int(tali_yol_img.get_width() * scale_factor), int(tali_yol_img.get_height() * scale_factor)))
dur_img = pygame.transform.scale(dur_img, (int(dur_img.get_width() * 0.2), int(dur_img.get_height() * 0.2)))
yol_calismasi_img = pygame.transform.scale(yol_calismasi_img, (int(yol_calismasi_img.get_width() * scale_factor), int(yol_calismasi_img.get_height() * scale_factor)))
donel_kasvak = pygame.transform.scale(donel_kasvak, (int(donel_kasvak.get_width() * scale_factor), int(donel_kasvak.get_height() * scale_factor)))

kazi_alani= pygame.transform.scale(kazi_alani,(int(kazi_alani.get_width()*scale_factor),int(kazi_alani.get_height()*scale_factor)))
yolengel= pygame.transform.scale(yolengel,(int(yolengel.get_width()*scale_factor),int(yolengel.get_height()*scale_factor)))
solaDonusYasak= pygame.transform.scale(solaDonusYasak,(int(solaDonusYasak.get_width()*scale_factor),int(solaDonusYasak.get_height()*scale_factor)))
sagaDonusYasak= pygame.transform.scale(sagaDonusYasak,(int(sagaDonusYasak.get_width()*0.2),int(sagaDonusYasak.get_height()*0.2)))


#TRAFİK IŞIĞININ ÇİZİMİ 1

isik_radius = 10
# TRAFİK IŞIĞINDA IŞIK RENGİNİN DEĞİŞİMİ
def draw_trafik_isigi(x, y, light_color):
    # Trafik ışığı çizimi
    pygame.draw.rect(pencere, (0, 0, 0), (x, y, 20, 60))
    pygame.draw.circle(pencere, green_off if light_color != "yesil" else green, (x + 10, y + 10), isik_radius)
    pygame.draw.circle(pencere, yellow_off if light_color != "sari" else yellow, (x + 10, y + 30), isik_radius)
    pygame.draw.circle(pencere, red_off if light_color != "kirmizi" else red, (x + 10, y + 50), isik_radius)


#YAYA GEÇİTLERİNİN ÇİZDİRİLMESİ
#Yaya geçidi çizgilerinin özellikleri
line_height = 7  # yaya gecidi şeridinin genişliği
cizgiler_arasi_aralik = 8
line_width = 55

def draw_yatay_yaya_gecidi():
    # Çizgi boyutları
    for i in range(5, 11):  # bir yolun genişliği 7-12 aralığında yani 5 piksel
        yaya_gecidi = pygame.Rect(550, i * (line_height + cizgiler_arasi_aralik), line_width,
                                  line_height)  # 550 x eksenindeki konumu
        pygame.draw.rect(pencere, white if i % 1 == 0 else asphalt_color, yaya_gecidi)


def draw_dikey_yaya_gecidi():
    # Dikey yaya geçidi çizgilerini çiz
    for i in range(58,64):  # bir yolun genişliği 80-85 aralığında yani 5 piksel
        yaya_gecidi = pygame.Rect(i * (line_height + cizgiler_arasi_aralik), 320, line_height,
                                  line_width)  # 300 y eksenindeki konumu
        pygame.draw.rect(pencere, white if i % 1 == 0 else asphalt_color, yaya_gecidi)

#GEÇİCİ ARABANIN ÇİZDİRİLMESİ
def draw_car(x, y, color):
    pygame.draw.rect(pencere, color, (x, y, 30, 15), border_radius=60)  # Araba gövdesi


# Bütün Fonksiyonları Çağırdığımız ve Ana Ekranı Oluşturduğumuz MAIN Fonksiyon

def main():
    pygame.display.update()
    # TRAFİK IŞIĞI ZAMANLAYICISI
    clock = pygame.time.Clock()
    start_time = time.time()
    light_color = "yesil"  # Trafik ışığı başlangıcı

    # NPC'ler

    # NPC Arabalar
    car_x_yellow = -60  # Sarı arabanın başlangıç pozisyonu
    car_y_yellow = 705  # Taşlı yol üzerinde olacak şekilde y konumu
    car_speed_yellow = 2  # Sarı arabanın hızı

    car_x_red = 1000  # Kırmızı arabanın başlangıç pozisyonu
    car_y_red = 80  # Asfalt yol üzerinde olacak şekilde y konumu
    car_speed_red = 2  # Kırmızı arabanın hızı (daha hızlı)

    kedi = pygame.image.load("kedi.png")
    kedi_x = 1200
    kedi_y = 750
    kedi_speed = 1

    npc_kopekli_abla_sol = pygame.image.load("npc_kopekli_abla_sol.png")
    npc_kopekli_abla_sag = pygame.image.load("npc_kopekli_abla_sag.png")

    npc_adam_on = pygame.image.load("npc_adam_on.png")
    npc_adam_arka = pygame.image.load("npc_adam_arka.png")

    # Karakter başlangıç pozisyonu ve hız

    npc_kopekli_abla_x = 920
    npc_kopekli_abla_y = 300
    npc_kopekli_abla_speed = 0.5
    gidis_sol = True

    npc_adam_x = 550
    npc_adam_y = 0
    npc_adam_speed = 0.6
    gidis_asagi = True

    run = True

    # Ana Ekranı Çalıştırma ve Kapatma
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Arkaplan rengini uygula
        pencere.fill(arkaplan)

        # Kazı Alanındaki Yer Resmini Ekrana Yazdır

        # --------------------------------------------------------------------------------------------------------------
        pencere.blit(kazi_alani, (700, 470))
        pencere.blit(kazi_alani, (700, 480))
        pencere.blit(kazi_alani, (750, 480))
        pencere.blit(kazi_alani, (800, 480))
        # Trafik Işığı Renk Döngüsü
        # 20 SANİYE YEŞİL, 3 SANİYE SARI, 10 SANİYE KIRMIZI, 3 SANİYE SARI, 20 SANİYE YEŞİL... OLACAK ŞEKİLDE...
        elapsed_time = (time.time() - start_time) % 36  # TOPLAM 36 SANİYE

        if elapsed_time < 20:
            light_color = "yesil"
        elif elapsed_time < 23:
            light_color = "sari"
        elif elapsed_time < 33:
            light_color = "kirmizi"


        car_x_red -= car_speed_red
        car_x_yellow += car_speed_yellow
        kedi_x += kedi_speed

        # NPCLER

        # NPC Arabalar ve Kedi
        if car_x_yellow > 1800:  # Sarı Araba Alttaki Yoldan Geçecek
            car_x_yellow = -100

        if car_x_red < -100:  # Kırmızı Araba Yukardaki Yoldan
            car_x_red = 1800
        if car_x_red > 1800:
            car_x_red = 1800
        if kedi_x > genislik:
            kedi_x = 200

        # Sağdaki Dikey Yolda Yaya Geçidinden Geçen Köpekli Kadın
        if gidis_sol:
            npc_kopekli_abla = npc_kopekli_abla_sol
            npc_kopekli_abla_x -= npc_kopekli_abla_speed
            if npc_kopekli_abla_x < 800:  # Sol sınır
                gidis_sol = False
                npc_kopekli_abla = npc_kopekli_abla_sag
        else:
            npc_kopekli_abla_x += npc_kopekli_abla_speed
            if npc_kopekli_abla_x > 950:  # Sağ sınır
                gidis_sol = True
                npc_kopekli_abla = npc_kopekli_abla_sol

        # Üst Yatay Yolda Yaya Geçidinden Geçen Yalnız Yıkık Adam
        if gidis_asagi:
            npc_adam = npc_adam_on
            npc_adam_y += npc_adam_speed
            if npc_adam_y > 100:  # Aşağı sınır
                gidis_asagi = False
                npc_adam = npc_adam_arka
        else:
            npc_adam_y -= npc_adam_speed
            if npc_adam_y < -75:  # Yukarı sınır
                gidis_asagi = True
                npc_adam = npc_adam_on

        # KÜÇÜLTÜLMÜŞ KAMYONUN DETAYLI ÇİZİMİ
        def draw_truck(x, y):
            # Kamyon gövdesi (turuncu) - boyut küçültüldü
            pygame.draw.rect(pencere, (255, 140, 0), (x - 90, y, 90, 35), border_radius=6)

            # Tuğla şekilli yük (daha detaylı, küçültülmüş)
            for i in range(3):  # Satır sayısı azaltıldı
                for j in range(2):  # İki satır tuğla
                    brick_color = (210, 105, 30) if (i + j) % 2 == 0 else (180, 90, 20)
                    pygame.draw.rect(pencere, brick_color, (x - 85 + i * 10, y + 6 + j * 5, 10, 4))

            # Saydam yük örtüsü - boyut küçültüldü
            overlay_surface = pygame.Surface((70, 18), pygame.SRCALPHA)  # Boyutları küçültüldü
            overlay_surface.fill((200, 200, 200, 100))
            pencere.blit(overlay_surface, (x - 85, y + 6))

            # Kabin (sürücü bölümü) - boyut küçültüldü
            pygame.draw.rect(pencere, (255, 140, 0), (x, y + 6, 18, 30), border_radius=6)
            pygame.draw.polygon(pencere, (255, 140, 0), [(x, y + 6), (x + 18, y), (x + 18, y + 6)])

            # Kabin detayları (kapı ve pencere) - boyut küçültüldü
            pygame.draw.rect(pencere, white, (x + 4, y + 14, 8, 10))
            pygame.draw.rect(pencere, white, (x + 6, y + 10, 6, 8))

            # Kapı kolu
            pygame.draw.circle(pencere, silver, (x + 12, y + 18), 1.5)

            # Farlar - boyut küçültüldü ve yukarı konumlandırıldı
            pygame.draw.circle(pencere, yellow, (x - 8, y + 3), 2.5)

            # Tekerlekler - boyut küçültüldü
            pygame.draw.circle(pencere, (0, 0, 0), (x + 9, y + 38), 5)  # Ön tekerlek
            pygame.draw.circle(pencere, (0, 0, 0), (x - 60, y + 37), 5)  # Arka sol tekerlek
            pygame.draw.circle(pencere, (0, 0, 0), (x - 30, y + 37), 5)  # Arka sağ tekerlek

            # Jantlar - boyut küçültüldü
            pygame.draw.circle(pencere, white, (x + 9, y + 38), 2)  # Ön tekerlek jant
            pygame.draw.circle(pencere, white, (x - 60, y + 37), 2)  # Arka sol tekerlek jant
            pygame.draw.circle(pencere, white, (x - 30, y + 37), 2)  # Arka sağ tekerlek jant

            # Arka kısım detayları - boyut küçültüldü
            pygame.draw.rect(pencere, (200, 140, 0), (x - 90, y + 30, 90, 6))

            # Arka lambalar - boyut küçültüldü
            pygame.draw.circle(pencere, red, (x - 85, y + 35), 1.5)  # Sol arka lamba
            pygame.draw.circle(pencere, red, (x - 70, y + 35), 1.5)  # Sağ arka lamba

        # Kamyon konumu !!!KAMYONUN YER DEĞİŞİKLİĞİ İÇİN!!!
        truck_x = 1300
        truck_y = 653

        # Fonksiyonları Ekrana Yazdırma

        draw_alt_yatay_road()
        draw_sol_dikey_road()
        draw_ust_yatay_road()
        draw_sag_dikey_road()
        draw_ortayol1_road()
        draw_orta_yatay1_road()
        draw_ortayol2_road()
        draw_orta_yatay2_road()
        draw_daireselyol()
        draw_kavsak_ortası()
        draw_kavsakiccercevesi()
        draw_minikYol1()
        draw_minikYol2()
        draw_serit_cizgileri()


        pygame.draw.rect(pencere, white, (610, 75, 5, 80))  # adamın geçtiği yaya geçidi
        pygame.draw.rect(pencere, white, (540, 75, 5, 80))  # adamın geçtiği yaya geçidi
        pygame.draw.rect(pencere, white, (875, 380, 80, 5))  # kadının geçtiği yaya geçidi
        pygame.draw.rect(pencere, white, (875, 310, 80, 5))  # kadının geçtiği yaya geçidi
        pygame.draw.rect(pencere, white, (875, 225, 80, 2))  # sağ dikey yoldaki yatay trafik ışığı çizgisi
        pygame.draw.rect(pencere, white, (150, 225, 80, 2))  # sol dikey yoldaki yatay trafik ışığı çizgisi
        pygame.draw.rect(pencere, white, (150, 550, 80, 2))  # kavşaktaki dikey trafik ışığını çizgisi
        draw_trafik_isigi(120, 505, light_color)  # kavşaktaki trafik ışığı
        draw_trafik_isigi(120, 175, light_color)  # sol üst kesişen yolda trafik ışığı
        draw_trafik_isigi(845, 160, light_color)  # sağ dikey yol sonundaki trafik ışığı

        # Yaya Geçitlerini Ekle
        draw_yatay_yaya_gecidi()
        draw_dikey_yaya_gecidi()

        # NPC'leri Ekle

        draw_car(car_x_yellow, car_y_yellow, yellow)  # Sarı araba
        draw_car(car_x_red, car_y_red, red)  # Kırmızı araba
        pencere.blit(npc_kopekli_abla, (npc_kopekli_abla_x, npc_kopekli_abla_y))
        pencere.blit(npc_adam, (npc_adam_x, npc_adam_y))
        pencere.blit(kedi, (kedi_x, kedi_y))

        # Tabelaları Konumlarına Göre Yerleştir (şeffaflık ile)
        pencere.blit(yaya_gecidi_img, (620, 100))
        pencere.blit(yaya_gecidi_img, (950,360))
        pencere.blit(tali_yol_img, (800, 420))
        pencere.blit(dur_img, (35, 700))
        pencere.blit(donel_kasvak, (200, 700))
        pencere.blit(yolengel,(665,440))
        pencere.blit(solaDonusYasak,(370,530))
        pencere.blit(solaDonusYasak, (850, 530))
        pencere.blit(isci,(750,450))
        pencere.blit(agac,(700,200))
        pencere.blit(agac, (500, 200))
        pencere.blit(agac, (1400, 700))
        pencere.blit(agac, (1200, 400))
        pencere.blit(agac, (1100, 380))

        #kamyonun çizimi
        draw_truck(truck_x, truck_y)
        # Ev ve işyeri çizimleri
        # Küçük ev ve garajı çiz, evin sol alt köşeye yerleştir
        draw_house(60, yukseklik -60 )  # Küçültülmüş ev koordinatları
        draw_garage(155, yukseklik - 45)  # Küçültülmüş garaj konumu

        # Küçük ofis binalarını hizaladım
        draw_large_building(20, 10)  # Küçük büyük işyeri
        draw_small_building(120, 10)  # Küçük küçük işyeri


        # Dekorasyon Resimlerini ve Konumlarını Yükle

        pencere.blit(cop_kutusu, (820, 350))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

