export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).send('Method Not Allowed');

  // Ahora recibimos el historial completo en lugar de un solo mensaje
  const { history } = req.body;
  const apiKey = process.env.GEMINI_API_KEY;

  if (!apiKey) {
    console.error("ERROR: No se encontró la GEMINI_API_KEY en las variables de entorno.");
    return res.status(500).json({ error: 'Falta la llave de la API' });
  }

  // Reglas estrictas de EndoShop
  const reglas = `Eres el asistente virtual EXCLUSIVO de EndoShop, distribuidores de la marca Fanta Dental. 
  REGLAS ESTRICTAS:
  1. TU ÚNICA MARCA ES FANTA DENTAL. 
  2. TIENES ESTRICTAMENTE PROHIBIDO mencionar, recomendar o sugerir sistemas de otras marcas o de la competencia (como ProTaper, WaveOne, Dentsply, VDW, etc.).
  3. Si el doctor pregunta por V-Taper, AF Rotary, AF Baby u otro sistema, asume siempre que se refiere a la línea de Fanta Dental y destaca sus beneficios.
  4. Si preguntan por una marca de la competencia, responde amablemente que en EndoShop se especializan exclusivamente en la tecnología de Fanta Dental y ofréceles la alternativa de tu catálogo.
  5. Eres conversacional: recuerda el contexto de los mensajes anteriores.`;

  // Construimos el paquete para Gemini: Las reglas van primero como secreto, luego el historial real
  const contents = [
    { role: 'user', parts: [{ text: reglas }] },
    { role: 'model', parts: [{ text: 'Entendido, actuaré exclusivamente como el asistente de EndoShop, defenderé la marca Fanta Dental y recordaré el historial de la conversación.' }] },
    ...history // Aquí se inyecta toda la plática que lleva con el doctor
  ];

  try {
    // Usamos gemini-1.5-flash que es el estándar más estable
    const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ contents: contents })
    });

    const data = await response.json();

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