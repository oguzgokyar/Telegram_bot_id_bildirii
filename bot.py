import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Logging yapılandırması
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token'ını environment variable'dan al
BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    print("❌ HATA: BOT_TOKEN environment variable'ı bulunamadı!")
    print("🔧 Çözüm:")
    print("1. Railway dashboard'da Variables sekmesine gidin")
    print("2. BOT_TOKEN adında yeni bir variable ekleyin")
    print("3. Değer olarak BotFather'dan aldığınız token'ı girin")
    print("4. Deploy'u yeniden başlatın")
    print("\n📋 Mevcut environment variables:")
    for key, value in os.environ.items():
        if 'TOKEN' in key.upper() or 'BOT' in key.upper() or 'RAILWAY' in key.upper():
            print(f"   {key} = {'*' * len(value) if value else 'BOŞ'}")
    raise ValueError("BOT_TOKEN environment variable'ı ayarlanmamış!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Bot başlatıldığında çalışır ve kullanıcıya chat ID'sini gönderir."""
    user = update.effective_user
    chat = update.effective_chat
    
    # Chat ID bilgisini hazırla
    message = f"""
🤖 *HaberinOlsunRSS Bot*

Merhaba {user.first_name}! 

📋 **Chat Bilgileriniz:**
• Chat ID: `{chat.id}`
• User ID: `{user.id}`
• Kullanıcı Adı: @{user.username if user.username else 'Kullanıcı adı yok'}

💡 **Chat ID'nizi kopyalamak için:**
Yukarıdaki Chat ID'nin üzerine tıklayın ve kopyalayın.

🔧 **Bu bot ne işe yarar?**
Bu bot size chat ID bilginizi gösterir. Bu ID'yi başka uygulamalarda Telegram entegrasyonları için kullanabilirsiniz.

📞 **Destek:** @HaberinOlsunRSS_bot
    """
    
    await update.message.reply_text(
        message, 
        parse_mode='Markdown'
    )
    
    # Log bilgisi
    logger.info(f"Start komutu kullanıldı - User: {user.id}, Chat: {chat.id}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Yardım komutunu işler."""
    help_text = """
🤖 *HaberinOlsunRSS Bot Yardım*

**Kullanılabilir Komutlar:**
• `/start` - Bot hakkında bilgi al ve Chat ID'ni öğren
• `/help` - Bu yardım mesajını göster
• `/chatid` - Sadece Chat ID'ni göster

**Chat ID Nedir?**
Chat ID, Telegram'da her sohbetin benzersiz numarasıdır. Bu numarayı kullanarak bot'lar size mesaj gönderebilir.

**Kullanım Alanları:**
• RSS bot'ları için
• Bildirim sistemleri için
• Telegram API entegrasyonları için

📞 **Destek:** @HaberinOlsunRSS_bot
    """
    
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def chatid_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sadece chat ID'yi gönderir."""
    chat = update.effective_chat
    
    await update.message.reply_text(
        f"💬 **Chat ID:** `{chat.id}`\n\n💡 Kopyalamak için ID'nin üzerine tıklayın.",
        parse_mode='Markdown'
    )

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Hataları loglar."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

def main() -> None:
    """Bot'u başlatır."""
    # Application oluştur
    application = Application.builder().token(BOT_TOKEN).build()

    # Komut handler'larını ekle
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("chatid", chatid_command))
    
    # Hata handler'ını ekle
    application.add_error_handler(error_handler)

    # Bot'u başlat
    logger.info("Bot başlatılıyor...")
    
    # Railway için webhook modunda çalıştır
    PORT = int(os.environ.get('PORT', 8443))
    RAILWAY_STATIC_URL = os.environ.get('RAILWAY_STATIC_URL')
    
    if RAILWAY_STATIC_URL:
        # Production modunda webhook kullan
        webhook_url = f"https://{RAILWAY_STATIC_URL}"
        logger.info(f"Webhook modunda başlatılıyor: {webhook_url}")
        application.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=BOT_TOKEN,
            webhook_url=f"{webhook_url}/{BOT_TOKEN}"
        )
    else:
        # Development modunda polling kullan
        logger.info("Polling modunda başlatılıyor...")
        application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()