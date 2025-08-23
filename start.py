#!/usr/bin/env python3
"""
Railway için güvenli bot başlatma scripti
"""

import os
import sys
import time

def check_environment():
    """Environment variables'ları kontrol et"""
    print("🔍 Environment kontrol ediliyor...")
    
    # BOT_TOKEN kontrol
    bot_token = os.getenv('BOT_TOKEN')
    if not bot_token:
        print("❌ BOT_TOKEN bulunamadı!")
        print("\n🛠️ Railway'de BOT_TOKEN ayarlamak için:")
        print("1. Railway dashboard → Variables sekmesi")
        print("2. 'New Variable' → Name: BOT_TOKEN")
        print("3. Value: BotFather'dan aldığınız token")
        print("4. Deploy'u yeniden başlatın")
        return False
    
    print(f"✅ BOT_TOKEN bulundu ({len(bot_token)} karakter)")
    return True

def start_bot():
    """Bot'u başlat"""
    try:
        # Environment kontrol
        if not check_environment():
            print("❌ Environment variables eksik. Bot başlatılamıyor.")
            sys.exit(1)
        
        print("🤖 Bot başlatılıyor...")
        
        # bot.py'yi import et ve çalıştır
        import bot
        
    except ImportError as e:
        print(f"❌ Bot modülü import edilemedi: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Bot başlatılırken hata: {e}")
        print("🔄 5 saniye sonra tekrar denenecek...")
        time.sleep(5)
        start_bot()

if __name__ == '__main__':
    start_bot()