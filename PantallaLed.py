# -*- coding: utf-8 -*-

import serial
import time

# Configuración Serial para la pantalla LCD
LCD_PORT = '/dev/ttyUSB0'  # Cambiar según el puerto usado
LCD_BAUDRATE = 9600
lcd_serial = serial.Serial(LCD_PORT, LCD_BAUDRATE, timeout=1)

# Comandos para la pantalla LCD
LCD_CODES = {
    "INICIO": [0x5A, 0xA5, 0x07, 0x82, 0x00, 0x84, 0x5A, 0x01, 0x00, 0x00],
    "IDLE": [0x5A, 0xA5, 0x07, 0x82, 0x00, 0x84, 0x5A, 0x01, 0x00, 0x01],
    "CARGANDO": [0x5A, 0xA5, 0x07, 0x82, 0x00, 0x84, 0x5A, 0x01, 0x00, 0x02],
    "ERROR": [0x5A, 0xA5, 0x07, 0x82, 0x00, 0x84, 0x5A, 0x01, 0x00, 0x03],
    "RESUMEN": [0x5A, 0xA5, 0x07, 0x82, 0x00, 0x84, 0x5A, 0x01, 0x00, 0x04],
}

def send_lcd_command(command_name):
    """Envía un comando al LCD y verifica la respuesta."""
    if command_name in LCD_CODES:
        lcd_serial.write(bytearray(LCD_CODES[command_name]))
        print(f"Comando {command_name} enviado al LCD")
        
        # Leer respuesta (si aplica)
        response = lcd_serial.read(10)  # Cambiar tamaño según respuesta esperada
        print(f"Respuesta del LCD: {response}")
    else:
        print(f"Comando {command_name} no encontrado")

def main():
    """Prueba de comunicación con la pantalla LCD para todos los comandos."""
    try:
        print("Iniciando prueba de pantalla LCD...")
        for command in LCD_CODES.keys():
            send_lcd_command(command)
            time.sleep(1)  # Pausa entre comandos
        print("Prueba completada.")
    except Exception as e:
        print(f"Error durante la prueba: {e}")
    finally:
        lcd_serial.close()

if __name__ == "__main__":
    main()
