import pyautogui
import time
import subprocess
# 입력할 값을 지정
value_to_input = "Hello, World!"

# 실행할 파일 경로
file_path = "C:/Users/Mihyang/Desktop/automation/kurly.exe"

# 실행할 파일에 대한 명령어와 인자 (필요한 경우)
# 예: 명령어와 인자가 "example.exe arg1 arg2"와 같이 구성되어 있다면
# command = [file_path, "arg1", "arg2"]
command = [file_path]

# subprocess를 사용하여 파일 실행
subprocess.Popen(command)

# 외부 프로그램 실행 및 포커스 이동
# (예시로 메모장 실행)
pyautogui.press('tab')
time.sleep(1)
pyautogui.typewrite('Ekdzhd')
# time.sleep(1)
# pyautogui.press('enter')
# time.sleep(1)

# 입력할 값을 입력하기 위해 메모장 내부 클릭
# pyautogui.click(100, 100)
# time.sleep(1)

# 값을 입력 Ekdzhd
# pyautogui.typewrite(value_to_input)
# time.sleep(1)

# 입력한 값을 저장하고 종료
# pyautogui.hotkey('ctrl', 's')
# time.sleep(1)
# pyautogui.hotkey('alt', 'f4')
