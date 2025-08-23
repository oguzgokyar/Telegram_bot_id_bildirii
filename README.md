# 🤖 Telegram Chat ID Bot

Bu bot, kullanıcıların Telegram chat ID'lerini öğrenmelerine yardımcı olan basit bir Telegram bot'udur. Bot, `/start` komutu ile başlatıldığında kullanıcıya chat ID bilgisini gönderir.

## 🚀 Özellikler

- Chat ID ve User ID bilgilerini gösterir
- Kullanıcı dostu arayüz
- Railway'de kolay deployment
- Webhook ve polling modları

## 📋 Komutlar

- `/start` - Bot hakkında bilgi al ve Chat ID'ni öğren
- `/help` - Yardım mesajını göster
- `/chatid` - Sadece Chat ID'ni göster

## 🛠️ Kurulum

### 1. Telegram Bot Oluşturma

1. Telegram'da [@BotFather](https://t.me/botfather) bot'una git
2. `/newbot` komutunu kullan
3. Bot adını belirle (örn: "HaberinOlsun Chat ID Bot")
4. Bot kullanıcı adını belirle (örn: "@HaberinOlsunRSS_bot")
5. BotFather'dan aldığın token'ı kaydet

### 2. Local Development

```bash
# Repository'yi clone et
git clone https://github.com/kullanici-adi/telegram-bot-id-bildirii.git
cd telegram-bot-id-bildirii

# Virtual environment oluştur
python -m venv venv

# Virtual environment'ı aktifleştir
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Bağımlılıkları yükle
pip install -r requirements.txt

# Environment variables ayarla
copy .env.example .env
# .env dosyasındaki BOT_TOKEN'ı bot token'ınız ile değiştirin

# Bot'u çalıştır
python bot.py
```

### 3. Railway'de Deployment

#### Railway'e Deploy Et

1. [Railway](https://railway.app/) hesabı oluştur
2. GitHub repository'sini Railway'e bağla
3. Environment Variables ayarla:
   - `BOT_TOKEN`: BotFather'dan aldığın token
4. Deploy et!

#### Environment Variables

Railway'de aşağıdaki environment variable'ları ayarlayın:

| Variable | Açıklama | Örnek |
|----------|----------|-------|
| `BOT_TOKEN` | Telegram bot token'ı | `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz` |
| `RAILWAY_STATIC_URL` | Railway otomatik ayarlar | `your-project.up.railway.app` |
| `PORT` | Railway otomatik ayarlar | `8443` |

## 🔧 Troubleshooting

### "BOT_TOKEN environment variable'ı ayarlanmamış!" Hatası

Bu hata Railway'de BOT_TOKEN environment variable'ının ayarlanmadığını gösterir.

**Çözüm:**
1. Railway dashboard'a gidin
2. Projenizi seçin
3. "Variables" sekmesine tıklayın
4. "New Variable" butonuna tıklayın
5. Aşağıdaki bilgileri girin:
   - **Name:** `BOT_TOKEN`
   - **Value:** BotFather'dan aldığınız token (örn: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)
6. "Add" butonuna tıklayın
7. Railway otomatik olarak yeniden deploy edecektir

### Debug Modu

Eğer sorun devam ederse debug modunu aktif edin:

1. Railway'de "Settings" → "Deploy" bölümünde
2. "Start Command" kısmını `python debug_env.py && python start.py` olarak değiştirin
3. Deploy loglarında detaylı environment variable bilgilerini görebilirsiniz

### Token Doğrulama

BotFather'dan yeni token almak için:
1. [@BotFather](https://t.me/botfather) ile konuşun
2. `/mybots` komutunu gönderin
3. Botunuzu seçin
4. "API Token" → "Revoke current token" → "Yes"
5. Yeni token'ı kopyalayın ve Railway'de güncelleyin

## 🔧 Teknik Detaylar

- **Framework**: python-telegram-bot 20.7
- **Python Version**: 3.11
- **Deployment**: Railway (Webhook mode)
- **Development**: Polling mode

## 📁 Proje Yapısı

```
telegram-bot-id-bildirii/
├── bot.py              # Ana bot kodu
├── requirements.txt    # Python bağımlılıkları
├── Procfile           # Railway deployment config
├── runtime.txt        # Python version
├── .env.example       # Environment variables örneği
├── .gitignore         # Git ignore rules
└── README.md          # Bu dosya
```

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add some amazing feature'`)
4. Branch'i push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 📞 Destek

Sorularınız için [@HaberinOlsunRSS_bot](https://t.me/HaberinOlsunRSS_bot) ile iletişime geçebilirsiniz.

## 🔗 Yararlı Linkler

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [python-telegram-bot Documentation](https://python-telegram-bot.readthedocs.io/)
- [Railway Documentation](https://docs.railway.app/)
- [BotFather](https://t.me/botfather)