import webbrowser

def opcion1():
    print("🔍 Has elegido la Opción 1: Python Oficial")
    webbrowser.open("https://www.python.org")

def opcion2():
    print("📚 Has elegido la Opción 2: Documentación de Python")
    webbrowser.open("https://docs.python.org/3/")

def opcion3():
    print("💻 Has elegido la Opción 3: GitHub")
    webbrowser.open("https://github.com")

def opcion4():
    print("🎓 Has elegido la Opción 4: Stack Overflow")
    webbrowser.open("https://stackoverflow.com")

def opcion5():
    print("🚀 Has elegido la Opción 5: ChatGPT")
    webbrowser.open("https://chat.openai.com")

def mostrar_menu():
    print("\n----- 🌐 MENÚ CON ENLACES -----")
    print("1. Python Oficial")
    print("2. Documentación Python")
    print("3. GitHub")
    print("4. Stack Overflow")
    print("5. ChatGPT")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("\nElige una opción (1-6): "))
            if opcion == 1:
                opcion1()
            elif opcion == 2:
                opcion2()
            elif opcion == 3:
                opcion3()
            elif opcion == 4:
                opcion4()
            elif opcion == 5:
                opcion5()
            elif opcion == 6:
                print("👋 Saliendo del programa...")
                break
            else:
                print("❌ Error: Ingresa un número del 1 al 6.")
        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")

if __name__ == "__main__":
    main()
