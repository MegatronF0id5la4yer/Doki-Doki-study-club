Doki Doki Study Club! (Port Oficial para Android & Web)
Doki Doki Study Club! es una adaptación interactiva en formato de novela visual ambientada en el universo de Doki Doki Literature Club!. El proyecto funciona tanto en navegadores web de escritorio/móviles como de forma nativa en Android mediante un contenedor WebView optimizado en Android Studio.

Integra directamente a Natsuki como tutora de estudio personalizada impulsada por la API oficial de Google Gemini, adaptando explicaciones académicas, preguntas de opción múltiple y dinámicas de estudio con su personalidad distintiva.

Características Principales
Port Nativo para Android: Empaquetado como APK autónomo utilizando Android Studio. Configurado con bypass de directivas locales de CORS (allowUniversalAccessFromFileURLs) para permitir peticiones externas sin necesidad de un backend intermediario.

Integración con Gemini 3.5 Flash: Conexión directa a través de la API v1beta de Google Generative Language (gemini-3.5-flash), garantizando respuestas inmediatas y bajo consumo de recursos.

Soporte para Nuevas Claves de API: Manejo nativo mediante encabezados HTTP (x-goog-api-key), compatible tanto con las claves tradicionales (AIzaSy...) como con el nuevo estándar de Google AI Studio (AQ...).

Seguridad y Privacidad: El cliente no almacena llaves hardcodeadas. Cada usuario ingresa su propia credencial directamente en la interfaz, protegiendo las cuotas personales contra extracción en binarios.

Diseño Responsivo: Interfaz adaptada con controles táctiles, selector de proveedores de IA y panel de diálogo dinámico con sprites y música de fondo.

Descarga de Recursos y APK
Los archivos fuente compilados, el instalador APK listo para pruebas y los assets multimedia del proyecto se encuentran alojados en la siguiente carpeta compartida:

Google Drive: Descargar Recursos y APK del Proyecto

Arquitectura y Estructura de Archivos
Plaintext
DokiDokiStudyClub/
│
├── app/
│   ├── src/main/
│   │   ├── AndroidManifest.xml       # Permisos de red (INTERNET) y definición de tema
│   │   ├── java/.../MainActivity.java # Configuración del WebView y descarte del ActionBar
│   │   ├── res/                      # Recursos visuales, layouts y temas de Android
│   │   └── assets/                   # Raíz del frontend local ejecutado por el WebView
│   │       ├── index.html            # Interfaz principal, selectores y contenedores de audio/texto
│   │       ├── ai_services.js        # Lógica de conexión REST directa con Gemini
│   │       ├── img/                  # Sprites de personajes, poses y fondos de aula
│   │       └── music/                # Pistas de audio ambiental y efectos de sonido
│   └── build.gradle                  # Configuración de compilación para la plataforma Android
│
└── README.md                         # Documentación del repositorio
Componentes Clave
ai_services.js: Contiene la función asíncrona enviarMensaje. Prepara el payload con contents, inyecta el promptSistema junto a la consulta del usuario y despacha la petición al endpoint de Gemini procesando la respuesta en tiempo real.

MainActivity.java: Inicializa el componente WebView, habilita la ejecución de JavaScript, otorga permisos para peticiones salientes desde el protocolo file:/// y oculta la barra superior del sistema para una experiencia en pantalla completa.

AndroidManifest.xml: Otorga la directiva <uses-permission android:name="android.permission.INTERNET" /> requerida por el kernel de Android para el tráfico HTTP/HTTPS saliente.

Guía de Configuración para Jugadores
Para habilitar las respuestas de Natsuki en tu teléfono o navegador:

Ingresa a Google AI Studio.

Inicia sesión con tu cuenta de Google y haz clic en Get API key.

Selecciona Create API key y copia la cadena generada (comience con AIzaSy o AQ.).

Abre la aplicación, pega tu clave en el campo API Key, define la materia o duda que deseas estudiar y presiona Enviar Mensaje.

Compilación Local desde Android Studio
Si deseas clonar y compilar el proyecto manualmente:

Clona este repositorio:

Bash
git clone https://github.com/MegatronF0id5la4yer/Doki-Doki-study-club.git
Abre la carpeta del proyecto dentro de Android Studio.

Asegúrate de que los archivos web (index.html, ai_services.js, carpetas img y music) residan dentro de app/src/main/assets/.

Conecta tu dispositivo Android mediante depuración USB o inicia un emulador.

Haz clic en Run 'app' (Shift + F10) o genera el binario final en Build > Build Bundle(s) / APK(s) > Build APK(s).

Créditos y Licencias
Basado en los personajes y assets del videojuego original Doki Doki Literature Club! por Team Salvato.

Desarrollado con fines educativos y de entretenimiento. Este proyecto no está afiliado oficialmente con Team Salvato ni con Google.
