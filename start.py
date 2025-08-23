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
    print(f"📍 Python Version: {sys.version}")
    print(f"📁 Working Directory: {os.getcwd()}")
    print(f"📋 Toplam Environment Variables: {len(os.environ)}")
    
    # Tüm environment variables'ları listele (güvenlik için filtrelenmiş)
    print("\n🔑 Environment Variables:")
    for key, value in sorted(os.environ.items()):
        if any(keyword in key.upper() for keyword in ['TOKEN', 'BOT', 'RAILWAY', 'PORT', 'URL']):
            if 'TOKEN' in key.upper():
                display_value = f"{value[:5]}...{value[-3:]}" if value and len(value) > 8 else "GIZLI"
            else:
                display_value = value
            print(f"   {key} = {display_value}")
    
    # BOT_TOKEN kontrol
    bot_token = os.getenv('BOT_TOKEN')
    if not bot_token:
        print("\n❌ BOT_TOKEN bulunamadı!")
        print("\n🛠️ Railway'de BOT_TOKEN ayarlamak için:")
        print("1. Railway dashboard → Variables sekmesi")
        print("2. 'New Variable' → Name: BOT_TOKEN")
        print("3. Value: BotFather'dan aldığınız token")
        print("4. Deploy'u yeniden başlatın")
        return False
    
    print(f"\n✅ BOT_TOKEN bulundu ({len(bot_token)} karakter)")
    print(f"🔑 Token preview: {bot_token[:10]}...{bot_token[-5:] if len(bot_token) > 15 else bot_token}")
    return True

def start_bot(retry_count=0):
    """Bot'u başlat"""
    max_retries = 3
    
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