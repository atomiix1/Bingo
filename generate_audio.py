#!/usr/bin/env python3
"""
Script para generar archivos de audio para el Bingo 1-90
Genera archivos de audio MP3 para cada número del 1 al 90
Requisitos: pip install gTTS
"""

from gtts import gTTS
import os
from pathlib import Path

def generate_audio_files(output_dir="audio"):
    """
    Genera archivos de audio MP3 para números del 1 al 90
    
    Args:
        output_dir (str): Directorio donde guardar los archivos de audio
    """
    
    # Crear directorio si no existe
    Path(output_dir).mkdir(exist_ok=True)
    
    print(f"Generando archivos de audio en: {output_dir}/")
    print("-" * 50)
    
    try:
        # Generar audios para números del 1 al 90
        for number in range(1, 91):
            try:
                # Crear objeto de texto a voz en español
                tts = gTTS(text=str(number), lang='es', slow=False)
                
                # Nombre del archivo
                filename = f"{output_dir}/{number:02d}.mp3"
                
                # Guardar archivo
                tts.save(filename)
                
                print(f"✓ {number:2d} -> {filename}")
                
            except Exception as e:
                print(f"✗ Error generando audio para {number}: {e}")
        
        # Generar audio para "Fin del bingo"
        print("\nGenerando audios especiales...")
        try:
            tts = gTTS(text="Fin del bingo", lang='es', slow=False)
            tts.save(f"{output_dir}/fin.mp3")
            print("✓ Fin del bingo -> audio/fin.mp3")
        except Exception as e:
            print(f"✗ Error generando audio para 'Fin del bingo': {e}")
        
        print("-" * 50)
        print(f"✓ Audios generados exitosamente en carpeta '{output_dir}/'")
        
    except Exception as e:
        print(f"Error general: {e}")


def generate_audio_local_version(output_dir="audio"):
    """
    Versión alternativa que genera archivos de audio usando pyttsx3 (sin conexión a internet)
    Requisitos: pip install pyttsx3
    """
    try:
        import pyttsx3
    except ImportError:
        print("pyttsx3 no está instalado. Instálalo con: pip install pyttsx3")
        return
    
    # Crear directorio si no existe
    Path(output_dir).mkdir(exist_ok=True)
    
    print(f"Generando archivos de audio con pyttsx3 en: {output_dir}/")
    print("-" * 50)
    
    # Inicializar motor TTS
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Velocidad
    engine.setProperty('volume', 1)   # Volumen
    
    # Configurar idioma español
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'spanish' in voice.name.lower() or 'español' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    
    try:
        # Generar audios para números del 1 al 90
        for number in range(1, 91):
            try:
                filename = f"{output_dir}/{number:02d}.mp3"
                engine.save_to_file(str(number), filename)
                engine.runAndWait()
                print(f"✓ {number:2d} -> {filename}")
                
            except Exception as e:
                print(f"✗ Error generando audio para {number}: {e}")
        
        # Generar audio para "Fin del bingo"
        print("\nGenerando audios especiales...")
        try:
            filename = f"{output_dir}/fin.mp3"
            engine.save_to_file("Fin del bingo", filename)
            engine.runAndWait()
            print("✓ Fin del bingo -> audio/fin.mp3")
        except Exception as e:
            print(f"✗ Error generando audio para 'Fin del bingo': {e}")
        
        print("-" * 50)
        print(f"✓ Audios generados exitosamente en carpeta '{output_dir}/'")
        
    except Exception as e:
        print(f"Error general: {e}")


if __name__ == "__main__":
    import sys
    
    print("=" * 50)
    print("GENERADOR DE AUDIOS PARA BINGO 1-90")
    print("=" * 50)
    
    # Por defecto usar gTTS (requiere internet)
    if len(sys.argv) > 1 and sys.argv[1] == "--local":
        generate_audio_local_version()
    else:
        generate_audio_files()
    
    print("\n💡 Usa los archivos de audio como se muestra en 'usar_audios.py'")