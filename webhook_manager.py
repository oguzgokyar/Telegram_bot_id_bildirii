#!/usr/bin/env python3
"""
Telegram webhook temizleme ve kurulum scripti
Eski webhook'ları temizler ve yeni webhook kurar
"""

import os
import requests
import json

def clear_and_set_webhook():
    """Eski webhook'ı temizle ve yeni webhook kur"""
    
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    RAILWAY_STATIC_URL = os.getenv('RAILWAY_STATIC_URL')
    RAILWAY_PUBLIC_DOMAIN = os.getenv('RAILWAY_PUBLIC_DOMAIN')
    
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN bulunamadı!")
        return False
    
    # Telegram Bot API base URL
    api_base = f"https://api.telegram.org/bot{BOT_TOKEN}"
    
    print("🔍 Mevcut webhook durumunu kontrol ediyoruz...")
    
    # Mevcut webhook bilgisini al
    try:
        response = requests.get(f"{api_base}/getWebhookInfo")
        webhook_info = response.json()
        
        if webhook_info.get('ok'):
            current_url = webhook_info.get('result', {}).get('url', '')
            print(f"📋 Mevcut webhook URL: {current_url if current_url else 'Webhook yok'}")
            
            # Webhook'ı temizle
            print("🧹 Eski webhook temizleniyor...")
            clear_response = requests.post(f"{api_base}/deleteWebhook")
            if clear_response.json().get('ok'):
                print("✅ Eski webhook temizlendi!")
            else:
                print("⚠️ Webhook temizlenirken sorun oldu")
        
    except Exception as e:
        print(f"⚠️ Webhook durumu kontrol edilemedi: {e}")
    
    # Yeni webhook kur
    railway_url = RAILWAY_STATIC_URL or RAILWAY_PUBLIC_DOMAIN
    
    if railway_url:
        new_webhook_url = f"https://{railway_url}/{BOT_TOKEN}"
        print(f"🔗 Yeni webhook kuruluyor: {new_webhook_url}")
        
        try:
            set_response = requests.post(f"{api_base}/setWebhook", {
                'url': new_webhook_url
            })
            
            result = set_response.json()
            if result.get('ok'):
                print("✅ Yeni webhook başarıyla kuruldu!")
                return True
            else:
                print(f"❌ Webhook kurulurken hata: {result.get('description', 'Bilinmeyen hata')}")
                return False
                
        except Exception as e:
            print(f"❌ Webhook kurulum hatası: {e}")
            return False
    else:
        print("⚠️ Railway URL bulunamadı - webhook kurulamıyor")
        return False

if __name__ == '__main__':
    print("🚀 Telegram Webhook Yöneticisi")
    print("=" * 40)
    
    success = clear_and_set_webhook()
    
    print("=" * 40)
    if success:
        print("🎉 Webhook işlemleri tamamlandı!")
    else:
        print("❌ Webhook işlemlerinde sorun oluştu!")