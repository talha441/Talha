from pyrogram import Client, filters

# ✅ API তথ্য সঠিকভাবে ফরম্যাট করা
api_id = 24071389  # ইন্টিজার (কোটেশন ছাড়া)
api_hash = "17ad740bc29b835d5e89387305f0e9d8"  # স্ট্রিং (কোটেশন সহ)
bot_token = "7685876820:AAHiEb1CCbcC3KwOUw6yRVLc_5YyTDaR8ts"  # স্ট্রিং (কোটেশন সহ)

# ✅ বট সেটআপ
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# ✅ স্টার্ট কমান্ড
@app.on_message(filters.command("start") & filters.private)
def start(client, message):
    message.reply_text("👋 হ্যালো! আমি তোমার গ্রুপ ম্যানেজমেন্ট বট।")

# ✅ নতুন ইউজার জয়েন হলে ওয়েলকাম মেসেজ পাঠানো
@app.on_message(filters.new_chat_members)
def welcome(client, message):
    for user in message.new_chat_members:
        message.reply_text(f"🎉 স্বাগতম, {user.mention}!")

# ✅ স্প্যাম ফিল্টার
@app.on_message(filters.group & filters.text)
def filter_spam(client, message):
    banned_words = ["spam", "scam", "fake"]
    for word in banned_words:
        if word in message.text.lower():
            message.delete()
            message.reply_text("⚠️ স্প্যাম ডিটেক্টেড! মেসেজ মুছে ফেলা হলো।")
            break

# ✅ বট চালু করা
app.run()
