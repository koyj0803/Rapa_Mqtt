import RPi.GPIO as GPIO                     # GPIO 라이브러리 모듈 import
import time                                 # 시간 관련 라이브러리 모듈 import

TRIG_PIN = 20                               # Trig 핀 지정
ECHO_PIN = 21                               # Echo 핀 지정

def initUltrasonic():                       # 초음파 센서 초기화 함수
 GPIO.setup(TRIG_PIN, GPIO.OUT)             # Trig 핀 출력 설정
 GPIO.setup(ECHO_PIN, GPIO.IN)              # Echo 핀 출력 설정

def controlUltrasonic():                    # 초음파 센서 제어 함수
    distance = 0.0                          # 거리 변수 선언
    GPIO.output(TRIG_PIN, False)            # Trig 핀 LOW 신호 출력
    time.sleep(0.5)                         # 500ms 지연
    GPIO.output(TRIG_PIN, True)             # Trig 핀 HIGH 신호 출력
    time.sleep(0.00001)                     # 10us 지연
    GPIO.output(TRIG_PIN, False)            # Trig 핀 LOW 신호 출력
    
    while GPIO.input(ECHO_PIN) == 0 :       # Echo 핀 신호 입력 대기
        pulse_start = time.time()           # 대기 시작 시간 측정
    while GPIO.input(ECHO_PIN) == 1 :       # Echo 핀 신호 입력
        pulse_end = time.time()             # 입력 시간 측정
    
    pulse_duration = pulse_end - pulse_start # 시간차 계산
    distance = pulse_duration * 17000        # 거리 계산
    distance = round(distance, 2) 
    return distance 

def main():                                     # 메인 함수
    GPIO.setmode(GPIO.BCM)                      # GPIO 모드 설정
    distance = 0.0                              # 거리 변수 설정
    initUltrasonic()                            # 초음파 센서 초기화
    print("Ultrasonic Operating ...") 

    try:                                        # try 안 프로그램 실행 동안 키보드 인터럽트(Ctrl+C) 실행시 except 안 코드실행

        while True:
            distance = controlUltrasonic()      # 거리 측정
            print("Distance:%.2f cm"%distance)  # 터미널 창에 거리 출력

    except KeyboardInterrupt:                   # 키보드 인터럽트 시 실행
        GPIO.cleanup()                          # GPIO 핀 초기화

if __name__ == '__main__':                      # 메인 함수 실행
    main() 




