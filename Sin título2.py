# -*- coding: utf-8 -*-


import serial
import time

# Configuración Serial para la pantalla LCD
LCD_PORT = '/dev/ttyS0'  # UART de la Raspberry Pi (TX/RX GPIO)
LCD_BAUDRATE = 9600
lcd_serial = serial.Serial(LCD_PORT, LCD_BAUDRATE, timeout=1)

# Comandos para la pantalla LCD
LCD_CODES = {
    "INICIO": {'hexCodes': [0x5A, 0xA5, 0x07, 0x82, 0x00, 0x84, 0x5A, 0x01, 0x00, 0x00]},
    "IDLE": {'hexCodes': [0x5A, 0xA5, 0x07, 0x82, 0x00, 0x84, 0x5A, 0x01, 0x00, 0x01]},
    "CARGANDO": {'hexCodes': [0x5A, 0xA5, 0x07, 0x82, 0x00, 0x84, 0x5A, 0x01, 0x00, 0x02]},
    "ERROR": {'hexCodes': [0x5A, 0xA5, 0x07, 0x82, 0x00, 0x84, 0x5A, 0x01, 0x00, 0x03]},
    "RESUMEN": {'hexCodes': [0x5A, 0xA5, 0x07, 0x82, 0x00, 0x84, 0x5A, 0x01, 0x00, 0x04]},
}

def LCDScreen(code):
    """Envía un comando de la pantalla LCD usando los datos hexadecimales."""
    # Obtener el tamaño de los datos hexadecimales
    data_size = len(code['hexCodes'])
    
    # Enviar los datos hexadecimales por UART
    for i in range(data_size):
        lcd_serial.write(bytes([code['hexCodes'][i]]))  # Enviar byte por UART
    print(f"Comando {list(code.keys())[0]} enviado al LCD")

def main():
    """Prueba de comunicación con la pantalla LCD para todos los comandos."""
    try:
        print("Iniciando prueba de pantalla LCD...")
        for command in LCD_CODES.keys():
            LCDScreen(LCD_CODES[command])  # Llamar a la función LCDScreen
            time.sleep(1)  # Pausa entre comandos
        print("Prueba completada.")
    except Exception as e:
        print(f"Error durante la prueba: {e}")
    finally:
        lcd_serial.close()

if __name__ == "__main__":
    main()
