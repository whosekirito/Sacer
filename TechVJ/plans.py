
# Don't Remove Credit Tg - @Whosekirito
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @Whosekirito

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from database.db import db
from config import ADMINS
import datetime

# Plans configuration
PLANS = {
    "basic": {
        "name": "🌟 Basic Plan",
        "price": "$2.99",
        "duration": 30,
        "features": [
            "✅ 200 Downloads per day",
            "✅ Basic Support",
            "✅ All Media Types",
            "✅ Fast Downloads",
            "✅ Quality Selection (720p/1080p)",
            "✅ Download History"
        ]
    },
    "premium": {
        "name": "💎 Premium Plan", 
        "price": "$5.99",
        "duration": 30,
        "features": [
            "✅ Unlimited Downloads",
            "✅ Priority Support 24/7",
            "✅ Batch Downloads (Up to 100 files)",
            "✅ Ultra Fast Speed (10x faster)",
            "✅ No Ads",
            "✅ Auto-Organize Downloads",
            "✅ Custom File Names",
            "✅ Direct Cloud Storage Upload"
        ]
    },
    "pro": {
        "name": "⚡ Pro Plan",
        "price": "$8.99",
        "duration": 30,
        "features": [
            "✅ Everything in Premium",
            "✅ API Access",
            "✅ Batch Downloads (Up to 500 files)",
            "✅ Custom Watermarks",
            "✅ Advanced Statistics",
            "✅ Multi-Account Support",
            "✅ Scheduler Downloads",
            "✅ Premium Quality (4K/8K)"
        ]
    },
    "lifetime": {
        "name": "🚀 Lifetime Plan",
        "price": "$15.99", 
        "duration": 36500,  # 100 years
        "features": [
            "✅ All Pro Features Forever",
            "✅ VIP Support (1-on-1)",
            "✅ Unlimited Everything",
            "✅ Future Updates Free",
            "✅ Priority Processing",
            "✅ White-label Option",
            "✅ Custom Bot Features",
            "✅ Reseller Rights"
        ]
    }
}

@Client.on_callback_query(filters.regex("show_plans"))
async def show_plans(client: Client, callback_query: CallbackQuery):
    buttons = []
    for plan_id, plan in PLANS.items():
        buttons.append([InlineKeyboardButton(f"{plan['name']} - {plan['price']}", callback_data=f"plan_{plan_id}")])
    
    buttons.append([InlineKeyboardButton("🔙 Back to Main", callback_data="back_to_main")])
    reply_markup = InlineKeyboardMarkup(buttons)
    
    plans_text = """<b>💎 Choose Your Plan

🎯 Select the perfect plan for your needs:</b>

<b>🌟 Basic Plan - $2.99/month</b>
• 200 Downloads per day
• Quality Selection (720p/1080p)
• Download History

<b>💎 Premium Plan - $5.99/month</b>
• Unlimited Downloads
• Priority Support 24/7
• Batch Downloads (100 files)

<b>⚡ Pro Plan - $8.99/month</b>
• API Access & Scheduler
• Batch Downloads (500 files)  
• 4K/8K Premium Quality

<b>🚀 Lifetime Plan - $15.99 (One-time)</b>
• All Pro Features Forever
• VIP Support & Reseller Rights
• Custom Bot Features

<i>📞 Contact @Whosekirito to purchase any plan</i>"""
    
    await callback_query.edit_message_caption(
        caption=plans_text,
        reply_markup=reply_markup
    )

@Client.on_callback_query(filters.regex("plan_"))
async def plan_details(client: Client, callback_query: CallbackQuery):
    plan_id = callback_query.data.split("_")[1]
    plan = PLANS.get(plan_id)
    
    if not plan:
        await callback_query.answer("Plan not found!", show_alert=True)
        return
    
    features_text = "\n".join(plan["features"])
    duration_text = "30 days" if plan["duration"] == 30 else "Lifetime" if plan["duration"] == 36500 else f"{plan['duration']} days"
    
    plan_text = f"""<b>{plan['name']}
💰 Price: {plan['price']}
⏰ Duration: {duration_text}

🎯 Features:
{features_text}

📞 To purchase this plan, contact the admin with your user ID:
👤 Your ID: <code>{callback_query.from_user.id}</code></b>"""
    
    buttons = [
        [InlineKeyboardButton("💰 Buy Now", url="https://t.me/whosekirito")],
        [InlineKeyboardButton("🔙 Back to Plans", callback_data="show_plans")]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await callback_query.edit_message_caption(
        caption=plan_text,
        reply_markup=reply_markup
    )

@Client.on_callback_query(filters.regex("my_status"))
async def my_status(client: Client, callback_query: CallbackQuery):
    user_data = await db.get_user_subscription(callback_query.from_user.id)
    
    if user_data and user_data.get('is_premium'):
        expiry = user_data.get('expiry_date', 'Never')
        plan_name = user_data.get('plan_name', 'Premium')
        status_text = f"""<b>🎉 Premium User Status

👤 User: {callback_query.from_user.mention}
💎 Plan: {plan_name}
📅 Expires: {expiry}
✅ Status: Active

🎯 Premium Benefits:
• Unlimited Downloads
• Priority Support
• High Speed Processing
• No Advertisements</b>"""
    else:
        status_text = f"""<b>📊 User Status

👤 User: {callback_query.from_user.mention}
🔒 Plan: Free User
📅 Downloads Today: Limited
❌ Status: Basic

🎯 Upgrade to Premium for:
• Unlimited Downloads
• Priority Support  
• High Speed Processing
• Remove All Limits</b>"""
    
    buttons = [
        [InlineKeyboardButton("💎 Upgrade Now", callback_data="show_plans")],
        [InlineKeyboardButton("🔙 Back to Main", callback_data="back_to_main")]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await callback_query.edit_message_caption(
        caption=status_text,
        reply_markup=reply_markup
    )

@Client.on_callback_query(filters.regex("back_to_main"))
async def back_to_main(client: Client, callback_query: CallbackQuery):
    user_data = await db.get_user_subscription(callback_query.from_user.id)
    subscription_status = "🔓 Premium User" if user_data and user_data.get('is_premium') else "🔒 Free User"
    
    buttons = [[
        InlineKeyboardButton("💎 View Plans", callback_data="show_plans"),
        InlineKeyboardButton("📊 My Status", callback_data="my_status")
    ],[
        InlineKeyboardButton("❣️ Developer", url = "https://t.me/whosekirito")
    ],[
        InlineKeyboardButton('🔍 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/AACBotSupport'),
        InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/kirito_bots')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    start_text = f"""<b>🌟 Welcome {callback_query.from_user.mention}! 

🤖 I'm your Premium Save Restricted Content Bot
✨ Download any restricted content with ease!

📊 Your Status: {subscription_status}

🚀 Features:
• Download from Private Channels
• Support for All Media Types
• Batch Download Support
• High Speed Downloads
• 24/7 Availability

💡 Get started: /login to authenticate
📚 Need help? Use /help command

🎯 Upgrade to Premium for unlimited downloads!</b>"""
    
    await callback_query.edit_message_caption(
        caption=start_text,
        reply_markup=reply_markup
    )

# Give subscription command (Admin only)
@Client.on_message(filters.command(["givsub"]) & filters.user(ADMINS))
async def give_subscription(client: Client, message: Message):
    try:
        # Command format: /givsub user_id plan_name days
        # Example: /givsub 123456789 premium 30
        
        if len(message.command) < 4:
            await message.reply("""<b>❌ Invalid format!

📝 Usage: /givsub [user_id] [plan] [days]

📋 Available plans:
• basic
• premium
• pro
• lifetime

💡 Example: /givsub 123456789 premium 30</b>""")
            return
        
        user_id = int(message.command[1])
        plan_name = message.command[2].lower()
        days = int(message.command[3])
        
        if plan_name not in PLANS:
            await message.reply("❌ Invalid plan! Available: basic, premium, pro, lifetime")
            return
        
        # Calculate expiry date
        expiry_date = datetime.datetime.now() + datetime.timedelta(days=days)
        expiry_str = expiry_date.strftime("%d-%m-%Y") if days < 36500 else "Never"
        
        # Save subscription to database
        await db.set_user_subscription(user_id, {
            'is_premium': True,
            'plan_name': PLANS[plan_name]['name'],
            'expiry_date': expiry_str,
            'granted_by': message.from_user.id,
            'granted_on': datetime.datetime.now().strftime("%d-%m-%Y")
        })
        
        # Notify admin
        await message.reply(f"""<b>✅ Subscription Granted Successfully!

👤 User ID: <code>{user_id}</code>
💎 Plan: {PLANS[plan_name]['name']}
📅 Duration: {days} days
⏰ Expires: {expiry_str}

📨 User has been notified about the subscription.</b>""")
        
        # Notify user
        try:
            await client.send_message(
                user_id,
                f"""<b>🎉 Congratulations! 

💎 You have been granted {PLANS[plan_name]['name']}!
📅 Valid until: {expiry_str}
🎯 Enjoy unlimited downloads!

✨ Thank you for using our service!</b>"""
            )
        except:
            await message.reply("⚠️ Subscription granted but couldn't notify user (they haven't started the bot)")
            
    except ValueError:
        await message.reply("❌ Invalid user ID or days! Please use numbers only.")
    except Exception as e:
        await message.reply(f"❌ Error: {str(e)}")

# Check subscription command
@Client.on_message(filters.command(["mysub"]))
async def check_subscription(client: Client, message: Message):
    user_data = await db.get_user_subscription(message.from_user.id)
    
    if user_data and user_data.get('is_premium'):
        await message.reply(f"""<b>🎉 Your Subscription Status

💎 Plan: {user_data.get('plan_name', 'Premium')}
📅 Expires: {user_data.get('expiry_date', 'Never')}
✅ Status: Active

🎯 Enjoy unlimited downloads!</b>""")
    else:
        await message.reply("""<b>📊 Your Subscription Status

🔒 Plan: Free User
❌ Status: No active subscription

💎 Upgrade to Premium:
• Unlimited Downloads
• Priority Support
• High Speed Processing

Use /start to view available plans!</b>""")
