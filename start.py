#!/usr/bin/env python3
"""
Railway için güvenli bot başlatma scripti
"""

import os
import sys
import time

def start_bot(retry_count=0):
    """Bot'u başlat"""
    max_retries = 3
    
    try:
        print(f"🔍 Environment kontrol ediliyor...")
        print(f"📍 Python Version: {sys.version.split()[0]}")
        print(f"📁 Working Directory: {os.getcwd()}")
        
        # Bot token'ı debug için kontrol et (ama hatada çıkmaz)
        bot_token = os.getenv('BOT_TOKEN')
        if bot_token:
            print(f"✅ BOT_TOKEN mevcut ({len(bot_token)} karakter)")
        else:
            print("⚠️ BOT_TOKEN bulunamadı - bot.py kendi kontrolünü yapacak")
        
        print("🤖 Bot başlatılıyor...")
        
        # bot.py'yi import et ve çalıştır - kendi BOT_TOKEN kontrolünü yapacak
        import bot
        
    except ImportError as e:
        print(f"❌ Bot modülü import edilemedi: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Bot başlatılırken hata: {e}")
        
        if retry_count < max_retries:
            wait_time = 5 * (retry_count + 1)  # Her denemede daha uzun bekle
            print(f"🔄 {wait_time} saniye sonra tekrar denenecek... (Deneme {retry_count + 1}/{max_retries})")
            time.sleep(wait_time)
            start_bot(retry_count + 1)
        else:
            print(f"❌ Maksimum deneme sayısına ulaşıldı ({max_retries}). Bot başlatılamadı.")
            print("🛠️ Lütfen Railway'de BOT_TOKEN environment variable'ının doğru ayarlandığından emin olun.")
            sys.exit(1)

if __name__ == '__main__':
    start_bot()