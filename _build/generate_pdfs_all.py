"""Generate basic PDFs from all the translated markdown files.

For each locale that has its own quick-reference.md (or user-guide.md),
generate a basic text-only PDF. SVG/PNG screenshots aren't embedded —
those are placeholder references.
"""

import os
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

DOCS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAVY = colors.HexColor("#0F3460")
ACCENT = colors.HexColor("#00B4D8")
TEXT_MUTED = colors.HexColor("#556")
SURF = colors.HexColor("#F8FAFC")
BORDER = colors.HexColor("#E5E7EB")

# Try to register a Unicode font that supports many scripts.
# Falls back to Helvetica if not available.
FONT_NAME = 'Helvetica'
FONT_NAME_BOLD = 'Helvetica-Bold'
try:
    # DejaVu Sans is commonly available on Linux and supports Cyrillic, Greek,
    # extended Latin. For CJK/Arabic/Thai/Hindi, it lacks coverage but PDFs
    # for those locales will need a more specific font setup.
    pdfmetrics.registerFont(TTFont('DejaVu', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVu-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
    FONT_NAME = 'DejaVu'
    FONT_NAME_BOLD = 'DejaVu-Bold'
    print(f"Using DejaVu fonts")
except Exception as e:
    print(f"DejaVu not available, using Helvetica: {e}")


def make_styles():
    return {
        'title': ParagraphStyle('title', fontName=FONT_NAME_BOLD,
                                fontSize=24, textColor=NAVY,
                                spaceAfter=18, alignment=TA_LEFT,
                                leading=28),
        'h1': ParagraphStyle('h1', fontName=FONT_NAME_BOLD,
                             fontSize=18, textColor=NAVY,
                             spaceBefore=20, spaceAfter=10,
                             leading=22),
        'h2': ParagraphStyle('h2', fontName=FONT_NAME_BOLD,
                             fontSize=14, textColor=NAVY,
                             spaceBefore=16, spaceAfter=8,
                             leading=18),
        'h3': ParagraphStyle('h3', fontName=FONT_NAME_BOLD,
                             fontSize=12, textColor=NAVY,
                             spaceBefore=10, spaceAfter=6,
                             leading=15),
        'body': ParagraphStyle('body', fontName=FONT_NAME,
                               fontSize=10, leading=14,
                               spaceAfter=6),
        'code': ParagraphStyle('code', fontName='Courier',
                               fontSize=9, leading=12,
                               backColor=SURF, borderColor=BORDER,
                               borderWidth=0.5, borderPadding=6,
                               leftIndent=8, rightIndent=8,
                               spaceAfter=6),
        'note': ParagraphStyle('note', fontName=FONT_NAME,
                               fontSize=9, leading=12,
                               leftIndent=12, rightIndent=12,
                               backColor=SURF,
                               borderPadding=8,
                               textColor=TEXT_MUTED,
                               spaceAfter=8),
        'small': ParagraphStyle('small', fontName=FONT_NAME,
                                fontSize=8, leading=11,
                                textColor=TEXT_MUTED,
                                alignment=TA_CENTER),
    }


def inline_format(text):
    """Apply inline formatting."""
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<i>\1</i>', text)
    text = re.sub(r'`(.+?)`', r'<font face="Courier" backColor="#F8FAFC">\1</font>', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'<u>\1</u>', text)
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<i>[Image: \1]</i>', text)
    return text


def parse_markdown_to_flowables(md_content, styles, title):
    flowables = [Paragraph(title, styles['title']), Spacer(1, 12)]

    lines = md_content.split('\n')
    i = 0
    in_code = False
    code_lines = []
    in_table = False
    table_rows = []
    in_list = False
    list_items = []

    def flush_list():
        nonlocal in_list, list_items
        if in_list and list_items:
            for item in list_items:
                flowables.append(Paragraph("• " + item, styles['body']))
            flowables.append(Spacer(1, 4))
        in_list = False
        list_items = []

    def flush_table():
        nonlocal in_table, table_rows
        if in_table and table_rows:
            header = table_rows[0]
            data_rows = [r for r in table_rows[2:] if r and r[0] != '---']
            if data_rows:
                col_count = max(len(header), max(len(r) for r in data_rows))
                while len(header) < col_count:
                    header.append('')
                for r in data_rows:
                    while len(r) < col_count:
                        r.append('')
                tbl = Table([header] + data_rows, hAlign='LEFT',
                            colWidths=[17/col_count*cm] * col_count)
                tbl.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), SURF),
                    ('TEXTCOLOR', (0, 0), (-1, 0), NAVY),
                    ('FONTNAME', (0, 0), (-1, 0), FONT_NAME_BOLD),
                    ('FONTNAME', (0, 1), (-1, -1), FONT_NAME),
                    ('FONTSIZE', (0, 0), (-1, -1), 8),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('GRID', (0, 0), (-1, -1), 0.25, BORDER),
                    ('PADDING', (0, 0), (-1, -1), 5),
                ]))
                flowables.append(tbl)
                flowables.append(Spacer(1, 8))
        in_table = False
        table_rows = []

    while i < len(lines):
        line = lines[i].rstrip()

        if line.startswith('```'):
            if in_code:
                code_text = '\n'.join(code_lines)
                code_text = code_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                code_text = code_text.replace('\n', '<br/>')
                flowables.append(Paragraph(code_text, styles['code']))
                in_code = False
                code_lines = []
            else:
                flush_list()
                flush_table()
                in_code = True
            i += 1
            continue

        if in_code:
            code_lines.append(line)
            i += 1
            continue

        if not line:
            flush_list()
            flush_table()
            i += 1
            continue

        if line.startswith('#'):
            flush_list()
            flush_table()
            level = len(line) - len(line.lstrip('#'))
            heading_text = inline_format(line.lstrip('#').strip())
            if level == 1:
                flowables.append(Paragraph(heading_text, styles['h1']))
            elif level == 2:
                flowables.append(Paragraph(heading_text, styles['h2']))
            else:
                flowables.append(Paragraph(heading_text, styles['h3']))
            i += 1
            continue

        if line.strip() in ('---', '***', '___'):
            flush_list()
            flush_table()
            flowables.append(Spacer(1, 12))
            i += 1
            continue

        if line.startswith('>'):
            flush_list()
            flush_table()
            flowables.append(Paragraph(inline_format(line[1:].strip()), styles['note']))
            i += 1
            continue

        if line.startswith('|') and line.endswith('|'):
            flush_list()
            cells = [c.strip() for c in line[1:-1].split('|')]
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append([inline_format(c) for c in cells])
            i += 1
            continue
        elif in_table:
            flush_table()

        if re.match(r'^[-*+] ', line) or re.match(r'^\d+\. ', line):
            flush_table()
            if not in_list:
                in_list = True
                list_items = []
            item_text = re.sub(r'^[-*+] ', '', line)
            item_text = re.sub(r'^\d+\. ', '', item_text)
            list_items.append(inline_format(item_text))
            i += 1
            continue
        elif in_list and line.startswith('  '):
            list_items[-1] += ' ' + inline_format(line.strip())
            i += 1
            continue
        else:
            flush_list()

        if re.match(r'^!\[.*?\]\(.*?\)\s*$', line):
            placeholder = re.sub(r'!\[(.*?)\].*', r'[Screenshot: \1 — see HTML version]', line)
            flowables.append(Paragraph(f'<i>{placeholder}</i>', styles['small']))
            flowables.append(Spacer(1, 6))
            i += 1
            continue

        flowables.append(Paragraph(inline_format(line), styles['body']))
        i += 1

    flush_list()
    flush_table()

    flowables.append(Spacer(1, 18))
    flowables.append(Paragraph(
        'NVH Source Locator — EVDiag — support@evdiag.net',
        styles['small']
    ))
    return flowables


def generate_pdf(md_path, pdf_path, title):
    if not os.path.exists(md_path):
        return False
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    doc = SimpleDocTemplate(
        pdf_path, pagesize=A4,
        rightMargin=2*cm, leftMargin=2*cm,
        topMargin=2*cm, bottomMargin=2*cm,
        title=title, author='EVDiag'
    )
    styles = make_styles()
    flowables = parse_markdown_to_flowables(md_content, styles, title)
    try:
        doc.build(flowables)
        return True
    except Exception as e:
        print(f"  ERROR building {pdf_path}: {e}")
        return False


def main():
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from translations_ui import TRANSLATIONS, LANGUAGE_ORDER

    for locale in LANGUAGE_ORDER:
        ui = TRANSLATIONS.get(locale) or TRANSLATIONS['en']
        if ui.get('_fallback'):
            from translations_ui import TRANSLATIONS as T
            ui_en = T['en']
            qr_title = f"NVH Source Locator — {ui_en['quick_ref_title']}"
            ug_title = f"NVH Source Locator — {ui_en['user_guide_title']}"
        else:
            qr_title = f"NVH Source Locator — {ui['quick_ref_title']}"
            ug_title = f"NVH Source Locator — {ui['user_guide_title']}"

        locale_dir = os.path.join(DOCS_ROOT, locale)
        qr_md = os.path.join(locale_dir, 'quick-reference.md')
        qr_pdf = os.path.join(locale_dir, 'quick-reference.pdf')
        ug_md = os.path.join(locale_dir, 'user-guide.md')
        ug_pdf = os.path.join(locale_dir, 'user-guide.pdf')

        qr_ok = generate_pdf(qr_md, qr_pdf, qr_title)
        ug_ok = generate_pdf(ug_md, ug_pdf, ug_title)
        print(f"  {locale}: QR={'OK' if qr_ok else 'SKIP'} UG={'OK' if ug_ok else 'SKIP'}")


if __name__ == '__main__':
    main()
