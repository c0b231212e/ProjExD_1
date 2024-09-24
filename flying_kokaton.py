import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    bgr_img = pg.transform.flip(bg_img, True, False)
    kk_img = pg.transform.flip(kk_img, True, False) #練習2
    #kk_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_rct = kk_img.get_rect() #練習8-1 surfaceからrectを抽出する
    kk_rct.center = 300, 200 #練習8-2 rectを使った初期座標の設定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        dif_x = 0
        dif_y = 0

        key_lst = pg.key.get_pressed() #練習8-3 キーの押下状態を取得
        if key_lst[pg.K_UP]: #練習8-4
            dif_y -= 1 #こうかとんの縦座標を-1する
        if key_lst[pg.K_DOWN]:
            dif_y += 1
        if key_lst[pg.K_RIGHT]:
            dif_x += 2
        if key_lst[pg.K_LEFT]:
            dif_x -= 2
        else:
            dif_x -= 1

        kk_rct.move_ip((dif_x, dif_y))

        x = -(tmr % 3200) #練習6
        screen.blit(bg_img, [x, 0])
        screen.blit(bgr_img, [x + 1600, 0])
        screen.blit(bg_img, [x + 3200, 0])
        screen.blit(bgr_img, [x + 4800, 0])
        screen.blit(kk_img, kk_rct) #練習8-5
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
