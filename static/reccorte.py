from PIL import Image
from pathlib import Path

carpeta_origen = Path('static/Imagenes')
carpeta_destino = Path('static/Imagenes')
carpeta_destino.mkdir(parents=True, exist_ok=True)

TAMANO_MAXIMO = (500, 500)

for archivo in carpeta_origen.iterdir():
    if archivo.suffix.lower() not in ['.jpg', '.jpeg', '.png', '.webp']:
        continue

    img = Image.open(archivo)
    img = img.convert('RGB')  # necesario para guardar como jpg
    img.thumbnail(TAMANO_MAXIMO)  # redimensiona manteniendo proporción

    destino = carpeta_destino / f"{archivo.stem}.jpg"
    img.save(destino, 'JPEG', quality=80)
    print(f"{archivo.name} -> {destino.name} ({img.size[0]}x{img.size[1]})")
