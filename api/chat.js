export default async function handler(req, res) {
  // Solo aceptamos peticiones POST
  if (req.method !== 'POST') return res.status(405).send('Method Not Allowed');

  const { message } = req.body;
  // Llamamos a la llave desde las variables de entorno para que sea secreta
  const apiKey = process.env.GEMINI_API_KEY;

  try {
    const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${apiKey}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{
          role: 'user',
          parts: [{ 
            // Aquí le damos el contexto a la IA de cómo debe comportarse
            text: `Eres el asistente virtual experto de EndoShop. Ayudas a doctores con información de sistemas de limas, equipos y cotizaciones. Responde de forma amable, profesional y concisa a este mensaje: ${message}` 
          }]
        }]
      })
    });

    const data = await response.json();
    const botReply = data.candidates[0].content.parts[0].text;
    
    // Devolvemos la respuesta de Gemini a tu página
    res.status(200).json({ reply: botReply });
    
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Error al conectar con el asistente.' });
  }
}