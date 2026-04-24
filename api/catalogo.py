"""
api/catalogo.py
---------------
Función serverless de Vercel que genera el catálogo PDF de EndoShop.
Lee productos desde productos.json e imágenes desde la carpeta images/.

Dependencias (agregar en requirements.txt):
    reportlab
"""

import json
import os
import io
from http.server import BaseHTTPRequestHandler
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle


# =============================================================================
# COLORES
# =============================================================================
class C:
    TEAL_DARK   = colors.HexColor("#137a8a")
    TEAL_MID    = colors.HexColor("#1A9BAF")
    TEAL_LIGHT  = colors.HexColor("#e6f7fa")
    ORANGE      = colors.HexColor("#E8962A")
    BLUE_HEADER = colors.HexColor("#1E3A5F")
    BLUE_ALT    = colors.HexColor("#D6E8F5")
    WHITE       = colors.white
    GRAY_LIGHT  = colors.HexColor("#f8fafb")
    GRAY_MID    = colors.HexColor("#dde6e8")
    GRAY_TEXT   = colors.HexColor("#4a6670")
    GRAY_DARK   = colors.HexColor("#1e3035")


# =============================================================================
# DIMENSIONES
# =============================================================================
PAGE_W, PAGE_H = A4          # 595 x 842 pts
COL_L   = 160                # ancho columna izquierda (teal)
MARGIN  = 16 * mm
COL_R_X = COL_L + 16        # inicio columna derecha
COL_R_W = PAGE_W - COL_L - 32  # ancho útil columna derecha


# =============================================================================
# HELPERS DE DIBUJO
# =============================================================================
def draw_cover(c, brand_name, tagline, year):
    w, h = PAGE_W, PAGE_H

    # Fondo blanco
    c.setFillColor(C.WHITE)
    c.rect(0, 0, w, h, fill=1, stroke=0)

    # Bloque teal derecho
    c.setFillColor(C.TEAL_MID)
    c.rect(w * 0.5, 0, w * 0.5, h, fill=1, stroke=0)

    # Elipse decorativa
    c.setFillColor(C.TEAL_DARK)
    c.ellipse(w * 0.58, h * 0.42, w * 1.0, h * 0.88, fill=1, stroke=0)

    # Año
    c.setFillColor(C.WHITE)
    c.setFont("Helvetica-Bold", 42)
    c.drawString(w * 0.57, h * 0.52, year)

    # Subtítulo
    c.setFont("Helvetica", 9)
    c.drawString(w * 0.57, h * 0.47, "CATÁLOGO DE PRODUCTOS ENDODÓNTICOS")

    # Tagline izquierda
    c.setFillColor(C.TEAL_MID)
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(w * 0.26, h * 0.42, tagline)
    c.setFont("Helvetica", 10)
    c.drawCentredString(w * 0.26, h * 0.38, "SOLUCIONES ENDODÓNTICAS")

    # Nombre de marca
    c.setFillColor(C.TEAL_DARK)
    c.setFont("Helvetica-Bold", 34)
    parts = brand_name.split()
    c.drawString(w * 0.05, h * 0.18, parts[0])
    if len(parts) > 1:
        c.drawString(w * 0.05, h * 0.11, " ".join(parts[1:]))

    # Línea separadora
    c.setStrokeColor(C.TEAL_MID)
    c.setLineWidth(2)
    c.line(w * 0.05, h * 0.09, w * 0.44, h * 0.09)

    c.showPage()


def draw_backcover(c, brand_name, contact):
    c.setFillColor(C.TEAL_DARK)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    # Círculo decorativo
    c.setFillColor(C.TEAL_MID)
    c.circle(PAGE_W * 0.8, PAGE_H * 0.2, 120, fill=1, stroke=0)

    c.setFillColor(C.WHITE)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 + 30, brand_name)

    c.setFont("Helvetica", 11)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2, contact)

    c.setFont("Helvetica", 9)
    c.setFillColor(C.TEAL_LIGHT)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 20, "Instrumental Endodóntico de Alta Calidad")

    c.showPage()


def draw_section_col(c, cat_label, page_num):
    """Dibuja la columna izquierda teal con categoría y número de página."""
    c.setFillColor(C.TEAL_DARK)
    c.rect(0, 0, COL_L, PAGE_H, fill=1, stroke=0)

    # Número de página decorativo (semitransparente)
    c.saveState()
    c.setFillColor(C.WHITE)
    c.setFillAlpha(0.10)
    c.setFont("Helvetica-Bold", 110)
    c.drawString(4, 60, str(page_num).zfill(2))
    c.restoreState()

    # Etiqueta de categoría vertical
    c.saveState()
    c.translate(COL_L - 14, PAGE_H / 2)
    c.rotate(90)
    c.setFillColor(C.WHITE)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(0, 0, cat_label.upper())
    c.restoreState()

    # Línea separadora
    c.setStrokeColor(C.TEAL_MID)
    c.setLineWidth(1)
    c.line(COL_L, 0, COL_L, PAGE_H)

    # Número de página
    c.setFillColor(C.WHITE)
    c.setFont("Helvetica", 7)
    c.drawString(8, 10, str(page_num))


def draw_product_page(c, product, page_num, images_path):
    """Dibuja una página completa de producto."""

    cat_labels = {
        "limas":        "Limas Endodónticas",
        "complementos": "Complementos",
        "equipos":      "Equipos",
    }
    cat_label = cat_labels.get(product.get("cat", ""), "Producto")

    # Fondo blanco
    c.setFillColor(C.WHITE)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    # Columna izquierda
    draw_section_col(c, cat_label, page_num)

    # --- COLUMNA DERECHA ---
    x = COL_R_X
    y = PAGE_H - MARGIN

    # TAG badge
    tag = product.get("tag", "")
    tag_colors = {
        "Glide Path":    C.TEAL_MID,
        "Manual":        colors.HexColor("#2a9d5c"),
        "Rotatoria":     C.TEAL_MID,
        "Reciprocante":  C.TEAL_MID,
        "Retratamiento": C.ORANGE,
        "Finisher":      C.ORANGE,
        "Especial":      C.ORANGE,
        "Pediátrico":    C.ORANGE,
        "Complemento":   C.TEAL_MID,
        "Equipo":        C.ORANGE,
    }
    badge_color = tag_colors.get(tag, C.TEAL_MID)
    if tag:
        c.setFillColor(badge_color)
        c.roundRect(x, y - 14, len(tag) * 5.5 + 12, 14, 4, fill=1, stroke=0)
        c.setFillColor(C.WHITE)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(x + 6, y - 10, tag.upper())
        y -= 22

    # Nombre del producto
    name = product.get("name", "")
    c.setFillColor(C.GRAY_DARK)
    c.setFont("Helvetica-Bold", 13)
    # Wrap nombre si es largo
    words = name.split()
    line = ""
    lines = []
    for w in words:
        test = line + " " + w if line else w
        if len(test) * 7 < COL_R_W:
            line = test
        else:
            lines.append(line)
            line = w
    if line:
        lines.append(line)
    for ln in lines:
        c.drawString(x, y, ln)
        y -= 16
    y -= 4

    # Línea separadora bajo el nombre
    c.setStrokeColor(C.TEAL_MID)
    c.setLineWidth(1.2)
    c.line(x, y, x + COL_R_W, y)
    y -= 12

    # Imagen del producto
    img_file = product.get("img", "")
    img_path = os.path.join(images_path, os.path.basename(img_file))
    img_h = 0
    if img_file and os.path.exists(img_path):
        img_w_draw = COL_R_W * 0.45
        img_h = 110
        try:
            c.drawImage(img_path, x + COL_R_W - img_w_draw - 4,
                        y - img_h, width=img_w_draw, height=img_h,
                        preserveAspectRatio=True, mask='auto')
        except Exception:
            pass  # Si la imagen falla, continúa sin ella

    # Descripción — al lado izquierdo de la imagen
    desc = product.get("desc", "")
    text_w = COL_R_W * 0.52
    c.setFont("Helvetica", 8)
    c.setFillColor(C.GRAY_TEXT)
    desc_y = y
    desc_lines = _wrap_text(desc, text_w, 8)
    for dl in desc_lines:
        c.drawString(x, desc_y, dl)
        desc_y -= 11

    y = min(desc_y, y - img_h) - 10

    # Bloques IDEAL y DIFERENCIADOR
    for label, key in [("Indicado para:", "ideal"), ("Diferenciador:", "dif")]:
        val = product.get(key, "")
        if not val:
            continue
        if y < 80:
            break
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(C.TEAL_MID)
        c.drawString(x, y, label)
        c.setFont("Helvetica", 8)
        c.setFillColor(C.GRAY_TEXT)
        wrapped = _wrap_text(val, COL_R_W, 8)
        for wl in wrapped:
            y -= 11
            if y < 80:
                break
            c.drawString(x + 8, y, wl)
        y -= 8

    # Variantes (campos)
    campos = product.get("campos", [])
    if campos and y > 80:
        y -= 4
        c.setFillColor(C.TEAL_LIGHT)
        box_h = len(campos) * 28 + 12
        if y - box_h > 40:
            c.roundRect(x, y - box_h, COL_R_W, box_h, 5, fill=1, stroke=0)
            c.setStrokeColor(C.TEAL_MID)
            c.setLineWidth(0.5)
            c.roundRect(x, y - box_h, COL_R_W, box_h, 5, fill=0, stroke=1)
            cy = y - 12
            for campo in campos:
                c.setFont("Helvetica-Bold", 7)
                c.setFillColor(C.TEAL_DARK)
                c.drawString(x + 8, cy, campo["label"].upper() + ":")
                cy -= 11
                c.setFont("Helvetica", 7)
                c.setFillColor(C.GRAY_TEXT)
                opts = "  •  ".join(campo["opciones"])
                opt_lines = _wrap_text(opts, COL_R_W - 16, 7)
                for ol in opt_lines:
                    c.drawString(x + 8, cy, ol)
                    cy -= 9
                cy -= 4
            y = y - box_h - 8

    # Precio
    precio = product.get("precio", "")
    if precio and y > 40:
        c.setFillColor(C.ORANGE)
        precio_label = f"Precio: {precio} MXN"
        pw = len(precio_label) * 5.5 + 16
        c.roundRect(x, y - 18, pw, 18, 5, fill=1, stroke=0)
        c.setFillColor(C.WHITE)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(x + 8, y - 13, precio_label)

    c.showPage()


def _wrap_text(text, max_width, font_size):
    """Divide texto en líneas que caben en max_width (aproximado)."""
    char_w = font_size * 0.52
    max_chars = int(max_width / char_w)
    words = text.split()
    lines = []
    line = ""
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


# =============================================================================
# GENERADOR PRINCIPAL
# =============================================================================
def generate_pdf(products, images_path,
                 brand_name="EndoShop",
                 tagline="PROFESIONAL · PRECISO · CONFIABLE",
                 year="2025",
                 contact="www.endoshop.com.mx"):

    buf = io.BytesIO()
    cv = canvas.Canvas(buf, pagesize=A4)

    # Portada
    draw_cover(cv, brand_name, tagline, year)

    # Una página por producto
    for i, product in enumerate(products, start=1):
        draw_product_page(cv, product, i, images_path)

    # Contraportada
    draw_backcover(cv, brand_name, contact)

    cv.save()
    buf.seek(0)
    return buf.read()


# =============================================================================
# HANDLER DE VERCEL
# =============================================================================
class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            # Rutas base del proyecto
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            json_path = os.path.join(base_dir, "productos.json")
            images_path = os.path.join(base_dir, "images")

            # Leer productos
            with open(json_path, "r", encoding="utf-8") as f:
                products = json.load(f)

            # Generar PDF
            pdf_bytes = generate_pdf(products, images_path)

            # Respuesta HTTP
            self.send_response(200)
            self.send_header("Content-Type", "application/pdf")
            self.send_header("Content-Disposition",
                             "attachment; filename=catalogo-endoshop.pdf")
            self.send_header("Content-Length", str(len(pdf_bytes)))
            self.end_headers()
            self.wfile.write(pdf_bytes)

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(f"Error generando catálogo: {str(e)}".encode())
