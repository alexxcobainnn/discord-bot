import discord
from discord.ext import commands
import time


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# =====================
# ANTI SPAM SYSTEM
# =====================

user_requests = {}
COOLDOWN = 300  # detik (300 = 5 menit)

admins = [
    {
        "name": "Sandra",
        "phone": "0821-1707-2500",
        "discord_id": 731083851371118592
    },
    {
        "name": "Tasya",
        "phone": "0881-5236-359",
        "discord_id": 756324366345830451
    },
    {
        "name": "Ermy Ulle",
        "phone": "0822-6640-7499",
        "discord_id": 1494516522973139086
    },
    {
        "name": "Aril",
        "phone": "0812-9776-6762",
        "discord_id": 1494265944229417010
    },
    {
        "name": "Hakim",
        "phone": "0822-9835-9643",
        "discord_id": 1308126117567139880
    },
    {
        "name": "Ruby",
        "phone": "0878-3517-3029",
        "discord_id": 1494265093574103061
    },
    {
        "name": "Nadia",
        "phone": "0823-1082-2743",
        "discord_id": 1497092030298456085
    },
    {
        "name": "Dhisa",
        "phone": "0878-6725-2352",
        "discord_id": None
    },
    {
        "name": "Monic",
        "phone": "0819-9639-2737",
        "discord_id": None
    },
    {
        "name": "Nisa",
        "phone": "0895-3841-70908",
        "discord_id": 1497063750908252234
    },
    {
        "name": "Nathalie",
        "phone": "0823-3424-4616",
        "discord_id": 1393896058987352145
    },
    {
        "name": "Inka",
        "phone": "0823-1904-8616",
        "discord_id": 1497065966364917801
    },
    {
        "name": "Alcerio",
        "phone": "0821-1604-7806",
        "discord_id": None
    }


]
current_admin = 0

def get_next_admin():
    global current_admin
    admin = admins[current_admin]

    current_admin += 1
    if current_admin >= len(admins):
        current_admin = 0

    return admin
class JoinView(discord.ui.View):

    @discord.ui.button(label="🚀 Hubungi Customer Service", style=discord.ButtonStyle.green)
    async def join(self, interaction: discord.Interaction, button: discord.ui.Button):

        user_id = interaction.user.id
        now = time.time()

        # CEK apakah user sudah request
        if user_id in user_requests:

            last_time = user_requests[user_id]
            remaining = int(COOLDOWN - (now - last_time))

            if remaining > 0:
                await interaction.response.send_message(
                    f"⛔ Kamu sudah melakukan request.\n"
                    f"Silakan tunggu {remaining} detik sebelum request lagi.",
                    ephemeral=True
                )
                return

        # SIMPAN waktu request
        user_requests[user_id] = now

        admin = get_next_admin()

    # cek discord ada atau tidak

    if admin["discord_id"] and admin["discord_id"] != "-":
           discord_contact = f"<@{admin['discord_id']}>"

    else:
            discord_contact = "-"

        await interaction.response.send_message(
           f"✅ Request diterima!\n\n"
          f"👤 Admin: {admin['name']}\n"
           f"📱 WhatsApp: {admin['phone']}\n"
           f"💬 Discord: <@{admin['discord_id']}>",
           ephemeral=True
        )

@bot.event
async def on_ready():
    print(f"Bot online sebagai {bot.user}")

@bot.command()
async def panel(ctx):
    embed = discord.Embed(
        title="Bergabung Menjadi Member Traxindo Disini!",
        description="Klik tombol untuk bergabung"
    )
    await ctx.send(embed=embed, view=JoinView())

import os

bot.run(os.getenv("TOKEN"))