# 🌸 Doki Doki Study Club! (Port Android & Web) 🧁✨

¡Bienvenido al club de literatura más caótico y educativo del ciberespacio!  
**Doki Doki Study Club!** es una adaptación interactiva inspirada en el universo de *Doki Doki Literature Club!*, reconstruida para ejecutarse como aplicación nativa en dispositivos modernos con **Android 14 (API 34) o superior**, además de correr directamente en cualquier navegador web.

Nuestra querida y gruñona **Natsuki** toma el papel de tutora académica personalizada, impulsada directamente por el modelo **Gemini 3.5 Flash** de Google.

---

## 🎀 Descarga Directa (APK y Recursos)

Para instalar el juego en tu teléfono sin necesidad de compilar código:

* 📂 **Descargar APK y Assets:** https://drive.google.com/drive/folders/1wVzSWswDoSXXZhhiDiPahXRp2Vf75-rl?usp=drive_link

1. Descarga el paquete `.apk` desde el enlace de Drive.
2. Ábrelo en tu dispositivo con **Android 14+**.
3. Concede el permiso para instalar aplicaciones desde fuentes desconocidas si tu sistema te lo solicita y ¡a estudiar!

---

## 🔑 Cómo Despertar a Natsuki (Configuración de la API)

El juego procesa las respuestas directamente en tu dispositivo sin intermediarios. Para darle vida al cerebro de silicio de Natsuki necesitas una clave de acceso gratuita de Google:

1. Ingresa a **Google AI Studio**: https://aistudio.google.com/
2. Inicia sesión con tu cuenta de Google y pulsa el botón **Get API key**.
3. Haz clic en **Create API key** y copia la cadena generada (funciona tanto con el formato clásico `AIzaSy...` como con el estándar moderno `AQ...`).
4. Abre la aplicación en tu celular o navegador.
5. Pega tu clave en la casilla **API Key**, elige o escribe la materia que quieres aprender y presiona **Enviar Mensaje**.

---

## 🛠️ Para Desarrolladores y Modders (Compilación Local)

Si quieres inspeccionar las entrañas del proyecto, cambiar la música, agregar a Monika, Yuri o Sayori, o generar tu propio binario firmado:

### 1. Clonar el repositorio
git clone https://github.com/MegatronF0id5la4yer/Doki-Doki-study-club.git

### 2. Abrir en Android Studio
1. Abre Android Studio y pulsa en **Open**.
2. Selecciona la carpeta del proyecto para que Gradle descargue las dependencias y sincronice el entorno.
3. Verifica que la carpeta `assets` contenga todo el frontend (`index.html`, `ai_services.js`, carpetas `img` y `music`) en:
   app/src/main/assets/

### 3. Compilar el APK
* **Prueba rápida:** Conecta tu dispositivo con Android 14 por depuración USB y presiona **Run 'app'** (`Shift + F10`).
* **Generar paquete final:** Ve al menú superior **Build > Build Bundle(s) / APK(s) > Build APK(s)**.

---

## 📦 Radiografía de los Componentes Clave

DokiDokiStudyClub/
│
├── app/
│   ├── src/main/
│   │   ├── AndroidManifest.xml       # Permisos de red INTERNET y temas del sistema
│   │   ├── java/.../MainActivity.java # Contenedor WebView con soporte de red local
│   │   ├── res/                      # Íconos mipmap, layouts XML y estilos visuales
│   │   └── assets/                   # Entorno web ejecutado por la aplicación
│   │       ├── index.html            # Interfaz visual del club, sprites y cajas de texto
│   │       ├── ai_services.js        # Motor de conexión REST directa con Gemini 3.5 Flash
│   │       ├── img/                  # Expresiones, poses de Natsuki y fondos del aula
│   │       └── music/                # Temas ambientales y efectos de sonido en loop
│   └── build.gradle                  # Configuración orientada a Android 14 (API 34+)
│
└── README.md                         # Documentación del club

### Funcionamiento Interno

* **`ai_services.js` (Lógica de IA):**  
  Implementa la función asíncrona `enviarMensaje`. Prepara el payload `contents`, inyecta el `promptSistema` con la personalidad tsundere de Natsuki y conecta directamente con el endpoint `v1beta` utilizando el encabezado `x-goog-api-key`. Si una llave es inválida o falla, el sistema maneja la excepción sin colapsar la interfaz.

* **`MainActivity.java` (Puente Android):**  
  Monta un contenedor `WebView` blindado para la ejecución local:
  - Activa la ejecución de scripts (`setJavaScriptEnabled(true)`).
  - Habilita las políticas `setAllowUniversalAccessFromFileURLs(true)` y `setAllowFileAccessFromFileURLs(true)` para permitir llamadas salientes HTTPS desde el protocolo `file:///android_asset/`.
  - Oculta el `ActionBar` superior para ofrecer una experiencia en pantalla completa limpia y envolvente.

* **`AndroidManifest.xml` (Permisos):**  
  Otorga la directiva `<uses-permission android:name="android.permission.INTERNET" />` para que el sistema operativo permita el tráfico saliente hacia los servidores de Google.

* **`index.html` (Escenario del Club):**  
  Controla los eventos multimedia, el bucle de la banda sonora, los cuadros de diálogo interactivos y la captura de credenciales del jugador.

---

## ⚙️ Ficha Técnica

* **Modelo de IA:** Gemini 3.5 Flash (`gemini-3.5-flash`) mediante conexión directa REST.
* **Compatibilidad:** Android 14.0 (API 34) o superior; navegadores web modernos (Chrome, Firefox, Brave, Edge).
* **Autenticación:** Encabezado HTTP `x-goog-api-key` universal (compatible con prefijos `AQ...` y `AIzaSy...`).
* **Seguridad:** Repositorio y binarios 100% limpios de credenciales hardcodeadas; cada usuario administra su cuota.

---

## 📄 Créditos y Descargo de Responsabilidad

* Personajes, escenarios, música y recursos gráficos pertenecen originalmente a **Team Salvato** (*Doki Doki Literature Club!*).
* Este es un proyecto tributo de código abierto, desarrollado sin fines de lucro con propósitos educativos y de entretenimiento. No existe afiliación oficial con Team Salvato ni con Google.
