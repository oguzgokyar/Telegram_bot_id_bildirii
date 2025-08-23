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
        
        # Bot token'ı kontrol et ve environment'a set et
        bot_token = os.getenv('BOT_TOKEN')
        if bot_token:
            print(f"✅ BOT_TOKEN mevcut ({len(bot_token)} karakter)")
            # Environment'a kesin olarak set et (cache sorunları için)
            os.environ['BOT_TOKEN'] = bot_token
            print(f"🔧 BOT_TOKEN environment'a yeniden set edildi")
        else:
            print("⚠️ BOT_TOKEN bulunamadı - bot.py kendi kontrolünü yapacak")
        
        print("🤖 Bot başlatılıyor...")
        
        # Imports'u güvenli şekilde yap
        try:
            print("📦 Bot modülü import ediliyor...")
            # Önce telegram kütüphanesini test et
            try:
                import telegram
                print("✅ telegram kütüphanesi mevcut")
            except ImportError as telegram_error:
                print(f"❌ telegram kütüphanesi import hatası: {telegram_error}")
                print("🛠️ Çözüm: pip install python-telegram-bot")
                raise telegram_error
            
            # Şimdi bot modülünü import et
            import bot
            print("✅ Bot modülü başarıyla import edildi!")
            print("🎉 Bot başarıyla çalışıyor!")
            
        except ImportError as import_error:
            print(f"❌ Import hatası: {import_error}")
            print("🔍 Kullanılabilir modüller kontrol ediliyor...")
            
            # Mevcut modülleri listele
            import pkg_resources
            installed_packages = [d.project_name for d in pkg_resources.working_set]
            print(f"📋 Yüklü paketler ({len(installed_packages)} adet):")
            telegram_related = [p for p in installed_packages if 'telegram' in p.lower()]
            if telegram_related:
                print(f"🔍 Telegram ile ilgili paketler: {telegram_related}")
            else:
                print("❌ Telegram ile ilgili paket bulunamadı!")
            
            raise import_error
        
    except ImportError as e:
        print(f"❌ Bot modülü import edilemedi: {e}")
        print("🛠️ Dependencies kontrol edin: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Bot başlatılırken hata: {e}")
        print(f"🔍 Hata tipi: {type(e).__name__}")
        
        if retry_count < max_retries:
            wait_time = 5 * (retry_count + 1)  # Her denemede daha uzun bekle
            print(f"🔄 {wait_time} saniye sonra tekrar denenecek... (Deneme {retry_count + 1}/{max_retries})")
            time.sleep(wait_time)
            start_bot(retry_count + 1)
        else:
            print(f"❌ Maksimum deneme sayısına ulaşıldı ({max_retries}). Bot başlatılamadı.")
            print("🛠️ Lütfen Railway'de BOT_TOKEN environment variable'ının doğru ayarlandığından emin olun.")
            print("🛠️ Veya dependencies kurulum sorunları olabilir.")
            sys.exit(1)

if __name__ == '__main__':
    start_bot()