import os
import shutil
from pathlib import Path

def normalize(some_string):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "c", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    NUMBERS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '.')
    TRANS = {}
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()    
    
    def translate(name):
        name = name.translate(TRANS)
        return name
    
    some_string = translate(some_string)
    
    for val in some_string:
        if (not val in CYRILLIC_SYMBOLS) and (not val in TRANSLATION) and (not val in NUMBERS):
            some_string = some_string.replace(val, '_')
            
    return some_string   
    
def run():
    Path('archives').mkdir(exist_ok=True)
    Path('video').mkdir(exist_ok=True)
    Path('audio').mkdir(exist_ok=True)
    Path('documents').mkdir(exist_ok=True)
    Path('images').mkdir(exist_ok=True)


    for file in os.listdir():
        for name in file:
            normalize(name)
        
        if file == 'archives' or file == 'video' or file == 'audio' or file == 'documents' or file == 'images':
            continue
        if file.lower().endswith('.jpg') == True or file.lower().endswith('.png') == True or file.lower().endswith('.jpeg') == True or file.lower().endswith('.svg') == True:
            shutil.move(file, 'images')
            
        if file.lower().endswith('.pdf') == True or file.lower().endswith('.txt') == True or file.lower().endswith('.doc') == True or file.lower().endswith('.docx') == True or file.lower().endswith('.xlsx') == True or file.lower().endswith('.pptx') == True:
            shutil.move(file, 'documents')
        
        if file.lower().endswith('.avi') == True or file.lower().endswith('.mp4') == True or file.lower().endswith('.mov') == True or file.lower().endswith('.mkv') == True:
            shutil.move(file, 'video')
            
        if file.lower().endswith('.mp3') == True or file.lower().endswith('.ogg') == True or file.lower().endswith('.wav') == True or file.lower().endswith('.amr') == True:
            shutil.move(file, 'audio')
            
        if file.lower().endswith('.zip') == True or file.lower().endswith('.gz') == True or file.lower().endswith('.tar') == True:
            shutil.move(file, 'archives')
        else: 
            continue 