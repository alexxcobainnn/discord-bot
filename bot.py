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
    "Admin Sandra - 0821-1707-2500",
    "Admin Irvan - 0852-2233-1721",
    "Admin Ermy - 0822-6640-7499",
    "Admin Aril - 0812-9776-6762",
    "Admin Hakim - 0822-9835-9643",
    "Admin Ruby - 0878-3517-3029",
    "Admin Nadia - 0823-1082-2743",
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

        await interaction.response.send_message(
            f"✅ Request diterima!\n\n"
            f"Silakan hubungi admin berikut:\n📱 {admin}",
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