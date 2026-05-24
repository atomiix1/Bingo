#!/usr/bin/env python3
"""
Script para generar archivos de audio de números del 1 al 90 en español
usando gTTS (Google Text-to-Speech)
"""

from gtts import gTTS
import os

# Crear carpeta de audios si no existe
audio_folder = "audio"
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

# Generar audios para números del 1 al 90
for i in range(1, 91):
    try:
        tts = gTTS(text=str(i), lang='es', slow=False)
        filename = os.path.join(audio_folder, f"{i}.mp3")
        tts.save(filename)
        print(f"✓ Audio generado: {filename}")
    except Exception as e:
        print(f"✗ Error generando audio para {i}: {e}")

# Generar audio para "Fin del bingo"
try:
    tts = gTTS(text="Fin del bingo", lang='es', slow=False)
    filename = os.path.join(audio_folder, "fin.mp3")
    tts.save(filename)
    print(f"✓ Audio generado: {filename}")
except Exception as e:
    print(f"✗ Error generando audio para 'Fin del bingo': {e}")

print("\n¡Audios generados correctamente en la carpeta 'audio'!")
