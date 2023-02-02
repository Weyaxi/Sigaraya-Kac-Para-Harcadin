import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or("w!", "W!", "w! ", "W! "))
TOKEN = ""

@bot.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def sigarahesapla(ctx):
    pakette_kac_sigara = "20"

    def is_correct(m):
        return m.author == ctx.author and m.content.isdigit()

    await ctx.send('**<a:sigara:854437179501182996> Kaç yıldır sigara kullanıyorsunuz?**')

    try:
        kac_yil = await bot.wait_for('message', check=is_correct, timeout=10.0)
    except asyncio.TimeoutError:
        return await ctx.send(
            f'**<:normalcarpi:852958720328466474> Verilerini belirtmen çok uzun sürdü. Daha sonra tekrar dene.**')

    await ctx.send('**<a:sigara:854437179501182996> Bir günde kaç tane sigara içiyorsunuz?** ')

    try:
        gunde_kac_tane = await bot.wait_for('message', check=is_correct, timeout=10.0)
    except asyncio.TimeoutError:
        return await ctx.send(
            f'**<:normalcarpi:852958720328466474> Verilerini belirtmen çok uzun sürdü. Daha sonra tekrar dene.**')

    await ctx.send(
        '**<a:sigara:854437179501182996> Bir paket sigaraya kaç lira harcıyorsunuz? (Eğer bu değer yıldan yıla farklılık göseriyorsa lütfen ortalama bir değer giriniz)** ')

    try:
        paket_fiyati = await bot.wait_for('message', check=is_correct, timeout=10.0)
    except asyncio.TimeoutError:
        return await ctx.send(
            f'**<:normalcarpi:852958720328466474> Verilerini belirtmen çok uzun sürdü. Daha sonra tekrar dene.**')

    embed = discord.Embed(title="<a:sigara:854437179501182996> Sigara Zarar Hesaplama Komutu",
                          description=f"Girdiğiniz verilere göre, sigaradan ne kadar zarar ettiğiniz size detaylı bir rapor halinde sunulur.",
                          color=62150)
    embed.add_field(name=f"<a:sigara:854437179501182996> Bir Haftada İçtiğiniz Toplam Sigara Sayısı",
                    value=f"{int(gunde_kac_tane.content) * 7} Tane", inline=True)
    embed.add_field(name=f"<a:sigara:854437179501182996> Bir Haftada Sigaraya Harcadığınız Toplam Para",
                    value=f"{int(gunde_kac_tane.content) / 20 * int(paket_fiyati.content) * 7}", inline=True)

    embed.add_field(name=f"<a:sigara:854437179501182996> Bir Ayda İçtiğiniz Toplam Sigara Sayısı",
                    value=f"{int(gunde_kac_tane.content) * 30} Tane", inline=True)
    embed.add_field(name=f"<a:sigara:854437179501182996> Bir Ayda Sigaraya Harcadığınız Toplam Para",
                    value=f"{int(gunde_kac_tane.content) / 20 * int(paket_fiyati.content) * 30} TL", inline=True)

    embed.add_field(name=f"<a:sigara:854437179501182996> Bir Yılda İçtiğiniz Toplam Sigara Sayısı",
                    value=f"{int(gunde_kac_tane.content) * 365} Tane", inline=True)
    embed.add_field(name=f"<a:sigara:854437179501182996> Bir Yılda Sigaraya Harcadığınız Toplam Para",
                    value=f"{int(gunde_kac_tane.content) / 20 * int(paket_fiyati.content) * 365} TL", inline=True)

    embed.add_field(name=f"<a:sigara:854437179501182996> {kac_yil.content} Yılda İçtiğiniz Toplam Sigara Sayısı",
                    value=f"{int(gunde_kac_tane.content) * int(kac_yil.content) * 365} Tane", inline=False)
    embed.add_field(name=f"<a:sigara:854437179501182996> {kac_yil.content} Yılda Sigaraya Harcadığınız Toplam Para",
                    value=f"{int(gunde_kac_tane.content) / 20 * int(paket_fiyati.content) * int(kac_yil.content) * 365} TL",
                    inline=True)

    await ctx.send(embed=embed)


@sigarahesapla.error
async def sigarahesapla_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            f'<:saat:867471142800457748> **Bu komutu kullanabilmek için {round(error.retry_after, 2)} saniye daha beklmelisin.**')

bot.run(TOKEN)