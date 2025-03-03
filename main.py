import interactions
import os 
import platform
import random
import requests
from interactions import *

# $$$$$$$\   $$$$$$\ $$$$$$$$\        $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$\        $$\    $$\   $$\   
# $$  __$$\ $$  __$$\\__$$  __|      $$  __$$\ $$ |  $$ |$$  __$$\ $$  __$$\       $$ |   $$ |$$$$ |  
# $$ |  $$ |$$ /  $$ |  $$ |         $$ /  \__|$$ |  $$ |$$ /  $$ |$$ |  $$ |      $$ |   $$ |\_$$ |  
# $$$$$$$\ |$$ |  $$ |  $$ |         \$$$$$$\  $$$$$$$$ |$$ |  $$ |$$$$$$$  |      \$$\  $$  |  $$ |  
# $$  __$$\ $$ |  $$ |  $$ |          \____$$\ $$  __$$ |$$ |  $$ |$$  ____/        \$$\$$  /   $$ |  
# $$ |  $$ |$$ |  $$ |  $$ |         $$\   $$ |$$ |  $$ |$$ |  $$ |$$ |              \$$$  /    $$ |  
# $$$$$$$  | $$$$$$  |  $$ |         \$$$$$$  |$$ |  $$ | $$$$$$  |$$ |               \$  /   $$$$$$\ 
# \_______/  \______/   \__|          \______/ \__|  \__| \______/ \__|                \_/    \______|
                                                                                                    
                                                                                                    
                                                                                                    

                                         # 𝐂𝐨𝐧𝐟𝐢𝐠 
token = "MTM0NjA3Nzc1ODIwMzM2MzM2OA.GFh_mi.XBAe9eSt97_-apuBdS6ZhT34PBr0mguKhpPVkY"         #Token Bot
Flexzy = interactions.Client(token=token, intents=Intents.ALL)
planel_channel = "1346078030291931211"        # Planel Chanel
phone = "0993739602"         # Phone Number
log_channel = "1346078852555866143"        # Log Channel

                                        # 𝐇𝐞𝐚𝐝𝐞𝐫𝐬
title = "- ,, WELCOME TO FLEXZY TOPUP ꒰"
tn = "https://media.discordapp.net/attachments/1105860649294237846/1119320900341350501/Profile.png?width=468&height=468"  # Small Image
img = "https://www.truemoney.com/wp-content/uploads/2020/11/truemoneywallet_sendgift_CNY_HongPao2020_reward-1.png" # Big Image

                                        # 𝐑𝐨𝐥𝐞 𝐂𝐨𝐧𝐟𝐢𝐠
role_01 = "1346078189050658830"                   #ID role
role01_name = "test"               # ID name
role_01p = "0.00"              # ID Price

role_02 = "test2"                   #ID role
role02_name = "1346078923103928451"              # ID name
role_02p = "0.00"             # ID Price

role_03 = ""                    #ID role
role03_name = ""               # ID name
role_03p = "30.00"              # ID Price

role_04 = ""                   #ID role
role04_name = ""               # ID name
role_04p = "40.00"              # ID Price

role_05 = ""                     #ID role
role05_name = ""               # ID name
role_05p = "50.00"              # ID Price

role_06 = ""                  #ID role
role06_name = ""               # ID name
role_06p = "60.00"              # ID Price

@interactions.listen()
async def on_ready():

                                          # 𝐃𝐞𝐭𝐚𝐢𝐥𝐬
    ch = await Flexzy.fetch_channel(channel_id=planel_channel)
    main_embed = interactions.Embed(title=f"**{title} เติมเงินรับยศ Angpao Topup🧧**", description="_ _", color=0x00FF00)
    main_embed.add_field(name="╭━━━━━━━━━★", value="\nยินดีต้อนรับสู่ Flexzy Store\n💸・กดปุ่ม __เติมเงินซื้อยศ__ เพื่อซื้อยศ\n🌐・กดปุ่ม __ราคายศ__ เพื่อดูราคายศ\n╰━━━━━━━━━★")
    main_embed.set_thumbnail(tn) 
    main_embed.set_image(img)
    main_embed.set_footer("")

    topup = Button(
        style=ButtonStyle.GREEN,
        custom_id="topup_cb",
        label="💸 เติมเงินซื้อยศ",
    )
    
    all = Button(
        style=ButtonStyle.BLUE,
        custom_id="all_cb",
        label="🌐 ราคายศทั้งหมด",
    )

    await ch.send(embeds=main_embed, components=[topup, all])


    if platform.system() == 'Windows':

        os.system(f'cls & title {title} [ Working....]')
        print(" ")
        print(f"{title} [ Working.... ]")
        print(" ")
    
    else:

        os.system("clear")
        print(" ")
        print(f"{title} [ Working.... ]")
        print(" ")

@interactions.listen()
async def on_component(event: BaseComponent):

    ctx = event.ctx

    match ctx.custom_id:
        case "topup_cb":
            select_plan = StringSelectMenu(
                [
                    interactions.StringSelectOption(label="เติมเงิน", emoji="🧧", value="test"),
                ],
                placeholder="🟢 เติมเงินตามจำนวนราคายศ",
                min_values=1,
                max_values=1,
            )

            await ctx.send(components=select_plan, ephemeral=True)
            def check(component: Button) -> bool:
                return component.ctx.author.id == ctx.author.id

            try:

                used_component = await Flexzy.wait_for_component(components=select_plan, check=check, timeout=30)
                used_ctx = used_component.ctx
                rolebuy = used_ctx.values[0]
                topup_modal = Modal(
                    ShortText(
                    label="Wallet angpao Topup services",
                    custom_id="giftLink",
                    required=True,
                    placeholder="กรุณาใส่ลิ้งค์ซอง เช่น https://gift.truemoney.com/campaign/?v=XXXXXXXXXXXXXXX!",
                    max_length=80,
                    ),
                    title="🧧 เติมเงินตามจำนวนราคายศ!",
                )
                await used_ctx.send_modal(modal=topup_modal)
                modal_ctx: ModalContext = await used_ctx.bot.wait_for_modal(topup_modal)
                giftLink = modal_ctx.responses['giftLink']
                auth = requests.get(f"https://zamex-hub.000webhostapp.com/index.php?phone={phone}&link={giftLink}")
                flexzy = auth.json()

                if flexzy["status"] == "SUCCESS":

                    if flexzy["amount"] == role_01p:

                        role_01s = interactions.Embed(title=f"**{title} Success ( 1 )**", description="_ _", color=0x92f0a3)
                        role_01s.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ\n_ _\n")
                        role_01s.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`🎗️`: <@&{role_01}>\n_ _\n")
                        role_01s.add_field(name="> จำนวนเงิน", value=f"_ _\n`💸`: <@{role_01p}>\n_ _\n")
                        await ctx.send(embeds=role_01s, ephemeral=True)
                        log_01 = await Flexzy.fetch_channel(channel_id=log_channel)
                        log_01eb = interactions.Embed(title=f"**{title} Log**", description="_ _", color=0x75ffb1)
                        log_01eb.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ !\n_ _\n_ _")
                        log_01eb.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`❓`: <@&{role_01}>\n_ _\n_ _")
                        await log_01.send(f"<@{ctx.author.id}>", embeds=log_01eb)

                    elif flexzy["amount"] == role_02p:

                        role_02s = interactions.Embed(title=f"**{title} Success ( 2 )**", description="_ _", color=0x92f0a3)
                        role_02s.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ\n_ _\n")
                        role_02s.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`🎗️`: <@&{role_02}>\n_ _\n")
                        role_02s.add_field(name="> จำนวนเงิน", value=f"_ _\n`💸`: <@_{role_02p}>\n_ _\n")
                        await ctx.send(embeds=role_02s, ephemeral=True)
                        log_02 = await Flexzy.fetch_channel(channel_id=log_channel)
                        log_02eb = interactions.Embed(title=f"**{title} Log**", description="_ _", color=0x75ffb1)
                        log_02eb.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ !\n_ _\n_ _")
                        log_02eb.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`❓`: <@&{role_02}>\n_ _\n_ _")
                        await log_02.send(f"<@{ctx.author.id}>", embeds=log_02eb)

                    elif flexzy["amount"] == role_03p:

                        role_03s = interactions.Embed(title=f"**{title} Success ( 3 )**", description="_ _", color=0x92f0a3)
                        role_03s.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ\n_ _\n")
                        role_03s.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`🎗️`: <@&{role_03}>\n_ _\n")
                        role_03s.add_field(name="> จำนวนเงิน", value=f"_ _\n`💸`: <@{role_03p}>\n_ _\n")
                        await ctx.send(embeds=role_03s, ephemeral=True)
                        log_03 = await Flexzy.fetch_channel(channel_id=log_channel)
                        log_03eb = interactions.Embed(title=f"**{title} Log**", description="_ _", color=0x75ffb1)
                        log_03eb.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ !\n_ _\n_ _")
                        log_03eb.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`❓`: <@&{role_03}>\n_ _\n_ _")
                        await log_03.send(f"<@{ctx.author.id}>", embeds=log_03eb)

                    elif flexzy["amount"] == role_04p:

                        role_04s = interactions.Embed(title=f"**{title} Success ( 4 )**", description="_ _", color=0x92f0a3)
                        role_04s.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ\n_ _\n")
                        role_04s.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`🎗️`: <@&{role_04}>\n_ _\n")
                        role_04s.add_field(name="> จำนวนเงิน", value=f"_ _\n`💸`: <&{role_04p}>\n_ _\n")
                        await ctx.send(embeds=role_04s, ephemeral=True)
                        log_04 = await Flexzy.fetch_channel(channel_id=log_channel)
                        log_04eb = interactions.Embed(title=f"**{title} Log**", description="_ _", color=0x75ffb1)
                        log_04eb.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ !\n_ _\n_ _")
                        log_04eb.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`❓`: <@&{role_04}>\n_ _\n_ _")
                        await log_04.send(f"<@{ctx.author.id}>", embeds=log_04eb)

                    elif flexzy["amount"] == role_05p:

                        role_05s = interactions.Embed(title=f"**{title} Success ( 5 )**", description="_ _", color=0x92f0a3)
                        role_05s.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ\n_ _\n")
                        role_05s.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`🎗️`: <@&{role_05}>\n_ _\n")
                        role_05s.add_field(name="> จำนวนเงิน", value=f"_ _\n`💸`: <@{role_05p}>\n_ _\n")
                        await ctx.send(embeds=role_05s, ephemeral=True)
                        log_05 = await Flexzy.fetch_channel(channel_id=log_channel)
                        log_05eb = interactions.Embed(title=f"**{title} Log**", description="_ _", color=0x75ffb1)
                        log_05eb.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ !\n_ _\n_ _")
                        log_05eb.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`❓`: <@&{role_05}>\n_ _\n_ _")
                        await log_05.send(f"<@{ctx.author.id}>", embeds=log_05eb)

                    elif flexzy["amount"] == role_06p:

                        role_06s = interactions.Embed(title=f"**{title} Success ( 6 )**", description="_ _", color=0x92f0a3)
                        role_06s.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ\n_ _\n")
                        role_06s.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`🎗️`: <@&{role_06}>\n_ _\n")
                        role_06s.add_field(name="> จำนวนเงิน", value=f"_ _\n`💸`: <@{role_06p}>\n_ _\n")
                        await ctx.send(embeds=role_06s, ephemeral=True)
                        log_06 = await Flexzy.fetch_channel(channel_id=log_channel)
                        log_06eb = interactions.Embed(title=f"**{title} Log**", description="_ _", color=0x75ffb1)
                        log_06eb.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ !\n_ _\n_ _")
                        log_06eb.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`❓`: <@&{role_06}>\n_ _\n_ _")
                        await log_06.send(f"<@{ctx.author.id}>", embeds=log_06eb)

                    else:

                        role_07s = interactions.Embed(title=f"**{title} Success ( 7 )**", description="_ _", color=0xf59300)
                        role_07s.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ\n_ _\n")
                        role_07s.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`🎗️`: ไม่พบยศ !\n_ _\n")
                        role_07s.add_field(name="> จำนวนเงิน", value=f"_ _\n`💸`: ไม่สามารถดึงค่าได้ !\n_ _\n")
                        await ctx.send(embeds=role_07s, ephemeral=True)
                        log_07 = await Flexzy.fetch_channel(channel_id=log_channel)
                        log_07eb = interactions.Embed(title=f"**{title} Log**", description="_ _", color=0x75ffb1)
                        log_07eb.add_field(name="> สถานะ", value="_ _\n`❗`: เติมเงินเกินกว่าที่ระบบตั้งไว้ !\n_ _\n_ _")
                        await log_07.send(f"<@{ctx.author.id}>", embeds=log_07eb)

                else:

                    print("Fail")
                    fail = interactions.Embed(title=f"**{title} Fail**", description="_ _", color=0xf50049)
                    fail.add_field(name="> สถานะ", value="_ _\n`❌`: เติมเงินไม่สำเร็จ\n_ _\n")
                    await ctx.send(embeds=fail, ephemeral=True)
                    fail_x = await Flexzy.fetch_channel(channel_id=log_channel)
                    faileb = interactions.Embed(title=f"**{title} Log**", description="_ _", color=0xff004c)
                    faileb.add_field(name="> สถานะ", value="_ _\n`❌`: เติมเงินไม่สำเร็จ\n_ _\n_ _")
                    await fail_x.send(f"<@{ctx.author.id}>", embeds=faileb)
                        
            except TimeoutError:

                print("หมดเวลา")

        case "all_cb":

            role_all = interactions.Embed(title=f"**{title} Role**", description="_ _", color=0x21E9FC)
            role_all.set_thumbnail ("https://media.discordapp.net/attachments/1105860649294237846/1119320900341350501/Profile.png?width=468&height=468")  # Small Image
            role_all.set_image ("https://media.discordapp.net/attachments/1105860649294237846/1119548367660404796/FLEXZY2_copy.png?width=960&height=221") # Big Image
            role_all.add_field(name=f"・ยศ {role01_name}", value=f"\nยศที่ได้รับ <@&{role_01}>\n✼ •• ┈┈┈┈┈┈┈┈┈┈┈┈ •• ✼\nราคา `💸`: `{role_01p}`\n\n")
            role_all.add_field(name=f"・ยศ {role02_name}", value=f"\nยศที่ได้รับ <@&{role_02}>\n✼ •• ┈┈┈┈┈┈┈┈┈┈┈┈ •• ✼\nราคา `💸`: `{role_02p}`\n\n")
            role_all.add_field(name=f"・ยศ {role03_name}", value=f"\nยศที่ได้รับ <@&{role_03}>\n✼ •• ┈┈┈┈┈┈┈┈┈┈┈┈ •• ✼\nราคา `💸`: `{role_03p}`\n\n")
            role_all.add_field(name=f"・ยศ {role04_name}", value=f"\nยศที่ได้รับ <@&{role_04}>\n✼ •• ┈┈┈┈┈┈┈┈┈┈┈┈ •• ✼\nราคา `💸`: `{role_04p}`\n\n")
            role_all.add_field(name=f"・ยศ {role05_name}", value=f"\nยศที่ได้รับ <@&{role_05}>\n✼ •• ┈┈┈┈┈┈┈┈┈┈┈┈ •• ✼\nราคา `💸`: `{role_05p}`\n\n")
            role_all.add_field(name=f"・ยศ {role06_name}", value=f"\nยศที่ได้รับ <@&{role_06}>\n✼ •• ┈┈┈┈┈┈┈┈┈┈┈┈ •• ✼\nราคา `💸`: `{role_06p}`\n\n")

            role_all.set_footer("Copyright ©  2023 , All right reserved discord.gg/flexzy")

            await ctx.send(embeds=role_all, ephemeral=True)

Flexzy.start(token)

# Copyright ©  2023 , All right reserved discord.gg/flexzy
