from PIL import Image, ImageDraw, ImageFont
import datetime

def crear_recibo_imagen(dna, nombre, fecha, monto, no_recibo, concepto, folio, id_transaccion, archivo_salida):
    # Crear una nueva imagen en blanco
    width, height = 600, 700
    imagen = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(imagen)
    
    # Cargar fuentes
    font_path = "arial.ttf"  # Ruta a la fuente Arial, ajustar según el entorno
    font_title = ImageFont.truetype(font_path, 24)
    font_subtitle = ImageFont.truetype(font_path, 20)
    font_text = ImageFont.truetype(font_path, 16)
    font_mono = ImageFont.truetype(font_path, 18)
    font_bold = ImageFont.truetype(font_path, 20)
    
    # Título
    draw.text((width / 2 - 170, 30), "Dirección del Oxxo donde", font=font_title, fill="black")
    draw.text((width / 2 - 80, 70), "realizaste el pago", font=font_title, fill="black")
    
    # Línea punteada
    draw.line((20, 110, width - 20, 110), fill="black", width=2)
    draw.line((20, 114, width - 20, 114), fill="black", width=2)
    
    # Información del recibo
    draw.text((20, 130), f"GAMECA0110000    1    {fecha}", font=font_text, fill="black")
    
    # Caja de cobro de EBANX
    draw.rectangle([150, 160, 450, 200], outline="blue", width=2)
    draw.text((200, 170), "COBRO DE EBANX", font=font_text, fill="black")
    
    # Información de pago
    draw.text((20, 220), f"PAGADA EL DÍA {fecha} A LAS {datetime.datetime.now().strftime('%H:%M')}", font=font_text, fill="black")
    draw.text((20, 250), f"EN EL TICKET #{no_recibo}", font=font_text, fill="black")
    draw.text((20, 280), f"FOLIO DE CONTROL # {folio}", font=font_text, fill="black")
    draw.text((20, 310), f"REFERENCIA {id_transaccion}", font=font_mono, fill="black")
    
    # Valor
    draw.text((width / 2 - 60, 350), f"VALOR ${monto:.2f}", font=font_bold, fill="black")
    
    # Línea punteada
    draw.line((20, 390, width - 20, 390), fill="black", width=2)
    draw.line((20, 394, width - 20, 394), fill="black", width=2)
    
    # Folio e ID
    draw.text((20, 410), f"FOL: {folio}", font=font_text, fill="black")
    draw.text((20, 440), f"ID: {id_transaccion}", font=font_text, fill="black")
    
    # Nota de conservación
    draw.text((width / 2 - 120, 470), "*CONSERVE ESTE COMPROBANTE*", font=font_text, fill="black")
    
    # Guardar la imagen
    imagen.save(archivo_salida)
    print(f"Recibo de pago guardado como {archivo_salida}")

# Ejemplo de uso
dna = "12345678A"
nombre = "Juan Pérez"
fecha = datetime.datetime.now().strftime("%d/%m/%Y")
monto = 150.75
no_recibo = "0001"
concepto = "Pago de servicios"
folio = "1234"
id_transaccion = "1OTLC50DIH"
archivo_salida = "recibo_pago.png"

crear_recibo_imagen(dna, nombre, fecha, monto, no_recibo, concepto, folio, id_transaccion, archivo_salida)
