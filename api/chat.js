export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).send('Method Not Allowed');

  const { message } = req.body;
  const apiKey = process.env.GEMINI_API_KEY;

  // 1. Revisamos si Vercel sí está leyendo la llave
  if (!apiKey) {
    console.error("ERROR: No se encontró la GEMINI_API_KEY en las variables de entorno.");
    return res.status(500).json({ error: 'Falta la llave de la API' });
  }

  try {
    const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${apiKey}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{
          role: 'user',
          parts: [{ 
            text: `Eres el asistente virtual experto de EndoShop. Ayudas a doctores con información de sistemas de limas, equipos y cotizaciones. Responde de forma amable, profesional y concisa a este mensaje: ${message}` 
          }]
        }]
      })
    });

    const data = await response.json();

    // 2. Revisamos si Google nos regresó un error (ej. llave inválida)
    if (data.error) {
      console.error("ERROR DE GOOGLE:", data.error.message);
      return res.status(500).json({ error: data.error.message });
    }

    const botReply = data.candidates[0].content.parts[0].text;
    res.status(200).json({ reply: botReply });
    
  } catch (error) {
    console.error("ERROR INTERNO:", error);
    res.status(500).json({ error: 'Error al conectar con el asistente.' });
  }
}