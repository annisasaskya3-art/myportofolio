import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Buka browser Chrome
driver = webdriver.Chrome()

try:
    # 2. Buka halaman utama
    driver.get("http://localhost:8000/")
    time.sleep(2)  # Tahan 2 detik biar kelihatan
    
    # 3. Cek apakah title halaman ada
    print("Judul Halaman:", driver.title)
    
    # 4. Coba buka halaman login
    driver.get("http://localhost:8000/login/")
    time.sleep(2)
    print("Berhasil buka halaman login!")

finally:
    # 5. Tutup browser
    driver.quit()