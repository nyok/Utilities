import os

def create_gallery_page(input_folder, output_folder):
    # Проверяем, существует ли папка для миниатюр, и создаем ее, если она не существует
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Путь к файлу gallery.html в корневой папке
    output_file = os.path.join(input_folder, "gallery.html")

    # Открываем файл для записи HTML
    with open(output_file, "w") as html_file:
        # Начинаем запись HTML-кода
        html_file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Gallery</title>\n")
        # Добавляем стили
        html_file.write('<style> body { font-family: Arial, sans-serif; } h2 { font-size: 1.2em; } img { width: 250px; } </style>\n')
        html_file.write("</head>\n<body>\n")

        # Проходим по всем папкам и файлам в заданной директории
        for root, dirs, files in os.walk(output_folder):
            # Отображаем имя текущей папки с учетом вложенности
            depth = root[len(output_folder):].count(os.sep)
            html_file.write(f"<div style='margin-left: {depth * 10}px;'>")
            html_file.write(f"<h2>{os.path.basename(root)}</h2>\n")

            # Отображаем изображения в текущей папке
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    img_path = os.path.join(root, file)
                    html_file.write(f'<img src="{img_path}" alt="{file}">\n')
            html_file.write(f"</div>")

        # Завершаем запись HTML-кода
        html_file.write("</body>\n</html>")

if __name__ == "__main__":
    input_folder = "/Images/"
    output_folder = "/Images_thumbnails"
    create_gallery_page(input_folder, output_folder)
