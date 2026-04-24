// ============================================================
// FANTA DENTAL — productos.js
// Generado desde Catálogo México 2025
// Para actualizar: sube el nuevo PDF a Claude y pide
// "genera el productos.js actualizado con este catálogo"
// ============================================================

const products = [

  // ══════════════════════════════════════════════════════════
  // GLIDE PATH
  // ══════════════════════════════════════════════════════════

  {
    id: 1, cat: 'limas', sub: 'glide',
    name: 'C-Path #13 — Glide Path',
    tag: 'Glide Path', tagColor: '',
    desc: 'Lima rotatoria para crear un glide path seguro sin alterar la anatomía del conducto. Tamaño #13, taper 2%. Blister con 4 limas. Aleación AF-L Wire.',
    ideal: 'Conductos estrechos, obliterados o con curvaturas acentuadas. Reduce estrés en limas posteriores.',
    dif: '350 RPM / Torque 2N. No cambia la anatomía del conducto radicular.',
    campos: [
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/c-path.jpg'
  },
  {
    id: 2, cat: 'limas', sub: 'glide',
    name: 'C-Path #16 — Glide Path',
    tag: 'Glide Path', tagColor: '',
    desc: 'Lima rotatoria para crear un glide path seguro sin alterar la anatomía del conducto. Tamaño #16, taper 2%. Blister con 4 limas. Aleación AF-L Wire.',
    ideal: 'Conductos estrechos, obliterados o con curvaturas acentuadas.',
    dif: '350 RPM / Torque 2N. No cambia la anatomía del conducto radicular.',
    campos: [
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/c-path.jpg'
  },
  {
    id: 3, cat: 'limas', sub: 'glide',
    name: 'C-Path #19 — Glide Path',
    tag: 'Glide Path', tagColor: '',
    desc: 'Lima rotatoria para crear un glide path seguro sin alterar la anatomía del conducto. Tamaño #19, taper 2%. Blister con 4 limas. Aleación AF-L Wire.',
    ideal: 'Conductos estrechos, obliterados o con curvaturas acentuadas.',
    dif: '350 RPM / Torque 2N. No cambia la anatomía del conducto radicular.',
    campos: [
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/c-path.jpg'
  },

  // ══════════════════════════════════════════════════════════
  // LIMAS MANUALES
  // ══════════════════════════════════════════════════════════

  {
    id: 4, cat: 'limas', sub: 'manual',
    name: 'Limas Tipo C',
    tag: 'Manual', tagColor: 'green',
    desc: 'Limas manuales de acero al carbono para conductos muy estrechos o calcificados. Sección transversal cuadrangular. Punta semiactiva con tope de goma. Blister con 6 limas.',
    ideal: 'Preparación manual inicial de conductos estrechos, obliterados o calcificados.',
    dif: 'Acero al carbono: mayor resistencia y duración. Sección cuadrangular con excelente resistencia torsional.',
    campos: [
      { label: 'Medida', opciones: ['#06', '#08', '#10', '#12', '#15'] },
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/tipo-c.jpg'
  },
  {
    id: 5, cat: 'limas', sub: 'manual',
    name: 'Limas Tipo K — Primera Serie',
    tag: 'Manual', tagColor: 'green',
    desc: 'Limas manuales de acero inoxidable con diseño clásico tipo K. Sección transversal cuadrangular. Blister con 6 limas por medida. #15 al #40.',
    ideal: 'Apertura, exploración y permeabilización del conducto. Instrumentos de patencia.',
    dif: 'Alta resistencia torsional requerida en instrumentos de patencia.',
    campos: [
      { label: 'Medida', opciones: ['#10', '#15', '#20', '#25', '#30', '#35', '#40'] },
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/tipo-k.jpg'
  },
  {
    id: 6, cat: 'limas', sub: 'manual',
    name: 'Limas Tipo K — Segunda Serie',
    tag: 'Manual', tagColor: 'green',
    desc: 'Limas manuales de acero inoxidable con diseño clásico tipo K. Sección transversal cuadrangular. Blister con 6 limas por medida. #45 al #80.',
    ideal: 'Conformación en conductos amplios.',
    dif: 'Alta resistencia torsional y control manual preciso.',
    campos: [
      { label: 'Medida', opciones: ['#45', '#50', '#55', '#60', '#70', '#80'] },
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/tipo-k.jpg'
  },
  {
    id: 7, cat: 'limas', sub: 'manual',
    name: 'Limas Tipo H — Primera Serie',
    tag: 'Manual', tagColor: 'green',
    desc: 'Limas manuales Hedstroem de acero inoxidable. Excelente capacidad de corte traccional. Blister con 6 limas por medida. #15 al #40.',
    ideal: 'Alisado de paredes y remoción de detritus. Instrumentación de conductos ovalados.',
    dif: 'Corte traccional muy agresivo. Diseño de conos superpuestos.',
    campos: [
      { label: 'Medida', opciones: ['#15', '#20', '#25', '#30', '#35', '#40'] },
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/tipo-h.jpg'
  },
  {
    id: 8, cat: 'limas', sub: 'manual',
    name: 'Limas Tipo H — Segunda Serie',
    tag: 'Manual', tagColor: 'green',
    desc: 'Limas manuales Hedstroem de acero inoxidable. Excelente capacidad de corte traccional. Blister con 6 limas por medida. #45 al #80.',
    ideal: 'Remoción de gutapercha antigua, alisado de paredes en conductos amplios.',
    dif: 'Corte traccional muy agresivo.',
    campos: [
      { label: 'Medida', opciones: ['#45', '#50', '#55', '#60', '#70', '#80'] },
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/tipo-h.jpg'
  },
  {
    id: 9, cat: 'limas', sub: 'manual',
    name: 'V-Taper Hand File',
    tag: 'Manual', tagColor: 'green',
    desc: 'Lima manual NiTi con mango ergonómico de goma. Sistema multitaper (SX, S1, S2, F1, F2, F3). Aleación AF-L Wire con tratamiento térmico. Blister completo por longitud.',
    ideal: 'Agilizar instrumentación manual. Transición de manual a rotatorio en posgrado.',
    dif: 'NiTi tratado térmicamente para uso manual. Secuencia universal conocida.',
    campos: [
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/vtaper-hand-file.jpg'
  },

  // ══════════════════════════════════════════════════════════
  // ROTATORIAS — SISTEMAS PRINCIPALES
  // ══════════════════════════════════════════════════════════

  {
    id: 10, cat: 'limas', sub: 'conformacion',
    name: 'AF Rotary Surtido',
    tag: 'Rotatoria', tagColor: '',
    desc: 'Sistema rotatorio fabricado con aleación AF-Wire. Soporta 3,200 ciclos. Kit surtido con la secuencia clínica. Blister con 4 limas.',
    ideal: 'Manejo en conductos curvos garantizando la preservación de la anatomía.',
    dif: 'Aleación AF-Wire con tres niveles de flexibilidad.',
    campos: [
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/af-rotary.jpg'
  },
  {
    id: 11, cat: 'limas', sub: 'conformacion',
    name: 'AF Rotary — Repuestos .04',
    tag: 'Rotatoria', tagColor: '',
    desc: 'Sistema rotatorio. Aleación AF-Wire con tres niveles de flexibilidad martensítica (AF-L, AF-R, AF-H). Blister con 4 limas individuales de la medida.',
    ideal: 'Ampliación apical conservadora en conductos estrechos.',
    dif: 'Sección triangular convexa con excelente corte. 500 RPM / Torque 2.5N.',
    campos: [
      { label: 'Medida', opciones: ['#20/.04', '#25/.04', '#30/.04', '#35/.04', '#40/.04', '#45/.04', '#50/.04'] },
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/af-rotary.jpg'
  },
  {
    id: 12, cat: 'limas', sub: 'conformacion',
    name: 'AF Rotary — Repuestos .06',
    tag: 'Rotatoria', tagColor: '',
    desc: 'Sistema rotatorio. Aleación AF-Wire con tres niveles de flexibilidad martensítica (AF-L, AF-R, AF-H). Blister con 4 limas individuales de la medida.',
    ideal: 'Conformación final e irrigación eficiente.',
    dif: 'Sección triangular convexa con excelente corte. 500 RPM / Torque 2.5N.',
    campos: [
      { label: 'Medida', opciones: ['#20/.06', '#25/.06', '#30/.06', '#35/.06', '#40/.06'] },
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/af-rotary.jpg'
  },
  {
    id: 13, cat: 'limas', sub: 'conformacion',
    name: 'AF Blue S-One',
    tag: 'Rotatoria', tagColor: '',
    desc: 'Sistema rotatorio de limas únicas con excelente resistencia cíclica. Blister surtido con 3 limas (Small, Primary, Large). Aleación M-Wire + tratamiento Fase R.',
    ideal: 'Tratamientos ágiles con mínima cantidad de instrumentos.',
    dif: 'Alta flexibilidad, soporta curvas complejas sin deformarse. 500 RPM / Torque 2.5N.',
    campos: [
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/af-blue-s-one.jpg'
  },
  {
    id: 14, cat: 'limas', sub: 'conformacion',
    name: 'AF Blue S-One — Repuestos',
    tag: 'Rotatoria', tagColor: '',
    desc: 'Repuestos individuales del sistema AF Blue S-One. Blister con 3 limas de la misma medida. Aleación M-Wire + tratamiento Fase R.',
    ideal: 'Reposición de limas específicas para mantener la secuencia completa.',
    dif: 'Alta resistencia a la fatiga cíclica.',
    campos: [
      { label: 'Medida', opciones: ['Small #20/.04', 'Primary #25/.06', 'Medium #35/.04', 'Large #40/.04'] },
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/af-blue-s-one.jpg'
  },

  // ══════════════════════════════════════════════════════════
  // ROTATORIAS — MULTITAPER Y SECUENCIAS
  // ══════════════════════════════════════════════════════════

  {
    id: 15, cat: 'limas', sub: 'conformacion',
    name: 'V-Taper Gold 2023 Surtido',
    tag: 'Multitaper', tagColor: 'blue',
    desc: 'Sistema multitaper rotatorio con tratamiento térmico Gold para mayor flexibilidad. Secuencia completa: SX, S1, S2, F1, F2, F3. Blister con 6 limas.',
    ideal: 'Conductos amplios, tratamientos de conducto estándar. Curvas moderadas.',
    dif: 'Aleación CM-wire Fase H. Corte progresivo y seguro. 350 RPM / Torque 2N.',
    campos: [
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/v-taper-gold.jpg'
  },
  {
    id: 16, cat: 'limas', sub: 'conformacion',
    name: 'V-Taper Gold 2023 - Repuestos',
    tag: 'Multitaper', tagColor: 'blue',
    desc: 'Repuestos individuales del sistema V-Taper Gold 2023. Blister con 6 limas de la misma medida (SX a F3).',
    ideal: 'Reposición del instrumento de mayor desgaste en la clínica.',
    dif: 'Aleación CM-wire Fase H. 350 RPM / Torque 2N.',
    campos: [
      { label: 'Medida', opciones: ['SX (Apertura)', 'S1 (Cuerpo)', 'S2 (Cuerpo)', 'F1 (#20)', 'F2 (#25)', 'F3 (#30)'] },
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/v-taper-gold.jpg'
  },
  {
    id: 17, cat: 'limas', sub: 'conformacion',
    name: 'V-Taper Blue Surtido',
    tag: 'Multitaper', tagColor: '',
    desc: 'Sistema multitaper. Secuencia: SX, S1, S2, F1, F2, F3. Blister con 6 limas. M-Wire + tratamiento Fase R.',
    ideal: 'Conductos muy estrechos o curvos severos que requieren la máxima flexibilidad posible.',
    dif: 'Flexibilidad superior al Gold, resiste deformaciones drásticas sin fractura. 350 RPM / Torque 2N.',
    campos: [
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/vtaper-blue.jpg'
  },
  {
    id: 18, cat: 'limas', sub: 'conformacion',
    name: 'AF Blue Rotary — Secuencia',
    tag: 'Rotatoria', tagColor: '',
    desc: 'Sistema rotatorio muy flexible. Aleación M-Wire + tratamiento térmico Fase R. Secuencia: #17(12%), #19(2%), #18(5%), #25(4%), #30(4%), #35(4%). Blister con 6 limas.',
    ideal: 'Todo tipo de conductos. Sobresale en conductos estrechos con curvatura abrupta.',
    dif: 'Extraordinaria resistencia a fatiga cíclica. 500 RPM / Torque 2.5N.',
    campos: [
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/af-blue-rotary.jpg'
  },
  {
    id: 19, cat: 'limas', sub: 'conformacion',
    name: 'AF Blue S4',
    tag: 'Rotatoria', tagColor: '',
    desc: 'Sistema de conformación de 4 limas. Aleación M-Wire + tratamiento térmico Fase R. Secuencia: #15(6%), #20(4%), #25(4%), #30(4%). Blister con 4 limas.',
    ideal: 'Enfoque mínimamente invasivo. Excelentes para endodoncia de molares con conductos muy curvos.',
    dif: 'Alta conservación de la estructura radicular en tercios coronal y medio.',
    campos: [
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/af-blue-s4.jpg'
  },

  // ══════════════════════════════════════════════════════════
  // ROTATORIAS — CASOS ESPECIALES / CORTAS
  // ══════════════════════════════════════════════════════════

  {
    id: 20, cat: 'limas', sub: 'conformacion',
    name: 'Rising Rotary',
    tag: 'Rotatoria', tagColor: '',
    desc: 'Sistema corto de 3 instrumentos multitaper. Aleación M-Wire + tratamiento térmico Fase R. Secuencia: #15(6%), #20(7%), #25(8%). Caja con 3 limas. Largo 25mm.',
    ideal: 'Sistemas cortos con corte aceptable para curvaturas leve a moderada.',
    dif: 'Taper variable con énfasis apical. Ángulo helicoidal para corte más agresivo. 300–500 RPM / Torque 2N.',
    campos: [],
    img: 'images/rising-rotary.jpg'
  },
  {
    id: 21, cat: 'limas', sub: 'conformacion',
    name: 'AF F One',
    tag: 'Rotatoria', tagColor: '',
    desc: 'Sistema rotatorio con faceta plana en eje longitudinal. Aleación M-Wire + tratamiento térmico Fase R. Secuencia Clásica: #17(12%), #18(5%), #25(4%), #25(6%), #35(4%). Blister con 5 limas.',
    ideal: 'Quien prefiere sistemas rápidos y de corte agresivo. Elimina eficazmente la dentina.',
    dif: 'Faceta plana aumenta espacio para irrigante y debris. Disminuye efecto de atornillamiento. 500 RPM / Torque 2.5N.',
    campos: [
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/af-f-one.jpg'
  },
  {
    id: 22, cat: 'limas', sub: 'conformacion',
    name: 'AF F One ECO — Eco',
    tag: 'Rotatoria', tagColor: '',
    desc: 'Sistema ECO de 2 instrumentos. Secuencia: #18(5%), #30(4%). Blister con 3 piezas de cada uno. Total 6 limas.',
    ideal: 'Casos vitales de complejidad media a baja. Instrumentación rápida y económica.',
    dif: 'Aleación AFR-Wire. 500 RPM / Torque 2.5N.',
    campos: [],
    img: 'images/af-f-one-eco.jpg'
  },
  {
    id: 23, cat: 'limas', sub: 'conformacion',
    name: 'AF F One ECO — Complete',
    tag: 'Rotatoria', tagColor: '',
    desc: 'Sistema ECO de 3 instrumentos. Secuencia: #18(5%), #25(6%), #35(4%). Blister con 2 piezas de cada uno. Total 6 limas.',
    ideal: 'Casos vitales o necróticos estándar. Balance entre economía y efectividad.',
    dif: 'Aleación AFR-Wire. 500 RPM / Torque 2.5N.',
    campos: [],
    img: 'images/af-f-one-eco.jpg'
  },

  // ══════════════════════════════════════════════════════════
  // ROTATORIAS — CASOS COMPLEJOS Y GRANDES
  // ══════════════════════════════════════════════════════════

  {
    id: 24, cat: 'limas', sub: 'conformacion',
    name: 'AF Max',
    tag: 'Rotatoria', tagColor: '',
    desc: 'Instrumentos de grandes calibres para terminación. Aleación M-Wire + tratamiento Fase R. Blister con 4 limas de la misma medida o surtido.',
    ideal: 'Conformación final en dientes anteriores o palatinos/distales amplios.',
    dif: 'Calibres grandes (#40 a #60) con alta flexibilidad que no desvían la curvatura. 500 RPM / Torque 2.5N.',
    campos: [
      { label: 'Medida', opciones: ['#40/.04', '#45/.04', '#50/.04', '#55/.04', '#60/.04', 'Surtido'] },
      { label: 'Longitud', opciones: ['21mm', '25mm', '31mm'] }
    ],
    img: 'images/af-max.jpg'
  },
  {
    id: 25, cat: 'limas', sub: 'conformacion',
    name: 'AF Retreatment',
    tag: 'Retratamiento', tagColor: 'red',
    desc: 'Limas específicas para desobturación. Aleación sin tratamiento térmico para mayor rigidez. Punta semiactiva. Secuencia: D1(#30/10% 16mm), D2(#25/8% 18mm), D3(#20/6% 22mm). Blister con 3 limas.',
    ideal: 'Remoción rápida y eficaz de gutapercha y cementos selladores.',
    dif: 'D1 con punta activa para penetrar gutapercha. Rigidez controlada para avanzar en el material. 350–500 RPM / Torque 2–3N.',
    campos: [],
    img: 'images/af-retreatment.jpg'
  },

  // ══════════════════════════════════════════════════════════
  // RECIPROCANTES
  // ══════════════════════════════════════════════════════════

  {
    id: 34, cat: 'limas', sub: 'reciprocante',
    name: 'Gold Reciprocante — Blisters Individuales',
    tag: 'Reciprocante', tagColor: '',
    desc: 'Sistema reciprocante muy flexible. Aleación M-Wire + tratamiento térmico Fase R. Disponible en blisters por medida: #20(6%), #25(6%), #30/#35(4%), #40(6%). Caja con 4 limas. Largo 25mm.',
    ideal: 'Conformación rápida y efectiva con pocos instrumentos para complejidad leve a moderada.',
    dif: 'Movimiento recíproco CCW 150° / CW 30°. Mayor resistencia a la fatiga. Sección cuadrangular en glide mejora resistencia torsional.',
    campos: [
      { label: 'Medida', opciones: ['#20 / 6% / 25mm', '#25 / 6% / 25mm', '#30+#35 / 4% / 25mm', '#40 / 6% / 25mm'] }
    ],
    img: 'images/gold-reciprocante.jpg'
  },
  {
    id: 35, cat: 'limas', sub: 'reciprocante',
    name: 'Gold Reciprocante — Secuencia Surtida',
    tag: 'Reciprocante', tagColor: '',
    desc: 'Blister surtido con la secuencia completa: #17(8%), #19(2%), #20(6%), #25(6%), #40(6%). Disponible en 21mm y 25mm. Blister con 5 limas.',
    ideal: 'Secuencia completa en un solo blister. Ideal para complejidad leve a moderada.',
    dif: 'Movimiento recíproco CCW 150° / CW 30°.',
    campos: [
      { label: 'Longitud', opciones: ['21mm', '25mm'] }
    ],
    img: 'images/gold-reciprocante.jpg'
  },
  {
    id: 28, cat: 'limas', sub: 'reciprocantes',
    name: 'AF Blue R3 Surtido',
    tag: 'Reciprocante', tagColor: '',
    desc: 'Sistema reciprocante con aleación M-Wire + tratamiento Fase R. Altísima flexibilidad. Secuencia: R1(#20/.06), R2(#25/.06), R3(#40/.06). Blister con 3 limas.',
    ideal: 'Casos severamente curvos que se prefieren tratar con movimiento recíproco.',
    dif: 'Suma de resistencia recíproca con la flexibilidad extrema del tratamiento Blue.',
    campos: [
      { label: 'Longitud', opciones: ['21mm', '25mm'] }
    ],
    img: 'images/af-blue-r3.jpg'
  },
  {
    id: 29, cat: 'limas', sub: 'reciprocantes',
    name: 'R One Mini — 6 pzas',
    tag: 'Reciprocante', tagColor: '',
    desc: 'Kit reciprocante con doble tratamiento térmico. Blister de 6 piezas: 3x #17(4%) + 3x #25(6%). Largo 25mm.',
    ideal: 'Instrumentación reciprocante rápida y sencilla en curvaturas leve a moderada.',
    dif: 'Preservación de dentina pericervical. Diámetro máximo 1.1mm. Sección S Itálica.',
    campos: [],
    img: 'images/r-one-mini.jpg'
  },
  {
    id: 30, cat: 'limas', sub: 'reciprocantes',
    name: 'R One Mini — 3 pzas',
    tag: 'Reciprocante', tagColor: '',
    desc: 'Kit reciprocante. Secuencia Surtida: #17(4%), #20(6%), #25(6%). Largo 25mm.',
    ideal: 'Secuencia completa en 3 instrumentos con movimiento recíproco.',
    dif: 'Preservación de dentina pericervical. Tratamiento térmico dual.',
    campos: [],
    img: 'images/r-one-mini.jpg'
  },

  // ══════════════════════════════════════════════════════════
  // PEDIATRÍA Y CUELLO LARGO
  // ══════════════════════════════════════════════════════════

  {
    id: 31, cat: 'limas', sub: 'pediatria',
    name: 'AF Cl',
    tag: 'Especial', tagColor: '',
    desc: 'Lima rotatoria con cuello liso extralargo. Diseñada para bajar el hombro del instrumento 5mm. Medidas #20 y #25. Taper 4%. Caja con 4 piezas de 25mm.',
    ideal: 'Visualización microscópica y minimización de contacto en el tercio coronal.',
    dif: 'Cuello largo sin estrías. Disminuye la fricción coronal.',
    campos: [
      { label: 'Medida', opciones: ['#20/.04', '#25/.04'] }
    ],
    img: 'images/af-cl.jpg'
  },

  // ══════════════════════════════════════════════════════════
  // COMPLEMENTOS: GUTAPERCHA
  // ══════════════════════════════════════════════════════════

  {
    id: 32, cat: 'complementos', sub: null,
    name: 'Gutapercha Convencional (Taper 02)',
    tag: 'Complemento', tagColor: '',
    desc: 'Puntas de gutapercha estandarizadas (ISO) con taper 02%. Caja con 120 piezas por medida.',
    ideal: 'Técnicas de condensación lateral o uso como punta accesoria.',
    dif: 'Excelente radiopacidad y adaptación. No se resquebraja.',
    campos: [
      { label: 'Medida', opciones: ['#15', '#20', '#25', '#30', '#35', '#40', '#45', '#50', '#55', '#60'] }
    ],
    img: 'images/gutapercha.jpg'
  },
  {
    id: 33, cat: 'complementos', sub: null,
    name: 'Gutapercha Taper 04',
    tag: 'Complemento', tagColor: '',
    desc: 'Gutapercha obtenida de látex natural. Biocompatible, radiopaca. Caja 60 piezas por medida. Taper 04.',
    ideal: 'Obturación con sistemas rotatorios taper 04.',
    dif: 'Buena afinidad con tejidos. Fácil manipulación y compactación.',
    campos: [
      { label: 'Medida', opciones: ['20/.04', '25/.04', '30/.04', '35/.04', '40/.04', '45/.04', 'Surtido 15-40'] }
    ],
    img: 'images/gutapercha.jpg'
  },
  {
    id: 34, cat: 'complementos', sub: null,
    name: 'Gutapercha Taper 06',
    tag: 'Complemento', tagColor: '',
    desc: 'Gutapercha radiopaca, caja 60 piezas por medida. Taper 06.',
    ideal: 'Obturación de conductos instrumentados con limas taper 06.',
    dif: 'Excelente sellado tridimensional en preparaciones de mayor conicidad.',
    campos: [
      { label: 'Medida', opciones: ['20/.06', '25/.06', '30/.06', '35/.06', '40/.06', 'Surtido 15-40'] }
    ],
    img: 'images/gutapercha.jpg'
  },
  {
    id: 35, cat: 'complementos', sub: null,
    name: 'Gutapercha Serie F (F1, F2, F3)',
    tag: 'Complemento', tagColor: '',
    desc: 'Gutapercha calibrada específicamente para coincidir con las conicidades de los sistemas Gold, Blue, etc. Caja con 60 piezas.',
    ideal: 'Técnica de cono único o condensación vertical tras usar limas tipo F.',
    dif: 'Ajuste exacto apical y de conicidad (tug-back).',
    campos: [
      { label: 'Medida', opciones: ['F1', 'F2', 'F3', 'Surtida F1-F3'] }
    ],
    img: 'images/gutapercha.jpg'
  },
  {
    id: 36, cat: 'complementos', sub: null,
    name: 'Gutapercha AF Max',
    tag: 'Complemento', tagColor: '',
    desc: 'Gutapercha calibrada para el sistema AF Max. Caja con 60 piezas.',
    ideal: 'Obturación precisa tras uso del sistema AF Max.',
    dif: 'Ajuste perfecto a las preparaciones amplias de AF Max.',
    campos: [
      { label: 'Medida', opciones: ['#40', '#45', '#50', '#55'] }
    ],
    img: 'images/gutapercha.jpg'
  },
  {
    id: 37, cat: 'complementos', sub: null,
    name: 'Gutapercha AF F-One',
    tag: 'Complemento', tagColor: '',
    desc: 'Gutapercha calibrada para el sistema AF F-One. Caja con 60 piezas.',
    ideal: 'Obturación precisa tras uso del sistema de lima única AF F-One.',
    dif: 'Coincidencia exacta de dimensiones y conicidad.',
    campos: [
      { label: 'Medida', opciones: ['#20', '#25/.04', '#25/.06', '#35/.04', '#40/.04', '#45/.04', 'Surtido'] }
    ],
    img: 'images/gutapercha.jpg'
  },

  // ══════════════════════════════════════════════════════════
  // COMPLEMENTOS: PUNTAS DE PAPEL
  // ══════════════════════════════════════════════════════════

  {
    id: 38, cat: 'complementos', sub: null,
    name: 'Puntas de Papel Convencional (Taper 02)',
    tag: 'Complemento', tagColor: '',
    desc: 'Puntas de papel absorbente estandarizadas (ISO) taper 02%. Caja con 200 piezas por medida.',
    ideal: 'Secado del conducto en preparaciones manuales.',
    dif: 'Alta capacidad de absorción y consistencia para evitar deshilacharse.',
    campos: [
      { label: 'Medida', opciones: ['#15', '#20', '#25', '#30', '#35', '#40', '#45', '#50', '#55', '#60'] }
    ],
    img: 'images/puntas-papel.jpg'
  },
  {
    id: 39, cat: 'complementos', sub: null,
    name: 'Puntas de Papel Taper 04',
    tag: 'Complemento', tagColor: '',
    desc: 'Puntas de papel de alta absorción, sin aglutinantes químicos. Caja con 100 piezas por medida.',
    ideal: 'Secado del conducto previo a obturar con sistemas taper 04.',
    dif: 'Alta absorción. Amplia variedad de medidas.',
    campos: [
      { label: 'Medida', opciones: ['25/.04', '30/.04', '35/.04', '40/.04', '45/.04'] }
    ],
    img: 'images/puntas-papel.jpg'
  },
  {
    id: 40, cat: 'complementos', sub: null,
    name: 'Puntas de Papel Taper 06',
    tag: 'Complemento', tagColor: '',
    desc: 'Puntas de papel de alta absorción. Caja con 100 piezas por medida.',
    ideal: 'Secado del conducto previo a obturar con sistemas taper 06.',
    dif: 'Secado eficiente, reduce la necesidad de usar múltiples conos.',
    campos: [
      { label: 'Medida', opciones: ['20/.06', '25/.06', '30/.06', '35/.06', '40/.06'] }
    ],
    img: 'images/puntas-papel.jpg'
  },
  {
    id: 41, cat: 'complementos', sub: null,
    name: 'Puntas de Papel Serie F (F1, F2, F3)',
    tag: 'Complemento', tagColor: '',
    desc: 'Puntas de papel calibradas para sistemas de cono tipo F (Gold, Blue). Caja con 100 piezas.',
    ideal: 'Secado exacto tras instrumentación con limas F.',
    dif: 'Seca la porción apical al instante gracias al ajuste de conicidad.',
    campos: [
      { label: 'Medida', opciones: ['F1', 'F2', 'F3', 'Surtidas F1-F3'] }
    ],
    img: 'images/puntas-papel.jpg'
  },
  {
    id: 42, cat: 'complementos', sub: null,
    name: 'Puntas de Papel AF Max',
    tag: 'Complemento', tagColor: '',
    desc: 'Puntas de papel calibradas para sistema AF Max. Caja con 100 piezas.',
    ideal: 'Secado de preparaciones amplias.',
    dif: 'No dejan residuos en el conducto.',
    campos: [
      { label: 'Medida', opciones: ['#40', '#45', '#50', '#55'] }
    ],
    img: 'images/puntas-papel.jpg'
  },
  {
    id: 43, cat: 'complementos', sub: null,
    name: 'Puntas de Papel AF F-One',
    tag: 'Complemento', tagColor: '',
    desc: 'Puntas de papel calibradas para sistema AF F-One. Caja con 100 piezas.',
    ideal: 'Secado eficiente para preparaciones de lima única.',
    dif: 'Ajuste ideal al tamaño final del AF F-One.',
    campos: [
      { label: 'Medida', opciones: ['#20', '#25/.04', '#25/.06', '#35/.04', '#40/.04', '#45/.04', 'Surtido'] }
    ],
    img: 'images/puntas-papel.jpg'
  },

  // ══════════════════════════════════════════════════════════
  // COMPLEMENTOS: INSTRUMENTAL
  // ══════════════════════════════════════════════════════════

  {
    id: 44, cat: 'complementos', sub: null,
    name: 'GP-Plugger / Espaciador (G-1)',
    tag: 'Instrumental', tagColor: '',
    desc: 'Espaciador manual (Hand Plugger). Lado NiTi: #35/.03. Lado Acero: #70/.02. Color del cuerpo: NEGRO.',
    ideal: 'Condensación vertical de gutapercha.',
    dif: 'Doble extremo (NiTi superflexible y Acero rígido).',
    campos: [],
    img: 'images/gp-plugger.jpg'
  },
  {
    id: 45, cat: 'complementos', sub: null,
    name: 'GP-Plugger / Espaciador (G-2)',
    tag: 'Instrumental', tagColor: '',
    desc: 'Espaciador manual (Hand Plugger). Lado NiTi: #40/.03. Lado Acero: #80/.02. Color del cuerpo: ROJO.',
    ideal: 'Condensación vertical de gutapercha.',
    dif: 'Doble extremo (NiTi superflexible y Acero rígido).',
    campos: [],
    img: 'images/gp-plugger.jpg'
  },
  {
    id: 46, cat: 'complementos', sub: null,
    name: 'GP-Plugger / Espaciador (G-3)',
    tag: 'Instrumental', tagColor: '',
    desc: 'Espaciador manual (Hand Plugger). Lado NiTi: #50/.03. Lado Acero: #100/.02. Color del cuerpo: AZUL.',
    ideal: 'Condensación vertical de gutapercha.',
    dif: 'Doble extremo (NiTi superflexible y Acero rígido).',
    campos: [],
    img: 'images/gp-plugger.jpg'
  },
  {
    id: 47, cat: 'complementos', sub: null,
    name: 'GP-Plugger / Espaciador (G-4)',
    tag: 'Instrumental', tagColor: '',
    desc: 'Espaciador manual (Hand Plugger). Lado NiTi: #60/.03. Lado Acero: #120/.02. Color del cuerpo: DORADO/BLANCO.',
    ideal: 'Condensación vertical de gutapercha en tercios coronales.',
    dif: 'Doble extremo (NiTi superflexible y Acero rígido).',
    campos: [],
    img: 'images/gp-plugger.jpg'
  },
  {
    id: 48, cat: 'complementos', sub: null,
    name: 'Agujas de Irrigación Laterales',
    tag: 'Complemento', tagColor: '',
    desc: 'Agujas estériles (30G) con doble ventilación lateral y punta cerrada/redondeada. Irrigación segura. Paquete con 50 piezas. Disponibles en 22mm y 27mm.',
    ideal: 'Irrigación segura y profunda del sistema de conductos.',
    dif: 'Evita presión apical directa durante la irrigación.',
    campos: [
      { label: 'Longitud', opciones: ['22mm', '27mm'] }
    ],
    img: 'images/agujas-irrigacion.jpg'
  },
  {
    id: 49, cat: 'complementos', sub: null,
    name: 'C-Handle',
    tag: 'Instrumental', tagColor: '',
    desc: 'Mango ergonómico para limas manuales. Facilita la instrumentación bajo microscopio o en piezas posteriores. Conector integrado para localizador.',
    ideal: 'Endodoncia bajo visión microscópica.',
    dif: 'Compatible con limas C, K y H. Autoclavable.',
    campos: [],
    img: 'images/c-handle.jpg'
  },

  // ══════════════════════════════════════════════════════════
  // EQUIPOS
  // ══════════════════════════════════════════════════════════

  {
    id: 57, cat: 'equipos', sub: null,
    name: 'Actor 1 Pro - Activador Ultrasónico',
    tag: 'Equipo', tagColor: 'orange',
    desc: 'Dispositivo de activación ultrasónica. Batería de 1600 mAh. Carga y control inalámbrico. Puntas con tratamiento térmico superflexibles.',
    ideal: 'Potenciación de los irrigantes intracanal y mejora de la desinfección.',
    dif: 'Completamente portátil e inalámbrico. Puntas superflexibles por tratamiento térmico. LED mejora visibilidad.',
    campos: [
      { label: 'Tips incluidos', opciones: ['3 tips E98', '3 tips EL96'] }
    ],
    img: 'images/actor-1-pro.jpg'
  },
  {
    id: 58, cat: 'equipos', sub: null,
    name: 'Motor Endodóntico IRoot Pro',
    tag: 'Equipo', tagColor: 'orange',
    desc: 'Motor endodóntico portátil inalámbrico con localizador de ápice integrado. 10 ajustes de memoria + comienzo rápido. Modo reciprocante completamente ajustable. Compatible con la mayoría de sistemas del mercado.',
    ideal: 'Flujo clínico eficiente integrando motor + localizador en un solo dispositivo.',
    dif: 'Motor + localizador en uno. Sincronización de datos en pantalla. No requiere accesorios adicionales.',
    campos: [],
    img: 'images/iroot-pro.jpg'
  },
  {
    id: 59, cat: 'equipos', sub: null,
    name: 'Wispex Localizador',
    tag: 'Equipo', tagColor: 'orange',
    desc: 'Localizador de ápice de alta resolución con tecnología de doble frecuencia. Alta precisión en conductos secos y húmedos. Punto de referencia ajustable. Autocalibración.',
    ideal: 'Determinación precisa de la longitud de trabajo en cualquier condición del conducto.',
    dif: 'Pantalla clara y tecnología avanzada de doble frecuencia para evitar falsos positivos.',
    campos: [],
    img: 'images/wispex.jpg'
  },

  // ══════════════════════════════════════════════════════════
  // NUEVOS PRODUCTOS 2025
  // ══════════════════════════════════════════════════════════
  {
    id: 60, cat: 'limas', sub: 'pediatria',
    name: 'AF Baby Rotary',
    tag: 'Odontopediatría', tagColor: 'blue',
    desc: 'Sistema rotatorio pediátrico diseñado específicamente para la anatomía de los dientes deciduos. Kit doble.',
    ideal: 'Tratamientos pulpares en pacientes infantiles, agilizando el tiempo en el sillón.',
    dif: 'Tamaño y conicidad adaptados para raíces primarias. Funciona a 350 RPM.',
    campos: [
      { label: 'Presentación', opciones: ['Kit Doble Surtido'] }
    ],
    img: 'images/af-baby.jpg'
  },
  {
    id: 61, cat: 'limas', sub: 'retratamiento',
    name: 'Limas de Retratamiento',
    tag: 'Desobturación', tagColor: 'red',
    desc: 'Limas rotatorias diseñadas con punta activa y estrías agresivas para la rápida remoción de gutapercha y cementos selladores.',
    ideal: 'Casos de fracaso endodóntico donde se requiere permeabilizar el conducto nuevamente.',
    dif: 'Diseño específico para desobturación eficiente minimizando el riesgo de perforación.',
    campos: [
      { label: 'Presentación', opciones: ['Kit Surtido D1-D3'] }
    ],
    img: 'images/af-retreatment.jpg'
  },
  {
    id: 62, cat: 'limas', sub: 'kits',
    name: 'Essential Kit selected by Styleitaliano',
    tag: 'Kit Premium', tagColor: 'teal',
    desc: 'Kit colaborativo avalado por Styleitaliano Endodontics. Incluye la secuencia esencial para resolver la mayoría de los retos clínicos con el estándar más alto.',
    ideal: 'Odontólogos que buscan protocolos estandarizados y avalados por referentes mundiales.',
    dif: 'Selección curada por expertos internacionales. Aleaciones de máxima flexibilidad.',
    campos: [
      { label: 'Tipo de Kit', opciones: ['Standard Kit', 'Complete Kit'] }
    ],
    img: 'images/essential-kit.jpg'
  },
  {
    id: 63, cat: 'equipos', sub: null,
    name: 'Microscopio Quirúrgico MCS 3000A',
    tag: 'Microscopio', tagColor: 'orange',
    desc: 'Microscopio operatorio con sistema de imagen FULL HD 1080p integrado. Múltiples opciones de magnificación (3.2X a 20X) y lente objetivo de enfoque fino (200-400mm).',
    ideal: 'Endodoncia microscópica, localización de conductos MB2, manejo de perforaciones y microcirugía apical.',
    dif: 'Barril ocular plegable (0-210°). Recubrimiento antibacteriano de iones de nano plata.',
    campos: [],
    img: 'images/microscopio-mc3000a.jpg'
  }
];