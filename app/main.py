# app/main.py
import calculator

def mostrar_menu():
    print("\n--- CALCULADORA TPO TESTING ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def run():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción (1-5): ")

        if opcion == '5':
            print("Saliendo de la aplicación. ¡Chau!")
            break

        if opcion in ['1', '2', '3', '4']:
            try:
                # Pedimos los números al usuario
                n1 = float(input("Ingresá el primer número: "))
                n2 = float(input("Ingresá el segundo número: "))

                if opcion == '1':
                    print(f">> Resultado de la suma: {calculator.add(n1, n2)}")
                elif opcion == '2':
                    print(f">> Resultado de la resta: {calculator.subtract(n1, n2)}")
                elif opcion == '3':
                    print(f">> Resultado de la multiplicación: {calculator.multiply(n1, n2)}")
                elif opcion == '4':
                    # Aquí es donde el test de "Caso de Error" va a ser útil
                    print(f">> Resultado de la división: {calculator.divide(n1, n2)}")
            
            except ValueError as e:
                # Captura tanto errores de letras en vez de números como la división por cero
                print(f">> ERROR: {e}")
            except Exception as e:
                print(f">> Ocurrió un error inesperado: {e}")
        else:
            print("Opción no válida, intentá de nuevo.")

if __name__ == "__main__":
    run()