# **📌 Menú de Navegación con URLs en Python**  
**Programa interactivo que abre enlaces web desde un menú de opciones.**  

## **🚀 Características**  
✅ Menú de **6 opciones** (5 URLs + salida).  
✅ Abre enlaces en el **navegador predeterminado**.  
✅ Validación de entrada para evitar errores.  
✅ Código modular y fácil de personalizar.  

---

## **⚙️ Requisitos**  
- Python 3.6 o superior.  
- Módulo `webbrowser` (incluido en la librería estándar de Python).  

---

## **📥 Instalación**  
1. Clona el repositorio o descarga el archivo `menu_urls.py`:  
   ```sh
   git clone https://github.com/tu-usuario/menu-urls.git
   ```
2. Navega al directorio del proyecto:  
   ```sh
   cd menu-urls
   ```

---

## **▶️ Ejecución**  
```sh
python menu_urls.py
```
**Menú de opciones:**  
```
----- 🌐 MENÚ CON ENLACES -----
1. Python Oficial
2. Documentación Python
3. GitHub
4. Stack Overflow
5. ChatGPT
6. Salir
```
- Elige una opción (1-5) para abrir la URL correspondiente.  
- Opción **6** cierra el programa.  

---

## **🔧 Personalización**  
Modifica las URLs o añade nuevas opciones editando las funciones en `menu_urls.py`:  
```python
def opcion1():
    print("🔍 Has elegido la Opción 1: Python Oficial")
    webbrowser.open("https://www.python.org")  # Cambia esta URL
```

---

## **📦 Compilar a Ejecutable (.exe)**  
Usa **PyInstaller** para crear un archivo ejecutable (Windows):  
```sh
pip install pyinstaller
pyinstaller --onefile --windowed menu_urls.py
```
- El ejecutable se generará en `dist/menu_urls.exe`.  

---

## **📜 Licencia**  
Este proyecto está bajo la licencia **MIT**.  

---

## **💡 Contribuciones**  
¿Quieres mejorar el proyecto? ¡Abre un **Pull Request**!  

---

### **🔗 Enlaces Relacionados**  
- [Documentación de Python](https://docs.python.org/3/)  
- [GitHub del Proyecto](https://github.com/tu-usuario/menu-urls)  
