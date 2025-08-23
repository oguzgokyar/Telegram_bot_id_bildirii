#!/usr/bin/env python3
"""
Railway environment variables debug scripti
Bu script environment variables'ların doğru yüklenip yüklenmediğini kontrol eder
"""

import os
import sys

print("🔍 Railway Environment Variables Debug")
print("=" * 50)

# BOT_TOKEN kontrol et
bot_token = os.getenv('BOT_TOKEN')
print(f"BOT_TOKEN: {'✅ Ayarlanmış' if bot_token else '❌ Ayarlanmamış'}")
if bot_token:
    print(f"BOT_TOKEN uzunluğu: {len(bot_token)} karakter")
    print(f"BOT_TOKEN önizleme: {bot_token[:10]}...{bot_token[-5:] if len(bot_token) > 15 else bot_token}")

# Railway değişkenleri
railway_vars = ['RAILWAY_STATIC_URL', 'RAILWAY_PUBLIC_DOMAIN', 'PORT']
print("\n🚂 Railway Variables:")
for var in railway_vars:
    value = os.getenv(var)
    print(f"{var}: {value if value else '❌ Yok'}")

# Tüm environment variables (güvenlik için filtrelenmiş)
print(f"\n📋 Toplam Environment Variables: {len(os.environ)}")
print("\n🔑 Bot ile ilgili variables:")
for key, value in sorted(os.environ.items()):
    if any(keyword in key.upper() for keyword in ['TOKEN', 'BOT', 'RAILWAY', 'PORT', 'URL']):
        if 'TOKEN' in key.upper():
            display_value = f"{value[:5]}...{value[-3:]}" if value and len(value) > 8 else "GIZLI"
        else:
            display_value = value
        print(f"   {key} = {display_value}")

# Python version
print(f"\n🐍 Python Version: {sys.version}")
print(f"📁 Working Directory: {os.getcwd()}")

print("\n" + "=" * 50)
print("✅ Debug tamamlandı!")