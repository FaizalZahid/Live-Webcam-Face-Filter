import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# effects = [
    # cv2.imread('gifts/2025.png', -1),
    # cv2.imread('gifts/handhearts.png', -1),
    # cv2.imread('gifts/corgi.png', -1),
    # cv2.imread('gifts/FaizalZahid.png', -1),
    # cv2.imread('gifts/heartme.png', -1),
    # cv2.imread('gifts/ramadan kareem.png', -1),
    # cv2.imread('gifts/shiningstarlight.png', -1),
    # cv2.imread('gifts/babyfox.png', -1),
    # cv2.imread('gifts/wau.png', -1),
    # cv2.imread('gifts/music.png', -1),
    # cv2.imread('gifts/nasilemak.png', -1),
    # cv2.imread('gifts/GG.png', -1),
    # cv2.imread('gifts/candycane.png', -1),
    # cv2.imread('gifts/tiktok.png', -1),
    # cv2.imread('gifts/venus.png', -1),
    # cv2.imread('gifts/perfume.png', -1)
    # cv2.imread('gifts/roticanai.png', -1),
    # cv2.imread('gifts/vote.png', -1),
    # cv2.imread('gifts/rose.png', -1),
    # cv2.imread('gifts/dalgona candy.png', -1),
    # cv2.imread('gifts/meowthumbsup.png', -1),
    # cv2.imread('gifts/festburst.png', -1),
    # cv2.imread('gifts/rosa.png', -1),
    # cv2.imread('gifts/feather.png', -1),
    # cv2.imread('gifts/confetti.png', -1),
    # cv2.imread('gifts/fingerheart.png', -1),
    # cv2.imread('gifts/littleghost.png', -1),
    # cv2.imread('gifts/littlecrown.png', -1),
    # cv2.imread('gifts/papercrane.png', -1),
    # cv2.imread('gifts/icecreamcone.png', -1),
    # cv2.imread('gifts/martabak.png', -1),
    # cv2.imread('gifts/cottoncandy.png', -1),
    # cv2.imread('gifts/instantnoodles.png', -1),
    # cv2.imread('gifts/capybara.png', -1),
    # cv2.imread('gifts/cap.png', -1),
    # cv2.imread('gifts/durian.png', -1),
    # cv2.imread('gifts/tgif.png', -1),
    # cv2.imread('gifts/levelup.png', -1)
    # cv2.imread('gifts/cheeryouup.png', -1),
    # cv2.imread('gifts/teambracelet.png', -1),
    ## Add more if you want. Better to separate in a .json file if too many but this is just a demo. Only a few gifts.
# ]

## 1. If by default, don't want to show face, use overlay_filter(frame, avatar, x, y, w, h) in 4(b) below
avatar = cv2.imread('gifts/FaizalZahid.png', -1)

effects_index = 0
num_effects = len(effects)
frames_per_effect = 1
frame_count = 0

def overlay_filter(frame, effect, x, y, w, h):
    offset = 25
    effect_resized = cv2.resize(effect, (w + 2 * offset, h + 2 * offset))

    overlay_color = effect_resized[:, :, :3]
    overlay_alpha = effect_resized[:, :, 3] / 255.0

    ## 2(a). Resize the filter image to match the size of the face region
    filter_resized = cv2.resize(effect_resized, (w, h))

    ## 2(b). New coordinates and within frame boundaries
    y1, y2 = max(0, y - offset), min(frame.shape[0], y + h + offset)
    x1, x2 = max(0, x - offset), min(frame.shape[1], x + w + offset)

    ## 2(c). Overlay area to match the resized effect
    overlay_y1, overlay_y2 = y1 - (y - offset), y2 - (y - offset)
    overlay_x1, overlay_x2 = x1 - (x - offset), x2 - (x - offset)

    for c in range(0, 3):
        ## 2(d). Alpha blending
        overlay_area = overlay_alpha[overlay_y1:overlay_y2, overlay_x1:overlay_x2]
        frame_area = frame[y1:y2, x1:x2, c]
        overlay_color_area = overlay_color[overlay_y1:overlay_y2, overlay_x1:overlay_x2, c]

        frame[y1:y2, x1:x2, c] = (overlay_area * overlay_color_area + (1 - overlay_area) * frame_area).astype(np.uint8)

while True:
    _, frame = cap.read()
    ## 3. Resize for wider resolution (long and many gifter names)
    # resize = cv2.resize(frame, (852, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        largest_face = max(faces, key=lambda rect: rect[2] * rect[3])
        (x, y, w, h) = largest_face
        
        ## 4(a). Comment/uncomment for gifters absent/present
        # cv2.rectangle(frame, (x-210, y-30), (x+180, y+20), (255, 255, 255), -1)
        # cv2.rectangle(resize, (x-210, y+210), (x+420, y+160), (255, 255, 255), -1)
        # cv2.rectangle(frame, (x-210, y+260), (x+420, y+210), (0, 0, 0), -1)

        ## 4(b). Comment/uncomment for gifters absent/present
        # current_effect = effects[effects_index]
        # overlay_filter(frame, current_effect, x, y, w, h)

        ## 4(c). Comment/uncomment for gifters absent/present
        ## 4(d). Above face
        # cv2.putText(frame, 'Thank you Katerina!', (x-200, y+1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
        # cv2.putText(frame, 'Thank you Katerina!', (x-199, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (133, 53, 29), 2, cv2.LINE_AA)

        ## 4(e). Comment/uncomment for gifters absent/present
        ## 4(f). Below face
        # cv2.putText(resize, 'THANK YOU GOOBER, Kai & Katerina!', (x-200, y+200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
        # cv2.putText(resize, 'THANK YOU GOOBER, Kai & Katerina!', (x-199, y+201), cv2.FONT_HERSHEY_SIMPLEX, 1, (133, 53, 29), 2, cv2.LINE_AA)

        ## 4(g). Comment/uncomment for gifters absent/present
        ## 4(h). Special subscriber box
        # cv2.putText(frame, 'Thank you Red Curry for subscribing!', (x-200, y+250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        # cv2.putText(frame, 'Thank you Red Curry for subscribing!', (x-199, y+251), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 70, 50), 2, cv2.LINE_AA)
        
    cv2.imshow('FaizaLingo Livestream', frame)

    ## 4(i). Comment/uncomment for gifters absent/present
    # frame_count += 1
    # if frame_count % frames_per_effect == 0:
    #     effects_index = (effects_index + 1) % num_effects

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

## Thank you for taking interest in this project. Brought to you by House of Hikmah.