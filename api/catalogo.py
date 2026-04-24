"""
catalogo.py
-----------
Generador de catalogo PDF estilo Fanta Dental para EndoShop.
Lee datos desde productos.json y agrupa por campo "sistema".

Uso local:
    cd endoshop-main && python api/catalogo.py

Dependencias:
    pip install reportlab
"""

import json
import os
import io
from collections import OrderedDict
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.platypus import Table, TableStyle


# =============================================================================
# COLORES
# =============================================================================
class C:
    TEAL        = colors.HexColor("#1A9BAF")
    TEAL_DARK   = colors.HexColor("#137a8a")
    TEAL_LIGHT  = colors.HexColor("#e6f7fa")
    ORANGE      = colors.HexColor("#E8962A")
    WHITE       = colors.white
    GRAY_100    = colors.HexColor("#f0f4f5")
    GRAY_200    = colors.HexColor("#dde6e8")
    GRAY_400    = colors.HexColor("#8fa8ad")
    GRAY_600    = colors.HexColor("#4a6670")
    GRAY_800    = colors.HexColor("#1e3035")


# =============================================================================
# DIMENSIONES
# =============================================================================
PAGE_W, PAGE_H = A4
SIDEBAR_W  = 20 * mm
CONTENT_X  = SIDEBAR_W + 14 * mm
CONTENT_W  = PAGE_W - CONTENT_X - 14 * mm
HEADER_H   = 52
FOOTER_H   = 20


# =============================================================================
# ETIQUETAS
# =============================================================================
CAT_LABELS = {
    "limas":        "LIMAS",
    "complementos": "COMPLEMENTOS",
    "equipos":      "EQUIPOS",
}

SUB_LABELS = {
    "glide":         "GLIDE PATH",
    "conformacion":  "CONFORMACION",
    "reciprocante":  "RECIPROCANTE",
    "retratamiento": "RETRATAMIENTO",
    "finisher":      "FINISHER",
    "especiales":    "ESPECIALES",
    "manual":        "MANUAL",
    "gutapercha":    "GUTAPERCHA",
    "puntas-papel":  "PUNTAS DE PAPEL",
    "gp-plugger":    "GP PLUGGER",
    "irrigacion":    "IRRIGACION",
    "accesorio":     "ACCESORIO",
}


# =============================================================================
# UTILIDADES
# =============================================================================
def wrap_text(text, max_width, font_size):
    chars_per_line = max(1, int(max_width / (font_size * 0.52)))
    words = text.split()
    lines, current = [], ""
    for word in words:
        test = (current + " " + word).strip()
        if len(test) <= chars_per_line:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def load_json(base_dir):
    json_path = os.path.join(base_dir, "productos.json")
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def group_by_sistema(products):
    grupos = OrderedDict()
    for p in products:
        sis = p.get("sistema", "Otros")
        if sis not in grupos:
            grupos[sis] = []
        grupos[sis].append(p)
    return grupos


# =============================================================================
# FOOTER COMUN
# =============================================================================
def draw_footer(c):
    c.setFillColor(C.TEAL_DARK)
    c.rect(0, 0, PAGE_W, FOOTER_H, fill=1, stroke=0)
    c.setFillColor(C.WHITE)
    c.setFont("Helvetica", 6.5)
    c.drawCentredString(
        PAGE_W / 2, 7,
        "EndoShop — Distribucion de instrumental endodontico — Guadalajara, Jalisco — ventasfantagdl@gmail.com"
    )


# =============================================================================
# PORTADA
# =============================================================================
def draw_cover(c, logo_path, year="2025"):
    w, h = PAGE_W, PAGE_H

    c.setFillColor(C.TEAL)
    c.rect(0, h / 2, w, h / 2, fill=1, stroke=0)

    c.setFillColor(C.WHITE)
    c.rect(0, 0, w, h / 2, fill=1, stroke=0)

    c.saveState()
    c.setFillColor(C.ORANGE)
    c.setFillAlpha(0.18)
    c.circle(w * 0.88, h * 0.82, 90, fill=1, stroke=0)
    c.restoreState()

    c.saveState()
    c.setFillColor(C.TEAL_LIGHT)
    c.setFillAlpha(0.7)
    c.circle(w * 0.1, h * 0.18, 60, fill=1, stroke=0)
    c.restoreState()

    logo_w, logo_h = 200, 84
    logo_x = (w - logo_w) / 2
    logo_y = h / 2 - logo_h - 20
    if logo_path and os.path.exists(logo_path):
        c.drawImage(logo_path, logo_x, logo_y,
                    width=logo_w, height=logo_h,
                    preserveAspectRatio=True, mask="auto")

    c.setFillColor(C.WHITE)
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(w / 2, h * 0.72, "CATALOGO DE PRODUCTOS")
    c.setFillColor(colors.HexColor("#cceef4"))
    c.setFont("Helvetica", 12)
    c.drawCentredString(w / 2, h * 0.72 - 22, "Instrumental Endodontico de Precision")

    c.setStrokeColor(C.ORANGE)
    c.setLineWidth(2.5)
    c.line(w * 0.28, h * 0.72 - 34, w * 0.72, h * 0.72 - 34)

    c.setFillColor(C.GRAY_600)
    c.setFont("Helvetica", 9.5)
    c.drawCentredString(w / 2, logo_y - 28, f"Edicion {2026}  |  Guadalajara, Jalisco")

    badge_w, badge_h = 196, 22
    badge_x = (w - badge_w) / 2
    badge_y = logo_y - 62
    c.setFillColor(colors.HexColor("#fef3e2"))
    c.roundRect(badge_x, badge_y, badge_w, badge_h, 11, fill=1, stroke=0)
    c.setFillColor(C.ORANGE)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawCentredString(w / 2, badge_y + 7, "DISTRIBUCION ESPECIALIZADA — ENDODONCIA")

    draw_footer(c)
    c.showPage()


# =============================================================================
# INDICE
# =============================================================================
def draw_index(c, grupos, logo_path):
    w, h = PAGE_W, PAGE_H

    c.setFillColor(C.WHITE)
    c.rect(0, 0, w, h, fill=1, stroke=0)

    c.setFillColor(C.TEAL)
    c.rect(0, 0, SIDEBAR_W, h, fill=1, stroke=0)

    c.saveState()
    c.setFillColor(C.WHITE)
    c.setFont("Helvetica-Bold", 8)
    c.translate(SIDEBAR_W / 2, h / 2)
    c.rotate(90)
    c.drawCentredString(0, 0, "CONTENIDO")
    c.restoreState()

    if logo_path and os.path.exists(logo_path):
        c.drawImage(logo_path, w - 112, h - 50,
                    width=102, height=38,
                    preserveAspectRatio=True, mask="auto")

    c.setFillColor(C.GRAY_800)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(CONTENT_X, h - 50, "Indice de Productos")
    c.setStrokeColor(C.TEAL)
    c.setLineWidth(2)
    c.line(CONTENT_X, h - 57, CONTENT_X + CONTENT_W, h - 57)

    cat_order = ["limas", "complementos", "equipos"]
    cat_sistemas = OrderedDict((cat, []) for cat in cat_order)
    for sistema, prods in grupos.items():
        cat = prods[0].get("cat", "otros")
        if cat in cat_sistemas:
            cat_sistemas[cat].append(sistema)
        else:
            cat_sistemas.setdefault(cat, []).append(sistema)

    y = h - 72
    page_num = 3

    for cat, sistemas in cat_sistemas.items():
        if not sistemas:
            continue

        c.setFillColor(C.TEAL_LIGHT)
        c.roundRect(CONTENT_X, y - 14, CONTENT_W, 20, 4, fill=1, stroke=0)
        c.setFillColor(C.TEAL_DARK)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(CONTENT_X + 8, y - 8, CAT_LABELS.get(cat, cat.upper()))
        y -= 26

        for sistema in sistemas:
            if y < FOOTER_H + 16:
                break

            c.setFillColor(C.GRAY_800)
            c.setFont("Helvetica", 8.5)
            c.drawString(CONTENT_X + 8, y, sistema)

            c.setFont("Helvetica-Bold", 8.5)
            c.setFillColor(C.TEAL)
            c.drawRightString(CONTENT_X + CONTENT_W, y, str(page_num))

            name_end = CONTENT_X + 8 + len(sistema) * 4.8
            page_start = CONTENT_X + CONTENT_W - 14
            if page_start > name_end + 8:
                c.setStrokeColor(C.GRAY_200)
                c.setLineWidth(0.5)
                c.setDash(1, 3)
                c.line(name_end + 4, y + 2, page_start - 4, y + 2)
                c.setDash()

            y -= 16
            page_num += 1

        y -= 8

    draw_footer(c)
    c.showPage()


# =============================================================================
# PAGINA POR SISTEMA — imagen centrada grande, todo centrado
# =============================================================================
def draw_system_page(c, sistema, productos, page_num, base_dir, logo_path):
    w, h = PAGE_W, PAGE_H

    # Fondo blanco
    c.setFillColor(C.WHITE)
    c.rect(0, 0, w, h, fill=1, stroke=0)

    # Banda lateral teal
    c.setFillColor(C.TEAL)
    c.rect(0, 0, SIDEBAR_W, h, fill=1, stroke=0)

    # Texto vertical en banda
    cat = productos[0].get("cat", "")
    sub = productos[0].get("sub", "")
    cat_label = CAT_LABELS.get(cat, cat.upper())
    sub_label = SUB_LABELS.get(sub, sub.upper()) if sub else ""
    sidebar_text = f"{cat_label}  |  {sub_label}" if sub_label else cat_label

    c.saveState()
    c.setFillColor(C.WHITE)
    c.setFont("Helvetica-Bold", 7)
    c.translate(SIDEBAR_W / 2, h / 2)
    c.rotate(90)
    c.drawCentredString(0, 0, sidebar_text)
    c.restoreState()

    # Numero de pagina en banda lateral
    c.setFillColor(C.ORANGE)
    c.roundRect(4, 28, SIDEBAR_W - 8, 18, 4, fill=1, stroke=0)
    c.setFillColor(C.WHITE)
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(SIDEBAR_W / 2, 33, str(page_num))

    # Encabezado fondo teal claro
    header_y = h - HEADER_H
    c.setFillColor(C.TEAL_LIGHT)
    c.rect(SIDEBAR_W, header_y, w - SIDEBAR_W, HEADER_H, fill=1, stroke=0)

    # Linea teal bajo encabezado
    c.setStrokeColor(C.TEAL)
    c.setLineWidth(1.5)
    c.line(SIDEBAR_W, header_y, w, header_y)

    # Logo en encabezado
    if logo_path and os.path.exists(logo_path):
        c.drawImage(logo_path, w - 112, header_y + 7,
                    width=100, height=36,
                    preserveAspectRatio=True, mask="auto")

    # Nombre del sistema
    c.setFillColor(C.TEAL_DARK)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(CONTENT_X, h - 22, sistema)

    # Tag
    tag = productos[0].get("tag", "")
    if tag:
        tag_w = len(tag) * 5.2 + 16
        c.setFillColor(C.TEAL)
        c.roundRect(CONTENT_X, header_y + 8, tag_w, 14, 4, fill=1, stroke=0)
        c.setFillColor(C.WHITE)
        c.setFont("Helvetica-Bold", 6.5)
        c.drawString(CONTENT_X + 6, header_y + 13, tag.upper())

    # --- Contenido centrado ---
    x  = CONTENT_X
    cx = CONTENT_X + CONTENT_W / 2   # centro horizontal del area de contenido
    y  = header_y - 12

    # Imagen centrada, 2/5 de la altura util
    area_util_h = header_y - FOOTER_H
    IMG_H = int(area_util_h * 0.40)
    IMG_W = CONTENT_W

    img_file = productos[0].get("img", "")
    img_path = os.path.join(base_dir, img_file) if img_file else ""
    img_drawn = False

    if img_path and os.path.exists(img_path):
        try:
            c.drawImage(img_path,
                        x, y - IMG_H,
                        width=IMG_W, height=IMG_H,
                        preserveAspectRatio=True, mask="auto")
            img_drawn = True
        except Exception:
            pass

    if img_drawn:
        y = y - IMG_H - 10

    # Descripcion centrada
    desc = productos[0].get("desc", "")
    if desc:
        c.setFillColor(C.GRAY_600)
        c.setFont("Helvetica", 8)
        desc_lines = wrap_text(desc, CONTENT_W, 8)
        for line in desc_lines:
            if y < FOOTER_H + 10:
                break
            c.drawCentredString(cx, y, line)
            y -= 11
        y -= 4

    # Bloque ideal / ventaja centrado
    ideal = productos[0].get("ideal", "")
    dif   = productos[0].get("dif", "")

    if (ideal or dif) and y > FOOTER_H + 50:
        ideal_lines = wrap_text(ideal, CONTENT_W - 18, 7.5) if ideal else []
        dif_lines   = wrap_text(dif,   CONTENT_W - 18, 7.5) if dif   else []

        block_h = 10
        if ideal_lines:
            block_h += 12 + len(ideal_lines) * 11
        if dif_lines:
            block_h += 12 + len(dif_lines) * 11

        if y - block_h > FOOTER_H + 10:
            c.setFillColor(C.TEAL_LIGHT)
            c.roundRect(x, y - block_h, CONTENT_W, block_h, 5, fill=1, stroke=0)
            by = y - 9

            if ideal_lines:
                c.setFillColor(C.TEAL_DARK)
                c.setFont("Helvetica-Bold", 7)
                c.drawCentredString(cx, by, "Ideal para:")
                by -= 11
                c.setFillColor(C.GRAY_600)
                c.setFont("Helvetica", 7.5)
                for line in ideal_lines:
                    c.drawCentredString(cx, by, line)
                    by -= 11

            if dif_lines:
                c.setFillColor(C.TEAL_DARK)
                c.setFont("Helvetica-Bold", 7)
                c.drawCentredString(cx, by, "Ventaja:")
                by -= 11
                c.setFillColor(C.GRAY_600)
                c.setFont("Helvetica", 7.5)
                for line in dif_lines:
                    c.drawCentredString(cx, by, line)
                    by -= 11

            y = y - block_h - 12

    # --- Tabla de especificaciones centrada ---
    if y > FOOTER_H + 50:
        c.setFillColor(C.GRAY_800)
        c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(cx, y, "Especificaciones y variantes disponibles")
        y -= 6
        c.setStrokeColor(C.GRAY_200)
        c.setLineWidth(0.5)
        c.line(x, y, x + CONTENT_W, y)
        y -= 10

        table_data = [["Producto", "Campo", "Opciones"]]
        for p in productos:
            nombre = p.get("name", "")
            campos = p.get("campos", [])
            if campos:
                first = True
                for campo in campos:
                    label    = campo.get("label", "")
                    opciones = campo.get("opciones", [])
                    ops_str  = "  /  ".join(str(o) for o in opciones)
                    row_name = nombre if first else ""
                    table_data.append([row_name, label, ops_str])
                    first = False
            else:
                table_data.append([nombre, "—", "Unica presentacion"])

        if len(table_data) > 1:
            col_w = [CONTENT_W * 0.36, CONTENT_W * 0.18, CONTENT_W * 0.46]
            tbl = Table(table_data, colWidths=col_w, repeatRows=1)
            tbl.setStyle(TableStyle([
                ("BACKGROUND",     (0, 0), (-1, 0), C.TEAL_DARK),
                ("TEXTCOLOR",      (0, 0), (-1, 0), C.WHITE),
                ("FONTNAME",       (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE",       (0, 0), (-1, 0), 7),
                ("ALIGN",          (0, 0), (-1, 0), "CENTER"),
                ("TOPPADDING",     (0, 0), (-1, 0), 4),
                ("BOTTOMPADDING",  (0, 0), (-1, 0), 4),
                ("LINEBELOW",      (0, 0), (-1, 0), 1.2, C.TEAL),
                ("FONTNAME",       (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE",       (0, 1), (-1, -1), 7),
                ("TEXTCOLOR",      (0, 1), (-1, -1), C.GRAY_800),
                ("ALIGN",          (0, 1), (0, -1),  "LEFT"),
                ("ALIGN",          (1, 1), (1, -1),  "CENTER"),
                ("ALIGN",          (2, 1), (2, -1),  "LEFT"),
                ("TOPPADDING",     (0, 1), (-1, -1), 3),
                ("BOTTOMPADDING",  (0, 1), (-1, -1), 3),
                ("LEFTPADDING",    (0, 0), (-1, -1), 6),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [C.WHITE, C.TEAL_LIGHT]),
                ("GRID",           (0, 0), (-1, -1), 0.4, C.GRAY_200),
            ]))

            tbl_w, tbl_h = tbl.wrapOn(c, CONTENT_W, y - FOOTER_H - 10)
            if y - tbl_h > FOOTER_H + 4:
                tbl.drawOn(c, x, y - tbl_h)

    draw_footer(c)
    c.showPage()


# =============================================================================
# CONTRAPORTADA
# =============================================================================
def draw_backcover(c, logo_path):
    w, h = PAGE_W, PAGE_H

    c.setFillColor(C.TEAL_DARK)
    c.rect(0, 0, w, h, fill=1, stroke=0)

    c.saveState()
    c.setFillColor(C.ORANGE)
    c.setFillAlpha(0.20)
    c.circle(w * 0.82, h * 0.22, 110, fill=1, stroke=0)
    c.restoreState()

    c.saveState()
    c.setFillColor(C.TEAL)
    c.setFillAlpha(0.35)
    c.circle(w * 0.12, h * 0.76, 70, fill=1, stroke=0)
    c.restoreState()

    logo_w, logo_h = 220, 88
    if logo_path and os.path.exists(logo_path):
        c.drawImage(logo_path,
                    (w - logo_w) / 2, h / 2 - 10,
                    width=logo_w, height=logo_h,
                    preserveAspectRatio=True, mask="auto")

    c.setStrokeColor(C.ORANGE)
    c.setLineWidth(2.5)
    c.line(w * 0.25, h / 2 - 22, w * 0.75, h / 2 - 22)

    c.setFillColor(C.WHITE)
    c.setFont("Helvetica", 11)
    c.drawCentredString(w / 2, h / 2 - 40, "PRECISION ENDODONTICA")

    c.setFillColor(colors.HexColor("#a8d8d3"))
    c.setFont("Helvetica", 9)
    c.drawCentredString(w / 2, h / 2 - 56, "Guadalajara, Jalisco")

    c.setFillColor(C.WHITE)
    c.setFont("Helvetica", 9)
    c.drawCentredString(w / 2, h * 0.32, "ventasfantagdl@gmail.com")

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
    products  = load_json(base_dir)
    grupos    = group_by_sistema(products)

    buf = io.BytesIO()
    cv  = rl_canvas.Canvas(buf, pagesize=A4)

    draw_cover(cv, logo_path, year)
    draw_index(cv, grupos, logo_path)

    for page_num, (sistema, prods) in enumerate(grupos.items(), start=3):
        draw_system_page(cv, sistema, prods, page_num, base_dir, logo_path)

    draw_backcover(cv, logo_path)

    cv.save()
    with open(output_path, "wb") as f:
        f.write(buf.getvalue())

    print(f"PDF generado: {output_path}  ({len(grupos)} sistemas, {len(products)} productos)")
    return output_path


# =============================================================================
# HANDLER VERCEL
# =============================================================================
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            base_dir    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
# EJECUCION LOCAL
# =============================================================================
if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output   = os.path.join(base_dir, "catalogo-endoshop.pdf")
    generate_pdf(base_dir, output)