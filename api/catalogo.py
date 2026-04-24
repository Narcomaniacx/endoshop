"""
catalogo.py
-----------
Generador de catálogo PDF estilo Fanta Dental para EndoShop.
Diseño: portada dividida, índice, páginas por familia de producto, contraportada.

Uso local:
    python catalogo.py

Dependencias:
    pip install reportlab
"""

import json
import os
import io
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib.utils import ImageReader


# =============================================================================
# COLORES (extraídos del logo EndoShop)
# =============================================================================
class C:
    TEAL        = colors.HexColor("#4a9b8e")   # teal principal del logo
    TEAL_DARK   = colors.HexColor("#2d7268")   # teal oscuro
    TEAL_LIGHT  = colors.HexColor("#e0f2ef")   # teal muy claro para fondos
    ORANGE      = colors.HexColor("#E8962A")   # naranja del logo
    ORANGE_LIGHT= colors.HexColor("#fef3e2")
    WHITE       = colors.white
    GRAY_LIGHT  = colors.HexColor("#f8fafb")
    GRAY_MID    = colors.HexColor("#dde6e8")
    GRAY_TEXT   = colors.HexColor("#4a6670")
    GRAY_DARK   = colors.HexColor("#1e3035")
    BLACK       = colors.black


# =============================================================================
# DIMENSIONES
# =============================================================================
PAGE_W, PAGE_H = A4          # 595 x 842 pts
MARGIN         = 18 * mm
COL_L          = 52          # ancho columna izquierda teal
COL_R_X        = COL_L + 14  # inicio columna derecha
COL_R_W        = PAGE_W - COL_L - 28  # ancho útil columna derecha


# =============================================================================
# FAMILIAS DE PRODUCTOS
# Define cómo se agrupan los productos del JSON en páginas del catálogo.
# Cada familia = una página.
# "ids" son los ids del JSON que se agrupan en esa página.
# =============================================================================
FAMILIES = [
    # LIMAS — GLIDE PATH
    {
        "title": "C-Path — Glide Path",
        "cat_label": "Glide Path",
        "ids": [1, 2, 3],
        "img": "images/c-path.jpg",
        "desc": (
            "Lima rotatoria para crear un glide path seguro sin alterar la "
            "anatomia del conducto. Alea cion AF-L Wire. 350 RPM / Torque 2N. "
            "Tip inactivo, stopper de silicona. Blister con 4 limas por medida."
        ),
        "features": [
            "Aleacion AF-L Wire de alta flexibilidad",
            "No altera la anatomia del conducto radicular",
            "Tip no cortante para evitar escalones",
            "Ideal para conductos estrechos, obliterados o con curvaturas acentuadas",
        ],
        "specs_header": ["Medida", "Taper", "21mm", "25mm", "31mm", "Piezas/Blister"],
        "specs_rows": [
            ["C-Path #13", "02", "✓", "✓", "✓", "4"],
            ["C-Path #16", "02", "✓", "✓", "✓", "4"],
            ["C-Path #19", "02", "✓", "✓", "✓", "4"],
        ],
        "precio": "$650 c/u",
    },

    # LIMAS — MANUALES: Tipo C
    {
        "title": "Limas Tipo C (C-Flex)",
        "cat_label": "Limas Manuales",
        "ids": [4],
        "img": "images/tipo-c.jpg",
        "desc": (
            "Lima manual C-Flex de acero inoxidable de alta calidad. "
            "Tip especial para negociar conductos calcificados y curvos. "
            "Aumenta la posibilidad de acceso en casos dificiles."
        ),
        "features": [
            "Tip agudo para conductos calcificados",
            "Alta flexibilidad comparada con limas K estandar",
            "Acero inoxidable de alta resistencia",
        ],
        "specs_header": ["Serie", "Medidas ISO", "Longitudes", "Piezas/Caja"],
        "specs_rows": [
            ["Pequenas", "#06 — #10", "21 / 25 / 31mm", "6"],
            ["Medianas", "#15 — #40", "21 / 25 / 31mm", "6"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — MANUALES: Tipo K
    {
        "title": "Limas Tipo K — Natro Hand Files",
        "cat_label": "Limas Manuales",
        "ids": [5, 6],
        "img": "images/tipo-k.jpg",
        "desc": (
            "Lima tipo K de acero inoxidable con sistema de doble codigo de color. "
            "Mango ergonomico antideslizante. Alta capacidad de corte. "
            "Compatible con localizador de apice en el mango (C-Handle)."
        ),
        "features": [
            "Codigo de color Natro para identificacion rapida",
            "Mango antideslizante de material especial",
            "Marcas de profundidad a 18, 19, 20 y 22mm",
            "Stopper de silicona incluido",
        ],
        "specs_header": ["Serie", "Medidas ISO", "Longitudes", "Piezas/Caja"],
        "specs_rows": [
            ["Primera", "#06 — #40", "21 / 25 / 31mm", "6"],
            ["Segunda", "#45 — #80", "21 / 25 / 31mm", "6"],
            ["Tercera", "#90 — #140", "21 / 25 / 31mm", "6"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — MANUALES: Tipo H
    {
        "title": "Limas Tipo H — Hedstroem",
        "cat_label": "Limas Manuales",
        "ids": [7, 8],
        "img": "images/tipo-h.jpg",
        "desc": (
            "Lima Hedstroem de acero inoxidable con alto poder de corte en movimiento "
            "de traccion. Ideal para conductos relativamente rectos e irregulares. "
            "Ventaja sobre NiTi en anatomias complejas no curvadas."
        ),
        "features": [
            "Alto poder de corte por traccion",
            "Acero inoxidable resistente",
            "Recomendada para conductos rectos e irregulares",
        ],
        "specs_header": ["Serie", "Medidas ISO", "Longitudes", "Piezas/Caja"],
        "specs_rows": [
            ["Primera", "#06 — #40", "21 / 25 / 31mm", "6"],
            ["Segunda", "#45 — #80", "21 / 25 / 31mm", "6"],
            ["Tercera", "#90 — #140", "21 / 25 / 31mm", "6"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — MANUALES: V-Taper Hand
    {
        "title": "V-Taper Hand File",
        "cat_label": "Limas Manuales",
        "ids": [9],
        "img": "images/vtaper-hand-file.jpg",
        "desc": (
            "Lima manual con diseno especial de taper variable. "
            "Complemento ideal del sistema V-Taper Gold rotatorio. "
            "Alta flexibilidad para anatomias curvadas."
        ),
        "features": [
            "Taper variable para mayor eficiencia",
            "Diseno compatible con sistema V-Taper Gold",
        ],
        "specs_header": ["Medida", "Taper", "Longitudes", "Piezas/Caja"],
        "specs_rows": [
            ["#15 — #40", "Variable", "21 / 25 / 31mm", "6"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — CONFORMACION: AF Rotary
    {
        "title": "AF Rotary",
        "cat_label": "Conformacion",
        "ids": [10, 11, 12, 13, 14],
        "img": "images/af-rotary.jpg",
        "desc": (
            "Lima rotatoria con tecnologia AF-H Wire de extrema flexibilidad. "
            "Ideal para conductos muy estrechos, calcificados y con curvaturas severas. "
            "Reserva mas dentina. 350-400 RPM."
        ),
        "features": [
            "AF-H Wire: maxima flexibilidad disponible",
            "600% mas resistencia a fatiga ciclica vs NiTi convencional",
            "Diseno que preserva mas dentina",
            "Tip no cortante para evitar iatrogenias",
            "Stopper y marcas de profundidad incluidos",
        ],
        "specs_header": ["Medida", "Taper", "21mm", "25mm", "31mm", "Piezas/Caja"],
        "specs_rows": [
            ["20/04", "04", "✓", "✓", "✓", "6"],
            ["25/04", "04", "✓", "✓", "✓", "6"],
            ["30/04", "04", "✓", "✓", "✓", "6"],
            ["Secuencia corta", "04", "✓", "✓", "✓", "5"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — CONFORMACION: AF Blue S One
    {
        "title": "AF Blue S One",
        "cat_label": "Conformacion",
        "ids": [15, 16, 17],
        "img": "images/af-blue-s-one.jpg",
        "desc": (
            "Lima rotatoria con tecnologia AF-R Wire y seccion transversal en S. "
            "Minimamente invasiva. Mayor resistencia a fatiga ciclica. "
            "Adecuada para conductos normales a anchos."
        ),
        "features": [
            "AF-R Wire Blue alloy tech",
            "Seccion en S: menos masa, menos estres torsional",
            "Mayor espacio para irrigacion durante la preparacion",
            "Disponible en Taper 04 y Taper 06",
        ],
        "specs_header": ["Medida", "Taper", "21mm", "25mm", "31mm", "Piezas/Caja"],
        "specs_rows": [
            ["20/04", "04", "✓", "✓", "✓", "3"],
            ["25/04", "04", "✓", "✓", "✓", "3"],
            ["35/04", "04", "✓", "✓", "✓", "3"],
            ["20/06", "06", "✓", "✓", "✓", "3"],
            ["25/06", "06", "✓", "✓", "✓", "3"],
            ["35/06", "06", "✓", "✓", "✓", "3"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — CONFORMACION: AF Blue Rotary
    {
        "title": "AF Blue Rotary",
        "cat_label": "Conformacion",
        "ids": [18, 19],
        "img": "images/af-blue-rotary.jpg",
        "desc": (
            "Sistema rotatorio con tecnologia AF-R Wire. Seccion triangular "
            "convexa. Amplio rango de medidas para la mayoria de los casos. "
            "Sistema S4 recomendado para secuencia completa."
        ),
        "features": [
            "AF-R Wire de control avanzado",
            "Seccion triangular convexa, mejor corte",
            "Sistema de secuencia S4 disponible",
            "Marcas de profundidad a 18, 19, 20, 22mm",
        ],
        "specs_header": ["Medida", "Taper", "21mm", "25mm", "31mm", "Piezas/Caja"],
        "specs_rows": [
            ["15/04", "04", "✓", "✓", "✓", "6"],
            ["20/04", "04", "✓", "✓", "✓", "6"],
            ["25/04", "04", "✓", "✓", "✓", "6"],
            ["25/06", "06", "✓", "✓", "✓", "6"],
            ["35/04", "04", "✓", "✓", "✓", "6"],
            ["40/06", "06", "✓", "✓", "✓", "6"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — CONFORMACION: AF Blue S4
    {
        "title": "AF Blue S4",
        "cat_label": "Conformacion",
        "ids": [20, 21],
        "img": "images/af-blue-s4.jpg",
        "desc": (
            "Kit de secuencia S4 con limas AF Blue. Diseno optimizado para la "
            "mayoria de los casos clinicos. Cuatro limas en secuencia logica "
            "para una preparacion eficiente y segura."
        ),
        "features": [
            "Secuencia de 4 limas para la mayoria de casos",
            "AF-R Wire technology",
            "Compatible con limas individuales de la serie AF Blue",
        ],
        "specs_header": ["Secuencia", "Medidas", "Longitudes", "Piezas/Kit"],
        "specs_rows": [
            ["S4 Kit", "Path + 25/06 + 35/04", "21 / 25 / 31mm", "4"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — CONFORMACION: VTaper Blue
    {
        "title": "VTaper Blue Rotary File",
        "cat_label": "Conformacion",
        "ids": [22],
        "img": "images/vtaper-blue.jpg",
        "desc": (
            "Lima rotatoria de taper variable con tecnologia Blue alloy. "
            "Combina las ventajas del sistema V-Taper con la flexibilidad "
            "superior del alambre azul AF-R."
        ),
        "features": [
            "Taper variable para mayor eficiencia",
            "AF-R Wire Blue alloy",
            "Alta resistencia a fatiga ciclica",
        ],
        "specs_header": ["Medida", "Taper", "Longitudes", "Piezas/Caja"],
        "specs_rows": [
            ["Variable", "Variable", "21 / 25 / 31mm", "6"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — CONFORMACION: V-Taper Gold
    {
        "title": "V-Taper Gold Rotary",
        "cat_label": "Conformacion",
        "ids": [23, 24],
        "img": "images/v-taper-gold.jpg",
        "desc": (
            "Sistema de 6 limas: 3 de conformacion (AF-R Wire) y 3 de "
            "finalizacion (AF-H Wire). Diseno de taper variable. "
            "Seccion triangular convexa. Movimiento rotatorio continuo."
        ),
        "features": [
            "3 limas de conformacion + 3 de finalizacion",
            "S-shapes / Finishers AF-H Wire para maxima flexibilidad",
            "Taper variable especialmente disenado",
            "Stopper de goma y marcas de profundidad",
        ],
        "specs_header": ["Lima", "Taper", "21mm", "25mm", "31mm", "Piezas/Caja"],
        "specs_rows": [
            ["SX #19", "02vt", "✓", "—", "—", "6"],
            ["S1 #18", "02vt", "✓", "✓", "✓", "—"],
            ["S2 #20", "04vt", "✓", "✓", "✓", "—"],
            ["F1 #20", "07vt", "✓", "✓", "✓", "—"],
            ["F2 #25", "08vt", "✓", "✓", "✓", "—"],
            ["F3 #30", "09vt", "✓", "✓", "✓", "6 (set)"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — CONFORMACION: Rising Rotary
    {
        "title": "Rising Rotary File",
        "cat_label": "Conformacion",
        "ids": [25],
        "img": "images/rising-rotary.jpg",
        "desc": (
            "Lima rotatoria con geometria de corte progresivo. "
            "Diseno optimizado para una preparacion rapida y segura "
            "en la mayoria de anatomias clinicas."
        ),
        "features": [
            "Geometria de corte progresivo",
            "Alta eficiencia en preparacion",
            "Disponible en multiples medidas",
        ],
        "specs_header": ["Medida", "Taper", "Longitudes", "Piezas/Caja"],
        "specs_rows": [
            ["20 — 40", "04 / 06", "21 / 25 / 31mm", "6"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — CONFORMACION: AF F One
    {
        "title": "AF F One",
        "cat_label": "Conformacion",
        "ids": [26, 27, 28, 29],
        "img": "images/af-f-one.jpg",
        "desc": (
            "Lima de archivo unico con tecnologia AF-R Wire y diseno flat "
            "lateral unico. Superior eficiencia de corte. Alta resistencia "
            "a fatiga ciclica. Seleccionada por Style Italiano Endodontics."
        ),
        "features": [
            "AF-R Wire technology",
            "Diseno flat lateral: reduce estres torsional y masa",
            "Mayor espacio para irrigacion",
            "Facilita el bypass si hay fractura",
            "Seleccionada por Style Italiano Endodontics",
        ],
        "specs_header": ["Medida", "Taper", "21mm", "25mm", "31mm", "Piezas/Caja"],
        "specs_rows": [
            ["F1 #20", "04", "✓", "✓", "✓", "3"],
            ["F2 #25", "04", "✓", "✓", "✓", "3"],
            ["F3 #35", "04", "✓", "✓", "✓", "3"],
            ["F4 #20", "06", "✓", "✓", "✓", "3"],
            ["F5 #25", "06", "✓", "✓", "✓", "3"],
            ["F6 #35", "06", "✓", "✓", "✓", "3"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — CONFORMACION: AF F One ECO
    {
        "title": "AF F One ECO",
        "cat_label": "Conformacion",
        "ids": [30, 31],
        "img": "images/af-f-one-eco.jpg",
        "desc": (
            "Version economica del sistema AF F One. Misma tecnologia de "
            "alambre y diseno flat lateral. Opcion accesible para mayor "
            "volumen de casos sin sacrificar calidad."
        ),
        "features": [
            "Misma tecnologia que AF F One",
            "Diseno flat lateral",
            "Precio accesible para alto volumen",
        ],
        "specs_header": ["Medida", "Taper", "Longitudes", "Piezas/Caja"],
        "specs_rows": [
            ["#25", "04 / 06", "21 / 25 / 31mm", "3"],
            ["#35", "04 / 06", "21 / 25 / 31mm", "3"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — FINISHER: AF Max
    {
        "title": "AF Max 3 Rotary — Finisher",
        "cat_label": "Finisher",
        "ids": [32],
        "img": "images/af-max.jpg",
        "desc": (
            "Lima finalizadora con taper variable maximo 04. Especializada "
            "en limpieza y remocion de smear layer. Transporta hipoloclorito "
            "hasta la longitud de trabajo. No modifica la forma de la preparacion. "
            "800 RPM / Torque 1N."
        ),
        "features": [
            "Taper maximo 04 (#25): no cambia la forma de preparacion",
            "Transporta NaOCl hasta el apice",
            "Remueve detritus y smear layer eficientemente",
            "800 RPM / Torque 1N",
            "1 lima por tubo (uso controlado)",
        ],
        "specs_header": ["Referencia", "Tip", "Taper", "21mm", "25mm", "31mm"],
        "specs_rows": [
            ["AF Max 1", "#25", "01-04", "✓", "✓", "✓"],
            ["AF Max 2", "#25", "01-04", "✓", "✓", "✓"],
            ["AF Max 3", "#25", "01-04", "✓", "✓", "✓"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — RETRATAMIENTO
    {
        "title": "AF Retreatment Rotary",
        "cat_label": "Retratamiento",
        "ids": [33],
        "img": "images/af-retreatment.jpg",
        "desc": (
            "Sistema de 3 limas para retratamiento endodontico. "
            "AF-R Wire. Seccion en diamante. Secuencia por tercios "
            "(coronal, medio, apical) para remocion eficiente de "
            "material de obturacion."
        ),
        "features": [
            "AF-R Wire technology",
            "Seccion transversal en diamante",
            "Secuencia de 3 limas por tercios del conducto",
            "Surtido de 3 limas por caja",
        ],
        "specs_header": ["Lima", "Taper", "Tip", "Longitud", "Piezas/Caja"],
        "specs_rows": [
            ["Retreatment 1", "07", "#20", "21mm", "6"],
            ["Retreatment 2", "08", "#25", "18mm", "6"],
            ["Retreatment 3", "09", "#30", "16mm", "6"],
            ["Surtido 3 en 1", "07/08/09", "20/25/30", "Todas", "3"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — RECIPROCANTES: Gold Reciprocante
    {
        "title": "Gold Reciprocante",
        "cat_label": "Reciprocantes",
        "ids": [34, 35],
        "img": "images/gold-reciprocante.jpg",
        "desc": (
            "Lima reciprocante con tecnologia Gold alloy para maxima "
            "flexibilidad. Movimiento reciprocante (CW/CCW). "
            "Ideal para la mayoria de anatomias incluyendo curvaturas severas."
        ),
        "features": [
            "Gold alloy: extrema flexibilidad",
            "Movimiento reciprocante (CW 150 / CCW 30)",
            "Disponible en blisters individuales y surtidos",
        ],
        "specs_header": ["Medida", "Taper", "Longitudes", "Piezas/Blister"],
        "specs_rows": [
            ["R20", "Reciproc", "21 / 25 / 31mm", "3"],
            ["R40", "Reciproc", "21 / 25 / 31mm", "3"],
            ["R50", "Reciproc", "21 / 25 / 31mm", "3"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — RECIPROCANTES: AF Blue R3
    {
        "title": "AF Blue R3",
        "cat_label": "Reciprocantes",
        "ids": [36, 37],
        "img": "images/af-blue-r3.jpg",
        "desc": (
            "Lima reciprocante AF-R Wire con seccion rectangular. "
            "Sistema de lima unica. Disponible en 3 medidas para "
            "conductos normales, estrechos y anchos."
        ),
        "features": [
            "AF-R Wire Blue alloy",
            "Seccion rectangular: menos agresiva con la pared",
            "3 medidas cubren la mayoria de anatomias",
            "Movimiento reciprocante",
        ],
        "specs_header": ["Referencia", "Tip", "Taper", "21mm", "25mm", "31mm"],
        "specs_rows": [
            ["R3-R1 (estrecho)", "#20", "06", "✓", "✓", "✓"],
            ["R3-R2 (normal)", "#25", "06", "✓", "✓", "✓"],
            ["R3-R3 (ancho)", "#40", "06", "✓", "✓", "✓"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — RECIPROCANTES: R One Mini Kit
    {
        "title": "R One Mini Kit",
        "cat_label": "Reciprocantes",
        "ids": [38, 39],
        "img": "images/r-one-mini.jpg",
        "desc": (
            "Kit mini de lima reciprocante. Presentacion compacta ideal "
            "para consultorio. Disponible en kit de 3 y de 6 piezas."
        ),
        "features": [
            "Presentacion compacta",
            "Kit de 3 o 6 piezas",
            "Movimiento reciprocante",
        ],
        "specs_header": ["Kit", "Medidas", "Longitudes", "Piezas"],
        "specs_rows": [
            ["Mini 3 pzas", "25/06", "21 / 25 / 31mm", "3"],
            ["Mini 6 pzas", "25/06", "21 / 25 / 31mm", "6"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — ESPECIALES: AF CL
    {
        "title": "AF CL System",
        "cat_label": "Especiales",
        "ids": [40],
        "img": "images/af-cl.jpg",
        "desc": (
            "Sistema especial para bypass y manejo de escalones. "
            "AF-R Wire con tip pre-doblado. Seccion en diamante. "
            "Movimiento reciprocante recomendado (CW 90-150 / CCW 30)."
        ),
        "features": [
            "Tip pre-doblado para bypass de escalones",
            "AF-R Wire technology",
            "Seccion en diamante",
            "Disponible en version rotatoria y manual",
            "Marcas de profundidad a 18, 19, 20, 22mm",
        ],
        "specs_header": ["Medida", "Taper", "21mm", "25mm", "31mm", "Piezas/Caja"],
        "specs_rows": [
            ["10/06", "06", "✓", "✓", "✓", "6"],
            ["15/06", "06", "✓", "✓", "✓", "6"],
            ["10/08", "08", "✓", "✓", "✓", "6"],
            ["20/07", "07", "✓", "✓", "✓", "6"],
            ["25/08", "08", "✓", "✓", "✓", "6"],
            ["30/09", "09", "✓", "✓", "✓", "6"],
            ["Surtido 6 en 1", "—", "✓", "✓", "✓", "6"],
        ],
        "precio": "Consultar",
    },

    # LIMAS — ESPECIALES: AF Baby Rotary
    {
        "title": "AF Baby Rotary",
        "cat_label": "Especiales",
        "ids": [41, 42],
        "img": "images/af-baby.jpg",
        "desc": (
            "Lima rotatoria especial para dientes primarios. AF-H Wire. "
            "16mm de longitud. Tip no cortante. Resistencia mejorada a "
            "fatiga ciclica para mayor seguridad en pacientes pediatricos."
        ),
        "features": [
            "16mm de longitud: disenada para dientes primarios",
            "AF-H Wire: maxima flexibilidad",
            "Resistencia mejorada a fatiga ciclica",
            "Open File #17/08 incluido en kit",
            "Elegir Taper 04 para curvaturas, 06 para conductos mas anchos",
        ],
        "specs_header": ["Medida", "Taper", "Longitud", "Piezas/Caja"],
        "specs_rows": [
            ["20/04", "04", "16mm", "6"],
            ["25/04", "04", "16mm", "6"],
            ["30/04", "04", "16mm", "6"],
            ["20/06", "06", "16mm", "6"],
            ["25/06", "06", "16mm", "6"],
            ["30/06", "06", "16mm", "6"],
        ],
        "precio": "Consultar",
    },

    # COMPLEMENTOS: Gutapercha
    {
        "title": "Gutapercha",
        "cat_label": "Complementos",
        "ids": [43, 44, 45, 46, 47, 48],
        "img": "images/gutapercha.jpg",
        "desc": (
            "Puntas de gutapercha ISO. Alta radiopacidad. Biocompatibles. "
            "Buena flexibilidad para acceso en conductos estrechos y curvados. "
            "Disponibles en multiple tapers compatibles con todos los sistemas "
            "de preparacion del catalogo."
        ),
        "features": [
            "Alta radiopacidad para verificacion radiografica",
            "Biocompatibles bajo estandar estricto",
            "Flexibilidad para conductos curvos",
            "Compatibles con V-Taper Gold, AF F One, Rising, Reciproc",
        ],
        "specs_header": ["Serie", "Taper", "Medidas", "Piezas/Caja"],
        "specs_rows": [
            ["ISO Taper 02", "02%", "#15 — #120 (surtida)", "120"],
            ["ISO Taper 04", "04%", "#15 — #120", "60"],
            ["ISO Taper 06", "06%", "#15 — #120", "60"],
            ["V-Taper Gold", "04% / 06%", "F1 — F5", "60"],
            ["Rising", "04% / 06%", "Compatible", "60"],
            ["Accesoria", "02%", "Fina", "120"],
        ],
        "precio": "Consultar",
    },

    # COMPLEMENTOS: Puntas de Papel
    {
        "title": "Puntas de Papel",
        "cat_label": "Complementos",
        "ids": [49, 50, 51],
        "img": "images/puntas-papel.jpg",
        "desc": (
            "Puntas de papel absorbentes. Superficie lisa para maxima "
            "absorcion. Taper disenado para cada sistema de preparacion. "
            "Permiten mejor adhesion del sellador y material de obturacion."
        ),
        "features": [
            "Alta capacidad de absorcion",
            "Superficie lisa",
            "Compatibles con todos los sistemas de preparacion",
        ],
        "specs_header": ["Serie", "Taper", "Medidas", "Piezas/Caja"],
        "specs_rows": [
            ["Taper 04", "04%", "#15 — #120", "100 — 200"],
            ["Taper 06", "06%", "#15 — #120", "100 — 200"],
            ["Serie F", "04% / 06%", "F1 — F5", "100"],
        ],
        "precio": "Consultar",
    },

    # COMPLEMENTOS: GP Plugger
    {
        "title": "GP Plugger",
        "cat_label": "Complementos",
        "ids": [52, 53],
        "img": "images/gp-plugger.jpg",
        "desc": (
            "Plugger de condensacion disponible en acero inoxidable y NiTi. "
            "Marcas de longitud ISO. Codigo de color estandar. "
            "Doble punta para dos medidas en un solo instrumento."
        ),
        "features": [
            "Disponible en acero inoxidable y NiTi flexible",
            "Marcas de longitud ISO",
            "Codigo de color estandar",
            "Doble punta: dos medidas por instrumento",
        ],
        "specs_header": ["Material", "Presentacion", "Medidas"],
        "specs_rows": [
            ["Acero inoxidable", "Kit completo / Individual", "ISO estandar"],
            ["NiTi", "Kit completo / Individual", "Para conductos curvos"],
        ],
        "precio": "Consultar",
    },

    # COMPLEMENTOS: Agujas de Irrigacion
    {
        "title": "Agujas de Irrigacion",
        "cat_label": "Complementos",
        "ids": [54],
        "img": "images/agujas-irrigacion.jpg",
        "desc": (
            "Agujas de irrigacion de pared delgada con dos vents laterales "
            "y punta redondeada. Permiten irrigacion segura a toda la longitud "
            "del conducto sin riesgo de extruusion apical."
        ),
        "features": [
            "Dos vents laterales para irrigacion segura",
            "Punta cerrada y redondeada",
            "Pared delgada: mejor caudal y flexibilidad",
            "Pre-doblar para conductos curvos",
        ],
        "specs_header": ["Tipo", "Punta", "Compatibilidad"],
        "specs_rows": [
            ["Doble vent lateral", "Cerrada / Redondeada", "Jeringas estandar"],
        ],
        "precio": "Consultar",
    },

    # COMPLEMENTOS: C-Handle
    {
        "title": "C-Handle",
        "cat_label": "Complementos",
        "ids": [55],
        "img": "images/c-handle.jpg",
        "desc": (
            "Mango especial compatible con limas manuales estandar. "
            "Diseno largo para ampliar el campo visual bajo microscopio. "
            "Conector integrado para localizador de apice. "
            "Esterilizable en autoclave."
        ),
        "features": [
            "Compatible con limas K, H, C y pluggers/spreaders",
            "Diseno largo: mejora campo visual bajo microscopio",
            "Conector integrado para localizador de apice",
            "Superficie antideslizante con puntos en relieve",
            "Autoclavable",
        ],
        "specs_header": ["Caracteristica", "Detalle"],
        "specs_rows": [
            ["Compatibilidad", "Limas ISO estandar, plugger, spreader"],
            ["Esterilizacion", "Autoclave"],
            ["Conector apice", "Integrado en extremo superior"],
        ],
        "precio": "Consultar",
    },

    # EQUIPOS: Microscopio
    {
        "title": "Microscopio MCS 3000A",
        "cat_label": "Equipos",
        "ids": [56],
        "img": "images/microscopio-mc3000a.jpg",
        "desc": (
            "Microscopio MC Files especialmente disenado para tratamiento "
            "endodontico. Alta resolucion. Iluminacion LED. "
            "Ampliacion multinivel. Mejora la eficiencia y calidad del "
            "tratamiento al visualizar estructuras finas del conducto."
        ),
        "features": [
            "Alta resolucion con sistema de iluminacion estable",
            "Ampliacion multinivel",
            "Mejora el campo visual en acceso a la camara pulpar",
            "Compatible con MC Files para tratamiento bajo microscopio",
        ],
        "specs_header": ["Caracteristica", "Detalle"],
        "specs_rows": [
            ["Modelo", "MCS 3000A"],
            ["Iluminacion", "LED integrado"],
            ["Amplificacion", "Multinivel"],
        ],
        "precio": "Consultar",
    },

    # EQUIPOS: Actor 1 Pro
    {
        "title": "Actor 1 Pro — Activador Ultrasonico",
        "cat_label": "Equipos",
        "ids": [57],
        "img": "images/actor-1-pro.jpg",
        "desc": (
            "Activador ultrasonico endodontico inalambrico. Dos modos de "
            "potencia. Bateria 1600mAh. Luz LED frontal. Carga inalambrica. "
            "Tecnologia ultrasonica silenciosa de pequena amplitud y gran potencia."
        ),
        "features": [
            "Modo regular y alta potencia",
            "Bateria 1600mAh de larga duracion",
            "Luz LED frontal para mejor vision",
            "Carga inalambrica",
            "Ultrasonico silencioso: pequena amplitud, gran potencia",
            "Control inalambrico de pie (opcional)",
            "Modelo: Actor I Pro",
        ],
        "specs_header": ["Caracteristica", "Detalle"],
        "specs_rows": [
            ["Modelo", "Actor I Pro"],
            ["Bateria", "1600 mAh"],
            ["Modos", "Regular / Alta potencia"],
            ["Tips incluidos", "3 TIPS/E98 o 3 TIPS/EL96"],
        ],
        "precio": "Consultar",
    },

    # EQUIPOS: Motor IRoot Pro
    {
        "title": "Motor Endodontico IRoot Pro",
        "cat_label": "Equipos",
        "ids": [58],
        "img": "images/iroot-pro.jpg",
        "desc": (
            "Motor endodontico con localizador de apice integrado. "
            "Pantalla OLED a color. Contra-angulo de rotacion libre. "
            "Cuatro modos de trabajo. Siete funciones incluyendo "
            "desaceleracion automatica apical y reversa automatica."
        ),
        "features": [
            "Localizador de apice integrado multi-frecuencia",
            "Pantalla OLED a color",
            "Contra-angulo rotacion libre",
            "4 modos de trabajo / 7 funciones",
            "Desaceleracion y reversa automatica en zona apical",
            "Sistemas de limas preconfigurados",
        ],
        "specs_header": ["Caracteristica", "Detalle"],
        "specs_rows": [
            ["Modelo", "SCM-011"],
            ["Dimensiones", "Diametro max 31mm x 148mm"],
            ["Peso", "112g"],
            ["Modos", "4 modos / 7 funciones"],
        ],
        "precio": "Consultar",
    },

    # EQUIPOS: Wispex
    {
        "title": "Wispex — Localizador de Apice",
        "cat_label": "Equipos",
        "ids": [59],
        "img": "images/wispex.jpg",
        "desc": (
            "Localizador de apice de alta precision. Tecnologia multi-frecuencia "
            "avanzada. Alta resolucion. Calibracion automatica. "
            "Funciona en canales humedos y secos. Posicion de referencia ajustable."
        ),
        "features": [
            "Tecnologia multi-frecuencia avanzada",
            "Alta precision en canales humedos y secos",
            "Calibracion automatica",
            "Posicion de referencia ajustable",
            "Compatible con C-Handle para localizacion con limas manuales",
        ],
        "specs_header": ["Caracteristica", "Detalle"],
        "specs_rows": [
            ["Modelo", "Wispex"],
            ["Peso", "85g"],
            ["Dimensiones", "94 x 60 x 13mm"],
            ["Incluye", "Cable, clips, ganchos, adaptador, USB"],
        ],
        "precio": "Consultar",
    },
]


# =============================================================================
# HELPERS
# =============================================================================
def wrap_text(text, max_width, font_size):
    """Divide texto en líneas que caben en max_width (aproximado por chars)."""
    char_w = font_size * 0.52
    max_chars = int(max_width / char_w)
    words = text.split()
    lines, line = [], ""
    for word in words:
        test = line + " " + word if line else word
        if len(test) <= max_chars:
            line = test
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def draw_logo(c, x, y, w, h, logo_path):
    """Dibuja el logo centrado en el área dada."""
    if os.path.exists(logo_path):
        try:
            c.drawImage(
                logo_path, x, y, width=w, height=h,
                preserveAspectRatio=True, mask='auto'
            )
        except Exception:
            pass


# =============================================================================
# PORTADA
# =============================================================================
def draw_cover(c, logo_path, year="2025"):
    w, h = PAGE_W, PAGE_H

    # Mitad izquierda — blanca
    c.setFillColor(C.WHITE)
    c.rect(0, 0, w * 0.52, h, fill=1, stroke=0)

    # Mitad derecha — teal
    c.setFillColor(C.TEAL)
    c.rect(w * 0.52, 0, w * 0.48, h, fill=1, stroke=0)

    # Círculo decorativo teal oscuro en lado derecho
    c.setFillColor(C.TEAL_DARK)
    c.circle(w * 0.76, h * 0.35, 95, fill=1, stroke=0)

    # Pequeño círculo naranja decorativo
    c.setFillColor(C.ORANGE)
    c.circle(w * 0.52, h * 0.72, 18, fill=1, stroke=0)

    # Año grande en blanco
    c.setFillColor(C.WHITE)
    c.setFont("Helvetica-Bold", 58)
    c.drawCentredString(w * 0.76, h * 0.52, year)

    # Subtítulo derecho
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.HexColor("#d4eeea"))
    c.drawCentredString(w * 0.76, h * 0.47, "CATALOGO DE PRODUCTOS ENDODONTICOS")

    # Línea separadora vertical sutil
    c.setStrokeColor(C.TEAL_DARK)
    c.setLineWidth(1.5)
    c.line(w * 0.52, h * 0.1, w * 0.52, h * 0.9)

    # Logo lado izquierdo (centrado verticalmente en zona media-alta)
    logo_w = w * 0.38
    logo_h = logo_w * 0.42
    logo_x = (w * 0.52 - logo_w) / 2
    logo_y = h * 0.50
    draw_logo(c, logo_x, logo_y, logo_w, logo_h, logo_path)

    # Tagline bajo el logo
    c.setFillColor(C.TEAL_DARK)
    c.setFont("Helvetica", 9)
    c.drawCentredString(w * 0.26, h * 0.46, "PRECISION ENDODONTICA")

    # Línea naranja decorativa bajo tagline
    c.setStrokeColor(C.ORANGE)
    c.setLineWidth(2)
    c.line(w * 0.10, h * 0.445, w * 0.42, h * 0.445)

    # Ciudad
    c.setFillColor(C.GRAY_TEXT)
    c.setFont("Helvetica", 8)
    c.drawCentredString(w * 0.26, h * 0.42, "Guadalajara, Jalisco")

    # Barra inferior teal oscuro
    c.setFillColor(C.TEAL_DARK)
    c.rect(0, 0, w, h * 0.07, fill=1, stroke=0)
    c.setFillColor(C.WHITE)
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(w * 0.26, h * 0.028, "PROFESIONAL  |  PRECISO  |  CONFIABLE")

    c.showPage()


# =============================================================================
# ÍNDICE
# =============================================================================
def draw_index(c, families):
    w, h = PAGE_W, PAGE_H

    # Fondo blanco
    c.setFillColor(C.WHITE)
    c.rect(0, 0, w, h, fill=1, stroke=0)

    # Barra superior teal
    c.setFillColor(C.TEAL)
    c.rect(0, h - 60, w, 60, fill=1, stroke=0)

    # Título del índice
    c.setFillColor(C.WHITE)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(MARGIN, h - 38, "INDICE DE PRODUCTOS")

    # Línea naranja bajo barra
    c.setStrokeColor(C.ORANGE)
    c.setLineWidth(3)
    c.line(0, h - 62, w, h - 62)

    # Agrupa por categoría para el índice
    cats = {}
    page_num = 3  # portada=1, índice=2, productos desde 3
    for fam in families:
        cat = fam["cat_label"]
        if cat not in cats:
            cats[cat] = []
        cats[cat].append((fam["title"], page_num))
        page_num += 1

    y = h - 90
    col_w = (w - 2 * MARGIN) / 2

    cat_colors = {
        "Glide Path":     C.TEAL,
        "Limas Manuales": C.TEAL,
        "Conformacion":   C.TEAL,
        "Finisher":       C.ORANGE,
        "Retratamiento":  C.ORANGE,
        "Reciprocantes":  C.TEAL,
        "Especiales":     C.ORANGE,
        "Complementos":   C.TEAL_DARK,
        "Equipos":        C.TEAL_DARK,
    }

    col = 0
    x_positions = [MARGIN, MARGIN + col_w + 10]

    for cat, items in cats.items():
        x = x_positions[col]

        if y < 80:
            col += 1
            if col > 1:
                break
            x = x_positions[col]
            y = h - 90

        # Encabezado de categoría
        badge_color = cat_colors.get(cat, C.TEAL)
        c.setFillColor(badge_color)
        c.roundRect(x, y - 2, col_w - 20, 16, 4, fill=1, stroke=0)
        c.setFillColor(C.WHITE)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(x + 6, y + 2, cat.upper())
        y -= 22

        for title, pg in items:
            # Línea punteada
            c.setStrokeColor(C.GRAY_MID)
            c.setLineWidth(0.5)
            c.setDash(1, 3)
            c.line(x, y + 3, x + col_w - 40, y + 3)
            c.setDash()

            c.setFillColor(C.GRAY_DARK)
            c.setFont("Helvetica", 8)
            c.drawString(x, y, title)

            c.setFillColor(C.TEAL)
            c.setFont("Helvetica-Bold", 8)
            c.drawRightString(x + col_w - 22, y, str(pg))
            y -= 14

        y -= 8

        # Alternar columna si la categoría es muy larga
        if y < h * 0.35 and col == 0:
            col = 1
            x = x_positions[col]
            y = h - 90

    # Footer
    c.setFillColor(C.TEAL_DARK)
    c.rect(0, 0, w, 28, fill=1, stroke=0)
    c.setFillColor(C.WHITE)
    c.setFont("Helvetica", 7)
    c.drawCentredString(w / 2, 10, "EndoShop — Distribucion de instrumental endodontico — Guadalajara, Jalisco")

    c.showPage()


# =============================================================================
# PÁGINA DE FAMILIA DE PRODUCTO
# =============================================================================
def draw_family_page(c, family, page_num, base_dir):
    w, h = PAGE_W, PAGE_H

    # Fondo blanco
    c.setFillColor(C.WHITE)
    c.rect(0, 0, w, h, fill=1, stroke=0)

    # ── COLUMNA IZQUIERDA TEAL
    c.setFillColor(C.TEAL_DARK)
    c.rect(0, 0, COL_L, h, fill=1, stroke=0)

    # Número de página grande semitransparente
    c.saveState()
    c.setFillColor(C.WHITE)
    c.setFillAlpha(0.10)
    c.setFont("Helvetica-Bold", 90)
    c.drawString(3, 55, str(page_num).zfill(2))
    c.restoreState()

    # Etiqueta de categoría vertical
    c.saveState()
    c.translate(COL_L - 12, h / 2)
    c.rotate(90)
    c.setFillColor(C.WHITE)
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(0, 0, family["cat_label"].upper())
    c.restoreState()

    # Número de página legible
    c.setFillColor(C.WHITE)
    c.setFont("Helvetica", 7)
    c.drawString(8, 10, str(page_num))

    # Línea naranja en borde de columna
    c.setStrokeColor(C.ORANGE)
    c.setLineWidth(2)
    c.line(COL_L, 0, COL_L, h)

    # ── COLUMNA DERECHA
    x = COL_R_X
    y = h - MARGIN

    # Badge de subcategoría
    badge_colors = {
        "Glide Path":     C.TEAL,
        "Limas Manuales": colors.HexColor("#2a9d5c"),
        "Conformacion":   C.TEAL,
        "Finisher":       C.ORANGE,
        "Retratamiento":  C.ORANGE,
        "Reciprocantes":  C.TEAL,
        "Especiales":     C.ORANGE,
        "Complementos":   C.TEAL_DARK,
        "Equipos":        C.TEAL_DARK,
    }
    bc = badge_colors.get(family["cat_label"], C.TEAL)
    badge_text = family["cat_label"].upper()
    badge_w = len(badge_text) * 5.5 + 14
    c.setFillColor(bc)
    c.roundRect(x, y - 13, badge_w, 13, 3, fill=1, stroke=0)
    c.setFillColor(C.WHITE)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(x + 7, y - 9, badge_text)
    y -= 20

    # Título del producto
    c.setFillColor(C.GRAY_DARK)
    c.setFont("Helvetica-Bold", 14)
    title_lines = wrap_text(family["title"], COL_R_W, 14)
    for ln in title_lines:
        c.drawString(x, y, ln)
        y -= 17
    y -= 4

    # Línea separadora teal
    c.setStrokeColor(C.TEAL)
    c.setLineWidth(1.2)
    c.line(x, y, x + COL_R_W, y)
    y -= 12

    # Imagen del producto (derecha) + descripción (izquierda)
    img_file = family.get("img", "")
    img_path = os.path.join(base_dir, img_file) if img_file else ""
    img_drawn_h = 0
    img_w_draw = COL_R_W * 0.42
    img_h_max = 105

    if img_file and os.path.exists(img_path):
        try:
            c.drawImage(
                img_path,
                x + COL_R_W - img_w_draw,
                y - img_h_max,
                width=img_w_draw,
                height=img_h_max,
                preserveAspectRatio=True,
                mask='auto'
            )
            img_drawn_h = img_h_max
        except Exception:
            pass

    # Descripción al lado izquierdo de la imagen
    text_w = COL_R_W * 0.55 if img_drawn_h > 0 else COL_R_W
    desc = family.get("desc", "")
    c.setFont("Helvetica", 8)
    c.setFillColor(C.GRAY_TEXT)
    desc_y = y
    for dl in wrap_text(desc, text_w, 8):
        c.drawString(x, desc_y, dl)
        desc_y -= 11

    y = min(desc_y, y - img_drawn_h) - 10

    # Features / características
    features = family.get("features", [])
    if features and y > 120:
        c.setFillColor(C.TEAL_LIGHT)
        feat_h = len(features) * 13 + 12
        if y - feat_h > 80:
            c.roundRect(x, y - feat_h, COL_R_W, feat_h, 5, fill=1, stroke=0)
            fy = y - 10
            for feat in features:
                # Bullet naranja
                c.setFillColor(C.ORANGE)
                c.circle(x + 7, fy + 2, 2.5, fill=1, stroke=0)
                c.setFillColor(C.GRAY_DARK)
                c.setFont("Helvetica", 7.5)
                feat_lines = wrap_text(feat, COL_R_W - 20, 7.5)
                for fl in feat_lines:
                    c.drawString(x + 14, fy, fl)
                    fy -= 11
            y = y - feat_h - 10

    # Tabla de especificaciones
    specs_header = family.get("specs_header", [])
    specs_rows   = family.get("specs_rows", [])

    if specs_header and specs_rows and y > 60:
        table_data = [specs_header] + specs_rows
        n_cols = len(specs_header)
        col_width = COL_R_W / n_cols

        tbl = Table(table_data, colWidths=[col_width] * n_cols)
        tbl.setStyle(TableStyle([
            # Header
            ('BACKGROUND',    (0, 0), (-1, 0), C.TEAL_DARK),
            ('TEXTCOLOR',     (0, 0), (-1, 0), C.WHITE),
            ('FONTNAME',      (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE',      (0, 0), (-1, 0), 7),
            ('ALIGN',         (0, 0), (-1, 0), 'CENTER'),
            ('TOPPADDING',    (0, 0), (-1, 0), 4),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 4),
            # Rows alternadas
            ('BACKGROUND',    (0, 1), (-1, -1), C.WHITE),
            ('ROWBACKGROUNDS',(0, 1), (-1, -1), [C.WHITE, C.TEAL_LIGHT]),
            ('FONTNAME',      (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE',      (0, 1), (-1, -1), 7),
            ('ALIGN',         (0, 1), (-1, -1), 'CENTER'),
            ('TEXTCOLOR',     (0, 1), (-1, -1), C.GRAY_DARK),
            ('TOPPADDING',    (0, 1), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 3),
            # Bordes
            ('GRID',          (0, 0), (-1, -1), 0.4, C.GRAY_MID),
            ('ROUNDEDCORNERS',(0, 0), (-1, -1), 4),
        ]))

        tbl_w, tbl_h = tbl.wrapOn(c, COL_R_W, 200)
        if y - tbl_h > 30:
            tbl.drawOn(c, x, y - tbl_h)
            y = y - tbl_h - 10

    # Precio
    precio = family.get("precio", "")
    if precio and precio != "Consultar" and y > 25:
        precio_label = f"Precio: {precio} MXN"
        pw = len(precio_label) * 5.5 + 16
        c.setFillColor(C.ORANGE)
        c.roundRect(x, y - 18, pw, 18, 4, fill=1, stroke=0)
        c.setFillColor(C.WHITE)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(x + 8, y - 13, precio_label)

    # Footer
    c.setFillColor(C.TEAL_DARK)
    c.rect(0, 0, w, 20, fill=1, stroke=0)
    c.setFillColor(C.WHITE)
    c.setFont("Helvetica", 6.5)
    c.drawCentredString(w / 2, 7, "EndoShop — Distribucion de instrumental endodontico — Guadalajara, Jalisco")

    c.showPage()


# =============================================================================
# CONTRAPORTADA
# =============================================================================
def draw_backcover(c, logo_path):
    w, h = PAGE_W, PAGE_H

    # Fondo teal oscuro
    c.setFillColor(C.TEAL_DARK)
    c.rect(0, 0, w, h, fill=1, stroke=0)

    # Círculo decorativo teal
    c.setFillColor(C.TEAL)
    c.circle(w * 0.8, h * 0.2, 110, fill=1, stroke=0)

    # Círculo naranja pequeño
    c.setFillColor(C.ORANGE)
    c.circle(w * 0.15, h * 0.75, 40, fill=1, stroke=0)

    # Logo centrado
    logo_w = w * 0.45
    logo_h = logo_w * 0.42
    draw_logo(c, (w - logo_w) / 2, h / 2 + 10, logo_w, logo_h, logo_path)

    # Tagline
    c.setFillColor(C.WHITE)
    c.setFont("Helvetica", 11)
    c.drawCentredString(w / 2, h / 2 - 10, "PRECISION ENDODONTICA")

    # Línea naranja decorativa
    c.setStrokeColor(C.ORANGE)
    c.setLineWidth(2)
    c.line(w * 0.25, h / 2 - 22, w * 0.75, h / 2 - 22)

    # Ciudad
    c.setFillColor(colors.HexColor("#a8d8d3"))
    c.setFont("Helvetica", 9)
    c.drawCentredString(w / 2, h / 2 - 38, "Guadalajara, Jalisco")

    # Barra inferior
    c.setFillColor(C.TEAL)
    c.rect(0, 0, w, 30, fill=1, stroke=0)
    c.setFillColor(C.WHITE)
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(w / 2, 11, "PROFESIONAL  |  PRECISO  |  CONFIABLE")

    c.showPage()


# =============================================================================
# GENERADOR PRINCIPAL
# =============================================================================
def generate_pdf(base_dir, output_path, year="2025"):
    logo_path = os.path.join(base_dir, "images", "logo.png")

    buf = io.BytesIO()
    cv = rl_canvas.Canvas(buf, pagesize=A4)

    # 1. Portada
    draw_cover(cv, logo_path, year)

    # 2. Índice
    draw_index(cv, FAMILIES)

    # 3. Páginas de producto
    for i, family in enumerate(FAMILIES, start=3):
        draw_family_page(cv, family, i, base_dir)

    # 4. Contraportada
    draw_backcover(cv, logo_path)

    cv.save()

    with open(output_path, "wb") as f:
        f.write(buf.getvalue())

    print(f"PDF generado: {output_path}  ({len(FAMILIES)} familias + portada + indice + contraportada)")
    return output_path


# =============================================================================
# HANDLER VERCEL
# =============================================================================
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            output_path = "/tmp/catalogo-endoshop.pdf"
            generate_pdf(base_dir, output_path)

            with open(output_path, "rb") as f:
                pdf_bytes = f.read()

            self.send_response(200)
            self.send_header("Content-Type", "application/pdf")
            self.send_header("Content-Disposition", "attachment; filename=catalogo-endoshop.pdf")
            self.send_header("Content-Length", str(len(pdf_bytes)))
            self.end_headers()
            self.wfile.write(pdf_bytes)

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(f"Error: {str(e)}".encode())


# =============================================================================
# EJECUCIÓN LOCAL
# =============================================================================
if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output = os.path.join(base_dir, "catalogo-endoshop.pdf")
    generate_pdf(base_dir, output)
