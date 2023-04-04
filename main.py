import flet
from flet import (Page,TextField,Image, Text, Row, ElevatedButton, icons, FilePicker, FilePickerResultEvent)
from io import BytesIO

import qrcode
import base64

def morning(s):
    qr = qrcode.make(s)
    buffered = BytesIO()
    qr.save(buffered, format="PNG")
    s1 = base64.b64encode(buffered.getvalue())
    resultOfQrCode = s1.decode("utf-8")
    
    return resultOfQrCode


def main(page: Page):
    page.scroll = "always"
    page.vertical_alignments = "center"
    page.horizontal_alignments = "center"
    
    def procedtocode(e):
        url = morning(txt.value)
        img = Image(src_base64=url)
        page.add(img)
        page.update()
    
    txt = TextField(label="Ingrese un texto")
    
    btn = ElevatedButton("Crear QR",
                    icon=icons.QR_CODE,
                    bgcolor='blue',
                    color='white',
                    on_click=procedtocode
                )
    
    page.add(txt)
    page.add(btn)
    
    

flet.app(target=main)