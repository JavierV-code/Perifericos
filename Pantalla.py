# -*- coding: utf-8 -*-


import serial

class LCDCode:
    def __init__(self, hex_codes):
        self.hex_codes = hex_codes

# Comandos para la pantalla LCD
LCD_CODES = {
    "INICIO": [0x5A, 0xA5, 0x07, 0x82, 0x00, 0x84, 0x5A, 0x01, 0x00, 0x00],
    "IDLE": [0x5A, 0xA5, 0x07, 0x82, 0x00, 0x84, 0x5A, 0x01, 0x00, 0x01],
    "CARGANDO": [0x5A, 0xA5, 0x07, 0x82, 0x00, 0x84, 0x5A, 0x01, 0x00, 0x02],
    "ERROR": [0x5A, 0xA5, 0x07, 0x82, 0x00, 0x84, 0x5A, 0x01, 0x00, 0x03],
    "RESUMEN": [0x5A, 0xA5, 0x07, 0x82, 0x00, 0x84, 0x5A, 0x01, 0x00, 0x04],
}

def lcd_screen(command_name):
    if command_name not in LCD_CODES:
        print(f"Comando '{command_name}' no encontrado.")
        return
    
    hex_codes = LCD_CODES[command_name]
    data_size = len(hex_codes)
    
    # Configurar el puerto serie (ajusta 'COMx' a tu puerto)
    ser = serial.Serial('COMx', 9600)  # 'COMx' es el puerto serie que estás usando, 9600 es la velocidad de transmisión

    # Enviar los datos hexadecimales por UART
    for i in range(data_size):
        ser.write(bytes([hex_codes[i]]))  # Enviar el código hexadecimal como un byte

    # Cerrar la conexión al puerto serie
    ser.close()

# Ejemplo de uso
lcd_screen("INICIO")  # Enviar el comando 'INICIO'
