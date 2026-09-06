# Doki Doki Study Club! (Port Oficial Android & Web)

Doki Doki Study Club! es una novela visual interactiva ambientada en el universo de Doki Doki Literature Club!, adaptada para dispositivos móviles mediante un port nativo de Android (WebView) y ejecutable también en navegadores web.

El juego integra a Natsuki como tutora de estudio personalizada gracias a la API oficial de Google Gemini, adaptando explicaciones académicas, preguntas de opción múltiple y dinámicas de estudio con su personalidad distintiva.

---

## Enlace de Descarga (APK y Recursos)

Para instalar el juego directamente en tu teléfono sin compilar nada:

* Descargar APK y Assets: https://drive.google.com/drive/folders/1wVzSWswDoSXXZhhiDiPahXRp2Vf75-rl?usp=drive_link

Descarga el archivo .apk, ábrelo en tu teléfono Android y permite la instalación de fuentes desconocidas si el sistema lo solicita.

---

## Cómo Configurar la IA para Jugar

Para que Natsuki pueda responder tus mensajes y generar las clases, necesitas una API Key gratuita de Google:

1. Entra a Google AI Studio: https://aistudio.google.com/
2. Inicia sesión con tu cuenta de Google y pulsa el botón Get API key.
3. Haz clic en Create API key y copia la clave generada (compatible tanto con el formato clásico AIzaSy como con el formato nuevo AQ...).
4. Abre la aplicación en tu celular o navegador.
5. Pega la clave en el campo API Key, escribe la materia o consulta que quieras y presiona Enviar Mensaje.

---

## Clonación y Compilación Local

Si eres desarrollador, quieres auditar el código fuente, crear un mod con otras chicas del club o generar tu propia versión del APK desde Android Studio:

### 1. Clonar el repositorio

git clone https://github.com/MegatronF0id5la4yer/Doki-Doki-study-club.git

### 2. Abrir en Android Studio

1. Abre Android Studio y selecciona Open.
2. Navega hasta la carpeta clonada y selecciónala para que Gradle sincronice el entorno.
3. Asegúrate de tener los assets web (index.html, ai_services.js, carpetas img y music) dentro de la ruta:
   app/src/main/assets/

### 3. Generar el APK

* Para pruebas rápidas: Conecta tu celular mediante depuración USB (o inicia un emulador) y presiona el botón Run 'app' (Shift + F10).
* Para exportar el instalador final: Ve al menú superior Build > Build Bundle(s) / APK(s) > Build APK(s).

---

## Desglose de Componentes Clave

DokiDokiStudyClub/
│
├── app/
│   ├── src/main/
│   │   ├── AndroidManifest.xml       # Permisos de red del sistema y asignación de temas
│   │   ├── java/.../MainActivity.java # Configuración del contenedor WebView y controles del sistema
│   │   ├── res/                      # Layouts XML, íconos de la app (mipmap) y estilos
│   │   └── assets/                   # Entorno frontend completo ejecutado dentro de la app
│   │       ├── index.html            # Interfaz de usuario, caja de chat y componentes multimedia
│   │       ├── ai_services.js        # Motor de conexión REST con la API de Gemini
│   │       ├── img/                  # Sprites de personajes, expresiones y fondos escolares
│   │       └── music/                # Música ambiental y efectos de sonido en bucle
│   └── build.gradle                  # Definición de dependencias y versiones de compilación
│
└── README.md                         # Documentación general del proyecto

### Explicación Técnica de los Archivos

* ai_services.js (Motor de IA):
  Implementa la función asíncrona enviarMensaje. Prepara las llamadas directas al endpoint v1beta de Gemini, inyecta las instrucciones del sistema (System Prompt) junto al texto del usuario, maneja los encabezados oficiales de autenticación (x-goog-api-key) y procesa las respuestas JSON descartando llaves caídas de forma automática.

* MainActivity.java (Puente Nativo Android):
  Inicializa el componente WebView e implementa las políticas de seguridad necesarias para puertos locales:
  - Habilita la ejecución de JavaScript (setJavaScriptEnabled(true)).
  - Otorga acceso a recursos locales y llamadas cruzadas (setAllowUniversalAccessFromFileURLs(true) y setAllowFileAccessFromFileURLs(true)), permitiendo que el juego haga peticiones HTTPS salientes desde el protocolo file:///android_asset/.
  - Oculta la barra de acciones superior (getSupportActionBar().hide()) para que el juego tome la pantalla completa de forma inmersiva.

* AndroidManifest.xml (Permisos del Sistema):
  Declara la regla <uses-permission android:name="android.permission.INTERNET" />, indispensable para que el kernel de Android no bloquee las peticiones salientes hacia los servidores de Google.

* index.html (Interfaz del Juego):
  Estructura el escenario visual, administra la reproducción del audio de fondo en bucle, captura los valores de los inputs (clave de API, prompt del sistema y consulta del jugador) y renderiza las respuestas en la caja de diálogo de Natsuki.

---

## Detalles Técnicos del Port

* Modelo: Gemini 3.5 Flash (gemini-3.5-flash) mediante conexión directa REST sin servidores proxy intermediarios.
* Seguridad de Llaves: Arquitectura sin credenciales hardcodeadas en código fuente ni binarios compilados; cada jugador administra su propio acceso.
* Autenticación Universal: Integración por encabezado HTTP x-goog-api-key, evitando errores de URL con las llaves emitidas por Google AI Studio (AQ... y AIzaSy).
* Soporte de Plataforma: Compatible con Android 7.0 (Nougat) en adelante y cualquier navegador web de escritorio o móvil moderno.

---

## Créditos

* Personajes, escenarios y arte original creados por Team Salvato (Doki Doki Literature Club!).
* Proyecto no oficial desarrollado sin fines de lucro con propósitos educativos.

## Créditos

* Personajes, escenarios y arte original creados por **Team Salvato** (*Doki Doki Literature Club!*).
* Proyecto no oficial desarrollado sin fines de lucro con propósitos educativos.
