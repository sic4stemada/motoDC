import RPi.GPIO as GPIO
import time

# Konfigurasi pin motor DC
in1 = 24
in2 = 23
en = 25

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)

# Fungsi untuk menggerakkan motor maju
def motor_maju():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)

# Fungsi untuk menggerakkan motor mundur
def motor_mundur():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)

# Fungsi untuk menghentikan motor
def motor_berhenti():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)

# Mengatur PWM
p = GPIO.PWM(en, 20)
p.start(25)

try:
    while True:
        print("Pilih durasi maju:")
        print("1. meja 1")
        print("2. 2 detik")
        print("3. 4 detik")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == "1": #start
            motor_maju()
            print("Kopi 1")
            time.sleep(2)
           
            motor_berhenti()
            time.sleep(2)

            motor_maju()
            print("Air Hangat")
            time.sleep(1)
            motor_berhenti()
            time.sleep(2)

            motor_maju()
            print("Menuju meja 1")
            time.sleep(2)
            motor_berhenti()
            time.sleep(2)

            motor_mundur()
            print("kembali ke awal")
            time.sleep(5)
            motor_berhenti() #end
        elif pilihan == "2":
            motor_maju()
            print("Motor bergerak maju selama 2 detik.")
            time.sleep(2)
            motor_berhenti()

            motor_mundur()
            print("Motor bergerak mundur selama 2 detik.")
            time.sleep(2)
            motor_berhenti()
        elif pilihan == "3":
            motor_maju()
            print("Motor bergerak maju selama 4 detik.")
            time.sleep(4)
            motor_berhenti()

            motor_mundur()
            print("Motor bergerak mundur selama 4 detik.")
            time.sleep(4)
            motor_berhenti()
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
