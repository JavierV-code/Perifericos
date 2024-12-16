import RPi.GPIO as GPIO
import time

matrix_keys = [['1', '2', '3', 'A'],
               ['4', '5', '6', 'B'],
               ['7', '8', '9', 'C'],
               ['*', '0', '#', 'D']]

keypad_rows = [2, 3, 4, 5]  # Pines GPIO para las filas
keypad_columns = [6, 7, 8, 9]  # Pines GPIO para las columnas

def asignacion():
    """Configura los pines GPIO para filas y columnas."""
    # Configurar pines de las filas como salida
    for row in keypad_rows:
        GPIO.setup(row, GPIO.OUT)
        GPIO.output(row, GPIO.LOW)  # Inicialmente apagados

    # Configurar pines de las columnas como entrada con pull-down
    for col in keypad_columns:
        GPIO.setup(col, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def main():
    """Detecta qué tecla está siendo presionada."""
    print("Ingrese el valor del teclado")
    try:
        while True:
            for row_idx, row_pin in enumerate(keypad_rows):
                # Activar una fila
                GPIO.output(row_pin, GPIO.HIGH)

                for col_idx, col_pin in enumerate(keypad_columns):
                    if GPIO.input(col_pin) == GPIO.HIGH:
                        print("Presionaste", matrix_keys[row_idx][col_idx])
                        time.sleep(0.5)  # Anti-rebote
                        
                # Desactivar la fila actual
                GPIO.output(row_pin, GPIO.LOW)
    except KeyboardInterrupt:
        print("Saliendo...")
    finally:
        GPIO.cleanup()  # Limpia la configuración de los pines

if __name__ == '__main__':
    # Configurar el modo de numeración de pines
    GPIO.setmode(GPIO.BCM)  # Usa la numeración BCM de los pines GPIO
    asignacion()
    main()
