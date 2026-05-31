#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Descargador Multi-Plataforma
Descarga videos y medios de múltiples plataformas
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path
from datetime import datetime

class Descargador:
    def __init__(self, carpeta_destino="descargas"):
        self.carpeta_destino = carpeta_destino
        self.crear_carpeta()
        
    def crear_carpeta(self):
        """Crea la carpeta de descargas si no existe"""
        Path(self.carpeta_destino).mkdir(exist_ok=True)
        print(f"✓ Carpeta de destino: {self.carpeta_destino}")
    
    def verificar_dependencias(self):
        """Verifica si yt-dlp está instalado"""
        try:
            subprocess.run(["yt-dlp", "--version"], 
                         capture_output=True, check=True)
            print("✓ yt-dlp detectado")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("✗ yt-dlp no instalado")
            print("  Instala con: pip install yt-dlp")
            return False
    
    def descargar_youtube(self, url):
        """Descarga de YouTube"""
        print(f"\n📥 Descargando de YouTube: {url}")
        try:
            cmd = [
                "yt-dlp",
                "-f", "best",
                "-o", f"{self.carpeta_destino}/%(title)s.%(ext)s",
                url
            ]
            subprocess.run(cmd, check=True)
            print("✓ Descarga completada")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Error: {e}")
            return False
    
    def descargar_tiktok(self, url):
        """Descarga de TikTok"""
        print(f"\n📥 Descargando de TikTok: {url}")
        try:
            cmd = [
                "yt-dlp",
                "-f", "best",
                "-o", f"{self.carpeta_destino}/tiktok_%(id)s.%(ext)s",
                url
            ]
            subprocess.run(cmd, check=True)
            print("✓ Descarga completada")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Error: {e}")
            return False
    
    def descargar_instagram(self, url):
        """Descarga de Instagram"""
        print(f"\n📥 Descargando de Instagram: {url}")
        try:
            cmd = [
                "yt-dlp",
                "-f", "best",
                "-o", f"{self.carpeta_destino}/instagram_%(id)s.%(ext)s",
                url
            ]
            subprocess.run(cmd, check=True)
            print("✓ Descarga completada")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Error: {e}")
            return False
    
    def descargar_twitter(self, url):
        """Descarga de Twitter/X"""
        print(f"\n📥 Descargando de Twitter/X: {url}")
        try:
            cmd = [
                "yt-dlp",
                "-f", "best",
                "-o", f"{self.carpeta_destino}/twitter_%(id)s.%(ext)s",
                url
            ]
            subprocess.run(cmd, check=True)
            print("✓ Descarga completada")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Error: {e}")
            return False
    
    def descargar_facebook(self, url):
        """Descarga de Facebook"""
        print(f"\n📥 Descargando de Facebook: {url}")
        try:
            cmd = [
                "yt-dlp",
                "-f", "best",
                "-o", f"{self.carpeta_destino}/facebook_%(id)s.%(ext)s",
                url
            ]
            subprocess.run(cmd, check=True)
            print("✓ Descarga completada")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Error: {e}")
            return False
    
    def descargar_twitch(self, url):
        """Descarga de Twitch"""
        print(f"\n📥 Descargando de Twitch: {url}")
        try:
            cmd = [
                "yt-dlp",
                "-f", "best",
                "-o", f"{self.carpeta_destino}/twitch_%(id)s.%(ext)s",
                url
            ]
            subprocess.run(cmd, check=True)
            print("✓ Descarga completada")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Error: {e}")
            return False
    
    def descargar_vimeo(self, url):
        """Descarga de Vimeo"""
        print(f"\n📥 Descargando de Vimeo: {url}")
        try:
            cmd = [
                "yt-dlp",
                "-f", "best",
                "-o", f"{self.carpeta_destino}/vimeo_%(id)s.%(ext)s",
                url
            ]
            subprocess.run(cmd, check=True)
            print("✓ Descarga completada")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Error: {e}")
            return False
    
    def descargar_dailymotion(self, url):
        """Descarga de Dailymotion"""
        print(f"\n📥 Descargando de Dailymotion: {url}")
        try:
            cmd = [
                "yt-dlp",
                "-f", "best",
                "-o", f"{self.carpeta_destino}/dailymotion_%(id)s.%(ext)s",
                url
            ]
            subprocess.run(cmd, check=True)
            print("✓ Descarga completada")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Error: {e}")
            return False
    
    def descargar_reddit(self, url):
        """Descarga de Reddit"""
        print(f"\n📥 Descargando de Reddit: {url}")
        try:
            cmd = [
                "yt-dlp",
                "-f", "best",
                "-o", f"{self.carpeta_destino}/reddit_%(id)s.%(ext)s",
                url
            ]
            subprocess.run(cmd, check=True)
            print("✓ Descarga completada")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Error: {e}")
            return False
    
    def detectar_plataforma(self, url):
        """Detecta automáticamente la plataforma"""
        url_lower = url.lower()
        
        if "youtube.com" in url_lower or "youtu.be" in url_lower:
            return "youtube"
        elif "tiktok.com" in url_lower:
            return "tiktok"
        elif "instagram.com" in url_lower:
            return "instagram"
        elif "twitter.com" in url_lower or "x.com" in url_lower:
            return "twitter"
        elif "facebook.com" in url_lower or "fb.watch" in url_lower:
            return "facebook"
        elif "twitch.tv" in url_lower:
            return "twitch"
        elif "vimeo.com" in url_lower:
            return "vimeo"
        elif "dailymotion.com" in url_lower:
            return "dailymotion"
        elif "reddit.com" in url_lower:
            return "reddit"
        else:
            return "desconocida"
    
    def descargar(self, url, plataforma=None):
        """Descarga desde URL (detecta o usa plataforma especificada)"""
        if not self.verificar_dependencias():
            return False
        
        # Detectar plataforma si no se especifica
        if plataforma is None:
            plataforma = self.detectar_plataforma(url)
        
        plataforma = plataforma.lower()
        
        print(f"\n🔍 Plataforma detectada: {plataforma}")
        print(f"🕐 Inicio: {datetime.now().strftime('%H:%M:%S')}")
        
        # Router de plataformas
        if plataforma == "youtube":
            return self.descargar_youtube(url)
        elif plataforma == "tiktok":
            return self.descargar_tiktok(url)
        elif plataforma == "instagram":
            return self.descargar_instagram(url)
        elif plataforma == "twitter":
            return self.descargar_twitter(url)
        elif plataforma == "facebook":
            return self.descargar_facebook(url)
        elif plataforma == "twitch":
            return self.descargar_twitch(url)
        elif plataforma == "vimeo":
            return self.descargar_vimeo(url)
        elif plataforma == "dailymotion":
            return self.descargar_dailymotion(url)
        elif plataforma == "reddit":
            return self.descargar_reddit(url)
        else:
            # Intenta con yt-dlp genérico
            print(f"\n📥 Intentando descargar (plataforma genérica): {url}")
            try:
                cmd = [
                    "yt-dlp",
                    "-f", "best",
                    "-o", f"{self.carpeta_destino}/%(title)s.%(ext)s",
                    url
                ]
                subprocess.run(cmd, check=True)
                print("✓ Descarga completada")
                return True
            except subprocess.CalledProcessError as e:
                print(f"✗ Error: {e}")
                return False
    
    def listar_descargas(self):
        """Lista todos los archivos descargados"""
        print(f"\n📁 Archivos en {self.carpeta_destino}:")
        try:
            archivos = list(Path(self.carpeta_destino).iterdir())
            if not archivos:
                print("  (Carpeta vacía)")
                return
            
            for archivo in sorted(archivos):
                tamaño = archivo.stat().st_size / (1024 * 1024)  # MB
                print(f"  • {archivo.name} ({tamaño:.2f} MB)")
        except Exception as e:
            print(f"✗ Error: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Descargador Multi-Plataforma",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python descargador.py "https://www.youtube.com/watch?v=..."
  python descargador.py "https://www.tiktok.com/..." --carpeta mis_descargas
  python descargador.py "https://instagram.com/..." --listar
        """
    )
    
    parser.add_argument("url", nargs="?", help="URL del video a descargar")
    parser.add_argument("-c", "--carpeta", default="descargas", 
                       help="Carpeta de destino (default: descargas)")
    parser.add_argument("-p", "--plataforma", 
                       help="Especificar plataforma (youtube, tiktok, instagram, etc.)")
    parser.add_argument("-l", "--listar", action="store_true",
                       help="Listar archivos descargados")
    parser.add_argument("-m", "--multiple", nargs="+",
                       help="Descargar múltiples URLs")
    
    args = parser.parse_args()
    
    # Crear instancia
    descargador = Descargador(args.carpeta)
    
    # Listar descargas
    if args.listar:
        descargador.listar_descargas()
        return
    
    # Descargar múltiples
    if args.multiple:
        for url in args.multiple:
            descargador.descargar(url, args.plataforma)
        return
    
    # Descargar una URL
    if args.url:
        descargador.descargar(args.url, args.plataforma)
    else:
        print("⚠️  Uso: python descargador.py <URL>")
        print("     O: python descargador.py --help")

if __name__ == "__main__":
    main()
