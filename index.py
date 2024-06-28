import os
import shutil

# Define the path to the Downloads folder
downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

# Define the target folders for different file types
folders = {
    'DOCUMENTS': ['.pdf', '.doc', '.docx', '.txt', '.odt', '.ppt', '.pptx', '.xls', '.xlsx'],
    'MUSIC': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
    'VIDEOS': ['.mp4', '.mkv', '.flv', '.avi', '.mov', '.wmv', '.webm'],
    'IMAGES': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'ARCHIVES': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'PROGRAMS': ['.exe', '.msi', '.deb', '.rpm', '.dmg'],
    'OTHERS': []
}

# Create the target folders if they don't exist
for folder in folders:
    folder_path = os.path.join(downloads_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files to the corresponding folders
for item in os.listdir(downloads_path):
    item_path = os.path.join(downloads_path, item)
    if os.path.isfile(item_path):
        file_extension = os.path.splitext(item)[1].lower()
        moved = False
        for folder, extensions in folders.items():
            if file_extension in extensions:
                shutil.move(item_path, os.path.join(downloads_path, folder, item))
                moved = True
                break
        if not moved:
            shutil.move(item_path, os.path.join(downloads_path, 'OTHERS', item))

print("Files have been organized.")
