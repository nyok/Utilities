import os
from PIL import Image

def create_thumbnails(input_folder, output_folder, thumbnail_size=(500, 500)):
    # Проверяем, существует ли папка для миниатюр, и создаем ее, если она не существует
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Проходим по всем папкам и файлам в заданной директории
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            # Проверяем, что файл имеет расширение изображения
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                # Создаем путь к исходному файлу и миниатюре
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_folder, os.path.relpath(input_path, input_folder))
                output_dir = os.path.dirname(output_path)

                # Проверяем, существует ли папка для миниатюры, и создаем ее, если она не существует
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                # Открываем изображение и создаем миниатюру
                image = Image.open(input_path)
                image.thumbnail(thumbnail_size)

                # Сохраняем миниатюру
                image.save(output_path)


if __name__ == "__main__":
    input_folder = "/Images"
    output_folder = "/Images_thumbnails"
    create_thumbnails(input_folder, output_folder)
