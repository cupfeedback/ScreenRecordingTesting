import tkinter as tk
from pynput import keyboard, mouse
import time

# 이벤트를 기록할 리스트
events = []

# 키보드 이벤트 핸들러
def on_keyboard_event(key):
    # 키보드 이벤트를 events 리스트에 추가
    events.append(('keyboard', key))

# 마우스 이벤트 핸들러
def on_mouse_event(x, y, button, pressed):
    # 마우스 이벤트를 events 리스트에 추가
    events.append(('mouse', x, y, button, pressed))

# 키보드 리스너 생성
keyboard_listener = keyboard.Listener(on_press=on_keyboard_event, on_release=None)
# 마우스 리스너 생성
mouse_listener = mouse.Listener(on_move=on_mouse_event, on_click=on_mouse_event, on_scroll=None)

# GUI 버튼 클릭 이벤트 핸들러
def start_recording():
    # events 리스트 초기화
    events.clear()
    # 키보드 리스너 시작
    keyboard_listener.start()
    # 마우스 리스너 시작
    mouse_listener.start()

def stop_recording():
    # 키보드 리스너 중지
    keyboard_listener.stop()
    # 마우스 리스너 중지
    mouse_listener.stop()

def run_macro():
    # events 리스트를 기반으로 매크로 실행 로직
    for event in events:
        event_type = event[0]
        if event_type == 'keyboard':
            # 키보드 이벤트 처리 로직
            key = event[1]
            # 예시: 키보드 이벤트를 출력
            print(f'키보드 이벤트: {key}')
        elif event_type == 'mouse':
            # 마우스 이벤트 처리 로직
            x, y, button, pressed = event[1], event[2], event[3], event[4]
            # 예시: 마우스 이벤트를 출력
            print(f'마우스 이벤트: x={x}, y={y}, button={button}, pressed={pressed}')
        # 매크로 실행 간격 (초)
        time.sleep(0.5)

# GUI 생성
root = tk.Tk()
root.title("매크로 레코더")

# 버튼 생성
start_button = tk.Button(root, text="레코딩 시작", command=start_recording)
start_button.pack()

stop_button = tk.Button(root, text="레코딩 중지", command=stop_recording)
stop_button.pack()

run_button = tk.Button(root, text="매크로 실행", command=run_macro)
run_button.pack()

# GUI 실행
root.mainloop()