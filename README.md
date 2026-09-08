Pinche bloque de código en la sección de Linux se quedó abierto con el triple backtick (```) mal ubicado, lo que provocó que todo el resto del texto se tragara el formato como si fuera código plano.
Reemplaza todo el contenido de tu README.md con este archivo corregido:
# 🌸 Doki Doki Study Club! (Port Android, Windows, Linux & Web) 🧁✨

[![Doki Doki Study Club tutorial](https://img.youtube.com/vi/jBb_K5g2S1E/hqdefault.jpg)](https://youtube.com/shorts/jBb_K5g2S1E)

---

> **NOTA:** Si no eres desarrollador, solo descarga el ZIP para Windows, el APK para Android o el archivo TAR para Linux que están en el enlace de Drive.

¡Bienvenido al club de literatura más caótico, sangriento y educativo del ciberespacio!

**Doki Doki Study Club!** es una adaptación interactiva inspirada en el universo de *Doki Doki Literature Club!*, reconstruida para ejecutarse como aplicación nativa en dispositivos modernos con **Android 14 (API 34) o superior**, ejecutables de escritorio independientes para **Windows (.exe)** y **Linux (ELF x64)** mediante runtime dedicado, además de correr directamente en cualquier navegador web.

Elige a tu tutora académica favorita (**Natsuki**, **Yuri**, **Monika**, **Sayori** o slots personalizados), cada una con sus propios estados emocionales dinámicos, respuestas canónicas y cerebro impulsado directamente por el modelo **Gemini 3.5 Flash** de Google.

---

## 🎀 Descarga Directa (APK, Binarios y Recursos)

Para instalar el juego sin necesidad de compilar código:

* **📁 Descargar APK y Assets:** [Google Drive - Doki Doki Study Club](https://drive.google.com/drive/folders/1wVzSWswDoSXXZhhiDiPahXRp2Vf75-rl?usp=drive_link)


### Android

* Descarga el archivo `.apk` desde el enlace de Drive.
* Ábrelo en tu dispositivo con Android 14+.
* Concede el permiso para instalar aplicaciones desde fuentes desconocidas si tu sistema te lo solicita y ¡a estudiar!


### Windows (.exe)

* Descarga el paquete para Windows (`.zip`).
* Descomprime la carpeta en cualquier ruta de tu disco.
* Ejecuta directamente `DokiDokiStudyClub.exe`.


### Linux (x86_64)

* Descarga el tarball `DokiDokiStudyClub-Linux.tar.gz`.
* Extrae el contenido en tu terminal con:

```bash
tar -xvf DokiDokiStudyClub-Linux.tar.gz
cd nwjs-v0.88.0-linux-x64
chmod +x DokiDokiStudyClub
./DokiDokiStudyClub


🔑 Despertar a las Dokis (Configuración de la API)
El juego procesa las respuestas directamente en tu dispositivo sin servidores intermediarios. Para conectar la IA necesitas una clave de acceso gratuita de Google:
Ingresa a Google AI Studio.
Inicia sesión con tu cuenta de Google y pulsa el botón Get API key.
Haz clic en Create API key y copia la cadena generada (compatible con el formato clásico AIzaSy... y el estándar AQ...).
Abre la aplicación en tu celular, escritorio o navegador y ve a la pestaña lateral Ajustes > IA & Prompts.
Pega tu clave en la casilla API Key Personal, selecciona o añade una materia y pulsa Nueva Lección.
💾 Gestión Offline y Respaldo de Materias (Exportar / Importar JSON)
Para que no pierdas tus lecciones personalizadas ni tu temario cuando no tengas conexión a internet, la interfaz incluye un sistema de respaldo directo:
⬇ Descargar Materias (JSON): Exporta un respaldo local en formato .json (materias_ddlc.json) con todas las materias predeterminadas y las agregadas manualmente.
⬆ Importar Materias (JSON): Carga un temario previamente guardado para restaurar tus cursos en cualquier dispositivo de forma instantánea.
🌐 Uso sin conexión: Todo el temario y minijuegos funcionan offline; la red solo se utiliza al realizar consultas interactivas a Gemini.
💻 Consola de Desarrollador, Diagnóstico y Easter Eggs
El juego incluye una terminal interna accesible pulsando el botón superior [ CMD ]. Admite los siguientes comandos:
checkassets: Ejecuta un escáner asíncrono sobre el catálogo completo de sprites para comprobar errores 404 o rutas rotas.
setlevel [materia] [nivel]: Modifica directamente el nivel académico registrado en el almacenamiento local para la materia indicada.
exit / quit: Cierra la ventana de la terminal de comandos.
clear / cls: Limpia los registros de la pantalla de la consola.
help: Muestra la lista de órdenes soportadas.
Easter Eggs: Comandos interactivos como sudo pacman -S cute kawai girlfriend, os.remove("monika.chr"), just monika, entre otros.
⚠️ Autopsia de Errores (Troubleshooting)
Si la sesión colapsa, la tutora en turno o la interfaz escupirán un mensaje de fallo. Aquí tienes la traducción a términos de Logcat y consola web:
Unable to open asset URL: file:///android_asset/... (Logcat de Android)
Discrepancia en mayúsculas/minúsculas (case-sensitivity) en el sistema de archivos de Android o archivo inexistente en assets/img/. Asegúrate de usar la versión parcheada de index.html donde se corrigieron las rutas de Yuri (Yurifull1.webp, Yuri_school_*.webp, Yuriinsane*.webp, YSHappy.webp, Casualclothes1-*.webp), Sayori (Ori*.webp, Sayoriii.webp) y Monika (Ika*.webp).
El API colapsó en un charco de sangre uwu. Revisa tu llave o tu conexión a internet. (Failed to fetch / NetworkError)
El paquete no llegó al servidor. La petición murió localmente porque el dispositivo no tiene conexión a red, o Android bloqueó el tráfico por faltar el permiso de red en el manifiesto.
Fallo de conexión crítico. Idiota. / Mi cerebro de silicio está frito uwu. (Error HTTP 400 / 403)
La API Key es inválida, le faltan caracteres o el cuerpo JSON de la petición fue rechazado por las políticas de Google AI Studio.
El servidor murió o las API Keys colapsaron uwu. (Error HTTP 404 / 503)
El endpoint no encontró el modelo especificado (comprueba que apunte a gemini-3.5-flash), o los servidores de Google se encuentran saturados.
ERR_CLEARTEXT_NOT_PERMITTED (Solo en Android Studio)
El sistema operativo bloqueó la conexión por intentar comunicarse mediante HTTP inseguro. Toda petición debe ir cifrada mediante HTTPS.
Lentitud o errores de GPU en Linux / WSL2 (Exiting GPU process due to errors)
Si ejecutas el port de Linux en un entorno virtualizado sin aceleración 3D nativa configurada, lanza el binario deshabilitando la GPU:
./DokiDokiStudyClub --no-sandbox --disable-gpu --in-process-gpu


🛠️ Para Desarrolladores y Modders (Compilación Local)
Clonar el repositorio
git clone https://github.com/MegatronF0id5la4yer/Doki-Doki-study-club.git


Compilación para Android (APK)
Abre Android Studio y selecciona Open en la carpeta clonada.
Comprueba que la carpeta assets contenga index.html, ai_services.js, img/ y music/ dentro de app/src/main/assets/.
Genera el binario final en Build > Build Bundle(s) / APK(s) > Build APK(s).
Compilación para Windows (.exe)
Coloca index.html, ai_services.js, img/, music/ y un package.json en una carpeta de trabajo.
Comprime esos archivos en un .zip y renómbralo a package.nw.
Descarga NW.js para Windows x64 y copia package.nw junto a nw.exe.
En la consola CMD corre:
copy /b nw.exe+package.nw DokiDokiStudyClub.exe


Compilación para Linux (x86_64)
Empaqueta los assets en Linux:
zip -r package.nw index.html ai_services.js img/ music/ package.json


Descarga y extrae los binarios de NW.js para Linux.
Fusiona los archivos:
cat nw package.nw > DokiDokiStudyClub


Asigna permisos:
chmod +x DokiDokiStudyClub


📦 Radiografía de los Componentes Clave
DokiDokiStudyClub/  
├── app/  
│   ├── src/main/  
│   │   ├── AndroidManifest.xml         # Permisos de red (INTERNET)  
│   │   ├── java/.../MainActivity.java  # Contenedor WebView con acceso a assets locales  
│   │   ├── res/                        # Iconos de la app y recursos nativos  
│   │   └── assets/                     # Núcleo del frontend portable  
│   │       ├── index.html              # Interfaz visual, CMD de diagnóstico y máquina de estados  
│   │       ├── ai_services.js          # Cliente REST modular para Gemini 3.5 Flash  
│   │       ├── img/                    # Fondos y carpetas de sprites estructuradas  
│   │       └── music/                  # BGM ambiental y pistas del club  
│   └── build.gradle                    # Target para Android 14 (API 34+)  
├── package.json                        # Manifiesto de ventana para ports de escritorio (NW.js)  
└── README.md  


⚙️ Ficha Técnica
Modelo de IA: Gemini 3.5 Flash (gemini-3.5-flash) mediante conexión directa REST.
Formato Gráfico: WebP (.webp) estructurado en 5 emociones por variante de ropa.
Respaldos: Exportación e importación de temarios en formato JSON puro.
Compatibilidad: Android 14.0 (API 34)+, Windows 10/11 (64-bit), Linux x86_64 y navegadores web modernos.
Autenticación: Encabezado HTTP x-goog-api-key universal.
Seguridad: Repositorio limpio de credenciales; cada usuario almacena su propia API Key en localStorage.

