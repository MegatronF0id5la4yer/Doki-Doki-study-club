Markdown
# 🌸 Doki Doki Study Club! (Port Android, Windows, Linux & Web) 🧁✨

[![Doki Doki Study Club tutorial](https://img.youtube.com/vi/jBb_K5g2S1E/hqdefault.jpg)](https://youtube.com/shorts/jBb_K5g2S1E)

¡Bienvenido al club de literatura más caótico y educativo del ciberespacio!  
**Doki Doki Study Club!** es una adaptación interactiva inspirada en el universo de *Doki Doki Literature Club!*, reconstruida para ejecutarse como aplicación nativa en dispositivos modernos con **Android 14 (API 34) o superior**, ejecutables de escritorio independientes para **Windows (.exe)** y **Linux (ELF x64)** mediante runtime dedicado, además de correr directamente en cualquier navegador web.

Elige a tu tutora académica favorita (**Natsuki**, **Yuri**, **Monika**, **Sayori** o slots personalizados), cada una con sus propios estados emocionales dinámicos, respuestas canónicas y cerebro impulsado directamente por el modelo **Gemini 3.5 Flash** de Google.

---

## 🎀 Descarga Directa (APK, Binarios y Recursos)

Para instalar el juego sin necesidad de compilar código:

* 📂 **Descargar APK y Assets:** [Google Drive - Doki Doki Study Club](https://drive.google.com/drive/folders/1wVzSWswDoSXXZhhiDiPahXRp2Vf75-rl?usp=drive_link)

### Android
1. Descarga el archivo `.apk` desde el enlace de Drive.
2. Ábrelo en tu dispositivo con **Android 14+**.
3. Concede el permiso para instalar aplicaciones desde fuentes desconocidas si tu sistema te lo solicita y ¡a estudiar!

### Windows (.exe)
1. Descarga el paquete para Windows (`.zip`).
2. Descomprime la carpeta en cualquier ruta de tu disco.
3. Ejecuta directamente `DokiDokiStudyClub.exe`.

### Linux (x86_64)
1. Descarga el tarball `DokiDokiStudyClub-Linux.tar.gz`.
2. Extrae el contenido en tu terminal:
   ```bash
   tar -xvf DokiDokiStudyClub-Linux.tar.gz
   cd nwjs-v0.88.0-linux-x64
Otorga permisos de ejecución si es necesario y lánzalo:

Bash
chmod +x DokiDokiStudyClub
./DokiDokiStudyClub
🔑 Despertar a las Dokis (Configuración de la API)
El juego procesa las respuestas directamente en tu dispositivo sin servidores intermediarios. Para conectar la IA necesitas una clave de acceso gratuita de Google:

Ingresa a Google AI Studio: https://aistudio.google.com/

Inicia sesión con tu cuenta de Google y pulsa el botón Get API key.

Haz clic en Create API key y copia la cadena generada (compatible con el formato clásico AIzaSy... y el estándar AQ...).

Abre la aplicación en tu celular, escritorio o navegador y ve a la pestaña lateral Ajustes > IA & Prompts.

Pega tu clave en la casilla API Key Personal, selecciona o añade una materia y pulsa Nueva Lección.

💻 Consola de Desarrollador, Diagnóstico y Easter Eggs
El juego incluye una terminal interna accesible pulsando el botón superior [ CMD ]. Admite los siguientes comandos:

checkassets: Ejecuta un escáner asíncrono sobre el catálogo completo de sprites del juego para comprobar que ningún archivo devuelva error 404 o rutas rotas.

setlevel [materia] [nivel]: Modifica directamente el nivel académico registrado en el almacenamiento local para la materia indicada.

exit / quit: Cierra la ventana de la terminal de comandos.

clear / cls: Limpia los registros de la pantalla de la consola.

help: Muestra la lista de órdenes soportadas.

Easter Eggs: Comandos ocultos interactivos (sudo pacman -S cute kawai girlfriend, os.remove("monika.chr"), just monika, entre otros).

⚠️ Autopsia de Errores (Troubleshooting)
Si la sesión colapsa, la tutora en turno o la interfaz escupirán un mensaje de fallo. Aquí tienes la traducción a términos de Logcat y consola web:

"Unable to open asset URL: file:///android_asset/..." (Logcat de Android)

Causa técnica: Discrepancia en mayúsculas/minúsculas (case-sensitivity) en el sistema de archivos de Android o archivo inexistente en assets/img/. Asegúrate de usar la versión parcheada de index.html donde se corrigieron las rutas de Yuri (Yurifull1.webp, Yuri_school_*.webp, Yuriinsane*.webp, YSHappy.webp, Casualclothes1-*.webp), Sayori (Ori*.webp, Sayoriii.webp) y Monika (Ika*.webp).

"El API colapsó en un charco de sangre uwu. Revisa tu llave o tu conexión a internet."

Causa técnica (Failed to fetch / NetworkError): El paquete no llegó al servidor. La petición murió localmente porque el dispositivo no tiene conexión a red, o Android bloqueó el tráfico por faltar el permiso de red en el manifiesto.

"Fallo de conexión crítico. Idiota." / "Mi cerebro de silicio está frito uwu."

Causa técnica (Error HTTP 400 / 403): La API Key es inválida, le faltan caracteres o el cuerpo JSON de la petición fue rechazado por las políticas de Google AI Studio.

"El servidor murió o las API Keys colapsaron uwu."

Causa técnica (Error HTTP 404 / 503): El endpoint no encontró el modelo especificado (comprueba que apunte a gemini-3.5-flash), o los servidores de Google se encuentran temporalmente saturados.

ERR_CLEARTEXT_NOT_PERMITTED (Solo en Android Studio)

El sistema operativo bloqueó la conexión por intentar comunicarse mediante HTTP inseguro. Toda petición debe ir cifrada mediante HTTPS.

Lentitud o errores de GPU en Linux / WSL2 (Exiting GPU process due to errors)

Si ejecutas el port de Linux en un entorno virtualizado sin aceleración 3D nativa configurada, ejecuta el binario deshabilitando la GPU por hardware:

Bash
./DokiDokiStudyClub --no-sandbox --disable-gpu --in-process-gpu
🛠️ Para Desarrolladores y Modders (Compilación Local)
Si deseas modificar los prompts, integrar nuevos trajes, añadir pistas de audio o generar tus propios paquetes:

1. Clonar el repositorio
Bash
git clone [https://github.com/MegatronF0id5la4yer/Doki-Doki-study-club.git](https://github.com/MegatronF0id5la4yer/Doki-Doki-study-club.git)
2. Compilación para Android (APK)
Abre Android Studio y selecciona Open en la carpeta clonada.

Comprueba que la carpeta assets contenga todo el frontend (index.html, ai_services.js, img/, music/) dentro de:

Plaintext
app/src/main/assets/
Genera el binario final en Build > Build Bundle(s) / APK(s) > Build APK(s).

3. Compilación para Windows (.exe)
Coloca index.html, ai_services.js, img/, music/ y un package.json en una carpeta de trabajo.

Comprime los archivos en un .zip y renómbralo a package.nw.

Descarga la versión Windows x64 de NW.js y copia package.nw junto a nw.exe.

Fusiona ambos archivos mediante la consola de comandos de Windows (CMD):

DOS
copy /b nw.exe+package.nw DokiDokiStudyClub.exe
4. Compilación para Linux (x86_64)
Desde tu terminal de Linux o Arch en WSL2, empaqueta los assets:

Bash
zip -r package.nw index.html ai_services.js img/ music/ package.json
Descarga y extrae los binarios de Linux de NW.js.

Concatena el binario nw con tu paquete .nw:

Bash
cat nw package.nw > DokiDokiStudyClub
chmod +x DokiDokiStudyClub
📦 Radiografía de los Componentes Clave
Plaintext
DokiDokiStudyClub/
│
├── app/
│   ├── src/main/
│   │   ├── AndroidManifest.xml        # Permisos de red (INTERNET)
│   │   ├── java/.../MainActivity.java  # Contenedor WebView con acceso a assets locales
│   │   ├── res/                       # Iconos de la app y recursos nativos
│   │   └── assets/                    # Núcleo del frontend portable
│   │       ├── index.html             # Interfaz visual, CMD de diagnóstico y máquina de estados
│   │       ├── ai_services.js         # Cliente REST modular para Gemini 3.5 Flash
│   │       ├── img/                   # Fondos y carpetas de sprites estructuradas
│   │       │   ├── bg/
│   │       │   ├── natsuki escuela/
│   │       │   ├── natsuki casual/
│   │       │   ├── yuri escuela/
│   │       │   ├── yuri casual/
│   │       │   ├── monika escuela/
│   │       │   ├── sayori escuela/
│   │       │   ├── sayori casual/
│   │       │   └── personaje personalizado 1..5/
│   │       └── music/                 # BGM ambiental y pistas del club
│   └── build.gradle                   # Target para Android 14 (API 34+)
│
├── package.json                       # Manifiesto de ventana para ports de escritorio (NW.js)
└── README.md
Funcionamiento Interno
ai_services.js (Motor de IA Modular):

Implementa la función asíncrona enviarMensaje(modelo, apiKey, promptUsuario, promptSistema). Prepara el payload contents, autentica mediante el encabezado x-goog-api-key y entrega el contenido limpio listo para parsear en JSON.

index.html (Lógica y Frontend Universal):

Maneja la selección de tutoras, el cambio dinámico de atuendos escolares/casuales, el mapeo de los 5 estados de ánimo (normal, pensando, examen, feliz, molesta), la terminal integrada de diagnóstico y la persistencia de niveles vía localStorage.

package.json (Runtime de Escritorio):

Define dimensiones de pantalla (1280x720 centrado), título de ventana y comportamiento nativo para las versiones compiladas de Windows y Linux.

MainActivity.java (Puente WebView Android):

Configura el navegador embebido habilitando JavaScript (setJavaScriptEnabled(true)) y otorgando acceso cruzado a los recursos empaquetados (setAllowFileAccessFromFileURLs(true) y setAllowUniversalAccessFromFileURLs(true)), permitiendo peticiones HTTPS hacia Google AI desde file:///android_asset/.

AndroidManifest.xml (Permisos Android):

Declara <uses-permission android:name="android.permission.INTERNET" /> para permitir la salida de tráfico hacia las APIs de Google.

⚙️ Ficha Técnica
Modelo de IA: Gemini 3.5 Flash (gemini-3.5-flash) mediante conexión directa REST.

Formato Gráfico: WebP (.webp) estructurado en 5 emociones por variante de ropa.

Compatibilidad:

Android: Android 14.0 (API 34) o superior.

Windows: Windows 10 / 11 (64-bit).

Linux: Distribuciones x86_64 con GLIBC 2.31+ y librerías base GTK3/Mesa.

Web: Navegadores modernos basados en Chromium o Firefox.

Autenticación: Encabezado HTTP x-goog-api-key universal.

Seguridad: Repositorio y binarios limpios de claves; cada usuario gestiona su propia API Key en almacenamiento local (localStorage).
