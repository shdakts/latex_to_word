# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 20:13:30 2025

@author: Suheda
"""

import subprocess
import shutil

def latex_to_word(latex_file, output_file):
    """
    LaTeX dosyasını Word formatına (docx) dönüştürür.
    
    Args:
        latex_file (str): Dönüştürülecek LaTeX dosyasının tam dosya yolu. 
                          
        output_file (str): Oluşturulacak Word dosyasının tam dosya yolu. 
                           
    
    Returns:
        None: Fonksiyon bir değer döndürmez.
    """
    # Pandoc'un kurulu olup olmadığını kontrol et
    if not shutil.which("pandoc"):
        raise EnvironmentError("Pandoc yüklü değil. Lütfen Pandoc'u yükleyin.")
    
    try:
        # Pandoc komutunu çalıştır
        subprocess.run(
            ["pandoc", latex_file, "-o", output_file],
            check=True
        )
        print(f"Dönüştürme tamamlandı: {output_file}")
    except subprocess.CalledProcessError as e:
        print("Dönüştürme sırasında bir hata oluştu:", e)

# Örnek kullanım
latex_file = "C:/Users/User/Desktop/simple.tex"  # LaTeX dosyasının tam yolu
output_file = "C:/Users/User/Desktop/simple.docx"  # Çıkış Word dosyasının tam yolu

# Fonksiyonu çağır
latex_to_word(latex_file, output_file)

