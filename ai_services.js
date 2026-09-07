async function enviarMensaje(modelo, apiKey, promptUsuario, promptSistema) {
    if (!apiKey || apiKey.trim() === "") {
        throw new Error("No hay API Key. El cerebro de silicio está desconectado.");
    }

    const urlAPI = `https://generativelanguage.googleapis.com/v1beta/models/${modelo}:generateContent?key=${apiKey}`;

    const cuerpoPeticion = {
        system_instruction: {
            parts: [{ text: promptSistema }]
        },
        contents: [
            {
                role: "user",
                parts: [{ text: promptUsuario }]
            }
        ]
    };

    try {
        const response = await fetch(urlAPI, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'x-goog-api-key': apiKey
            },
            body: JSON.stringify(cuerpoPeticion)
        });

        if (!response.ok) {
            const errorBody = await response.text();
            throw new Error(`Error HTTP ${response.status}: ${errorBody}`);
        }

        const data = await response.json();

        if (data.candidates && data.candidates[0].content && data.candidates[0].content.parts[0].text) {
            return data.candidates[0].content.parts[0].text.trim();
        } else {
            throw new Error("Respuesta inválida. La API devolvió un cuerpo vacío o deforme.");
        }

    } catch (error) {
        throw new Error(`Fallo de conexión crítico: ${error.message}`);
    }
}