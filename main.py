import os
from PIL import Image

def combine_images(filenames: list[str], output_filename: str) -> None:
  if not filenames:
    raise ValueError("Список файлів не може бути пустим.")

  images = []
  for filename in filenames:
    if not os.path.isfile(filename):
      raise ValueError(f"Файл '{filename}' не існує.")
    images.append(Image.open(filename))

  widths = [image.width for image in images]
  if not all(width == widths[0] for width in widths):
    raise ValueError("Всі зображення повинні мати однакову ширину.")

  combined_image = Image.new("RGB", (widths[0], sum(image.height for image in images)))
  y_offset = 0
  for image in images:
    combined_image.paste(image, (0, y_offset))
    y_offset += image.height

  combined_image.save(output_filename)


filenames: list[str] = [
  "1.png",
  "2.png",
  "3.png",
  "4.png",
  "5.png",
  "6.png",
  "7.png",
  "8.png",
]
output_filename: str = "result.png"

combine_images(filenames, output_filename)

print(f"Зображення успішно об'єднано: {output_filename}")
