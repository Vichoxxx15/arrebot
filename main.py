import discord
import discord.utils
from discord.ext import commands
import random



TOKEN = 'NjY5NzczNDczMTY5NTM5MDg0.Xiku3w.LXoQAtWCEERb7nJASz4ebavlk5o'


bot = commands.Bot(command_prefix = 'Arr ')


@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game(name='Sea chanties'))
    print('ready1')

    

@bot.command(pass_context = True)
async def octavobasico(ctx):
    await ctx.send('noveno piso')

@bot.command(pass_context = True)
async def clase(ctx):
    await ctx.send('https://www.youtube.com/watch?v=KcTJk4-z17s')

@bot.command(pass_context = True)
async def jurgol(ctx):
    await ctx.send('https://www.flickr.com/photos/institutanos/1366678386')

@bot.command(pass_context = True)
async def die(ctx):
    await ctx.send('https://imgur.com/r/cursedimages/NBVBYw3')
    
@bot.command(pass_context = True)
async def penis(ctx):
	await ctx.send('DEGENEREKE')
	await ctx.send('https://commons.wikimedia.org/wiki/File:Efecto_Yingo_(2944971475).jpg')

@bot.command(pass_context = True)
async def rule34(ctx):
    await ctx.send('Compare usted me esta vacilando')
    
@bot.command(pass_context = True)
async def ruleta(ctx):
    ran = (random.randrange(1000))
    if  0 < ran and ran < 40 :
        await ctx.send('https://imgur.com/gallery/MrLZlGR')
    if 40 < ran and ran < 80:
        await ctx.send('https://imgur.com/gallery/bRLDJ/comment/552290957')
    if 80 < ran and ran < 120:
        await ctx.send('https://imgur.com/r/blessedimages/oNVlgaI')
    if 120 < ran and ran < 130:
        await ctx.send('https://imgur.com/25uj4lo')
    if 130 < ran and ran < 140:
        await ctx.send('https://rule34.paheal.net/post/view/2649860#search=Barack_Obama')
    if 140 < ran and ran < 180:
        await ctx.send('https://imgur.com/r/eyebleach/37f2jxm')
    if 180 < ran and ran < 220:
        await ctx.send('https://imgur.com/r/eyebleach/CRTASnq')
    if 220 < ran and ran < 260:
        await ctx.send('https://imgur.com/gallery/WfAf0Ad')
    if 260 < ran and ran < 300:
        await ctx.send('https://imgur.com/gallery/2HdVD')
    if 300 < ran and ran < 340:
        await ctx.send('https://imgur.com/r/cursedimages/zx3RrI6')
    if 340 < ran and ran < 380:
        await ctx.send('https://imgur.com/r/cursedimages/p6UEwed')
    if 380 < ran and ran < 420:
        await ctx.send('https://imgur.com/r/cursedimages/T0qOhB7')
    if 420 < ran and ran < 460:
        await ctx.send('https://imgur.com/r/cursedimages/sSNy98x')
    if 460 < ran and ran < 500:
        await ctx.send('https://imgur.com/r/cursedimages/gv5R5Po')
    if 500 < ran and ran < 540:
        await ctx.send('https://imgur.com/r/cursedimages/uWLwHkL')
    if 540 < ran and ran < 580:
        await ctx.send('https://imgur.com/r/cursedimages/LjPd7UX')
    if 580 < ran and ran < 620:
        await ctx.send('https://imgur.com/r/cursedimages/otEDgXh')
    if 620 < ran and ran < 660:
        await ctx.send('https://imgur.com/r/cursedimages/CmZiWGb')
    if 660 < ran and ran < 700:
        await ctx.send('https://imgur.com/r/makemesuffer/J48cdZU')
    if 700 < ran and ran < 740:
        await ctx.send('https://imgur.com/r/makemesuffer/kWswODJ')
    if 740 < ran and ran < 780:
        await ctx.send('https://imgur.com/r/makemesuffer/mEv1bzW')
    if 780 < ran and ran < 820:
        await ctx.send('https://imgur.com/r/cursedimages/Q5Cu23a')
    if 820 < ran and ran < 860:
        await ctx.send('https://imgur.com/r/makemesuffer/pfL99Oy')
    if 860 < ran and ran < 900:
        await ctx.send('https://imgur.com/r/makemesuffer/Nel1VpP')
    if 900 < ran and ran < 940:
        await ctx.send('https://imgur.com/r/cursedimages/fuO4JoZ')
    if 940 < ran and ran < 980:
        await ctx.send('https://imgur.com/r/cursedimages/IxUbLzH')
    if 980 < ran and ran < 990:
        await ctx.send('https://imgur.com/gallery/I7brSfK')
    if 990 < ran and ran < 1000:
        await ctx.send('https://imgur.com/gallery/G5yM8je')

@bot.command(pass_context = True)
async def _2ball(ctx, pregunta):
    
    ran2 = (random.randrange(100))
    if  0 < ran2 and ran2 < 50 :
        await ctx.send('si')
    if 50 < ran2 and ran2 < 100:
        await ctx.send('no')

@bot.command(pass_context=True)
async def  god(ctx):
    await ctx.send('<:god:667173824055214142>')

@bot.command(pass_context=True)
async def  ship(ctx):
    await ctx.send('<:caramondongo:668658832532176947> :crossed_swords: <:god:667173824055214142>')


from discord.ext import commands
from discord.utils import get

@bot.command(pass_context=True)
async def infierno(ctx, Member:discord.Member):
    key = ctx.message.author
    this_member = Member
    this_guild = Member.guild
    this_role = get(this_guild.roles, id=int('621047585624293387'))
   
    if str(key) == 'Rash#9901':
        await ctx.send('Compadre dele nomas')
        await this_member.add_roles(this_role)
    elif str(key) == 'Vicho_#7195':
        await ctx.send('Compadre dele nomas')
        await this_member.add_roles(this_role)
    elif str(key) == 'gangweeder#0165':
        await ctx.send('Compadre dele nomas')
        await this_member.add_roles(this_role)
    elif str(key) == 'EspinOxet#8454':
        await ctx.send('Compadre dele nomas')
        await this_member.add_roles(this_role)
    else:
        await ctx.send('Compadre no tiene permiso')
    print (key)    

@bot.command(pass_context=True)
async def cacapeo(ctx):
    author = ctx.message.author
    await ctx.send("Hola {}, este comando no hace absolutamente nada".format(ctx.message.author.mention))

@bot.command(pass_context=True)
async def desinfierno(ctx, Member:discord.Member):
    key = ctx.message.author
    this_member = Member
    this_guild = Member.guild
    this_role = get(this_guild.roles, id=int('621047585624293387'))
   
    if str(key) == 'Vicho_#7195':
        await ctx.send('Compadre dele nomas')
        await this_member.remove_roles(this_role)
    else:
        await ctx.send('Compadre no tiene permiso')
    print (key)

@bot.command(pass_context=True)
async def creepypasta(ctx):
     await ctx.send('https://www.youtube.com/watch?v=iczeg0E_ff4')


@bot.event
async def on_message_delete(message):
	contenido = message.content
	if contenido.lower().count("se te cayó esto") > 0:
		await message.channel.send('Compare usted me esta vacilando?¿¿?¿?')
		print (contenido)
		return
		
	else:
		contenido1 = message.content
		autor = message.author
		await message.channel.send('Oye {},se te cayó esto: {}'.format(
        autor.mention, contenido1))
		return



@bot.event
async def on_message(message1):
    contenido1 = message1.content
    autor1 = message1.author
    if message1.author.bot:	
        return
    else:
        if contenido1.lower().count("lili") > 0:
            await message1.channel.send(
                'Una cagada asquerosa, repelente, abyecta, vomitiva, mugrosa, maldita, diarreosa, estercolera, inmunda, malnacida, pudenda, apestosa, maloliente, cabrona, maricona, huevona, pendeja, tarada, cancerígena, jodida, culeada, gilipollesca, pelotuda, encamada, malnacida, retardada, atrasada, inútil, móngola, incestuosa, burda, estúpida, insulsa, putrefacta, traicionera, indigna, chupapollas, soplahuevos, esnifacojones, gueleculo, coprofágica, masca-morrones, infecta, cerda, nauseabunda, cochambrosa, cochina, verdulera, infame, ruin, rastrera, degradada, descerebrada, zopenca, zafia, puta, engreída, esquizofrénica, granulenta, infeliz, profana, calamitosa, deficiente, cretina, lela, ramera, fulana, calientaguevos, ridícula, petarda, pasmarote, fistro, desidiosa, puta, reputa, soputa, recontraputa, hija de puta, hija de un millón de putas, escupepitos, caradepedo, necrofílica, alientoamojón, lambe-bukaka, revuelcaleche, coñoesumadre y de su abuela, conchuda, culoroto, nalgas reventadas, tragasable, succionaditos, esfinterpartido, ojetedesilachado, sorbemocos, capulla, pelmaza, zoquete, masturbadora crónica, espuria, chupa-tampones, regluda, coprófaga, gerontofílica, turra, ojete, atorrante, tierrúa, pajúa, amamaguevos, onanista caradeconcha y MALA PELICULA')
        if contenido1.lower().count('hipocrita') > 0:
            await message1.channel.send('Tú por ejemplo')
        if contenido1.lower().count('hipócrita') > 0:
            await message1.channel.send('Tú por ejemplo')
        if contenido1.lower().count('sebita') > 0:
            await message1.channel.send('Saquese el gorro')
        if contenido1.lower().count('420') > 0:
            await message1.channel.send('Nice.')
        if contenido1.lower().count('calibre 22') > 0:
            await message1.channel.send('La mejor arma para un tiroteo')
        if contenido1.lower().count('perkin') > 0:
            await message1.channel.send('Es el Sebita')
            await message1.channel.send('<:perkin:669661978918256672>')
        if contenido1.lower().count('cobarde') > 0:
            await message1.channel.send(
                'Oye {},me dijiste cobarde y aqui estoy.'.format(
                    autor1.mention))
        if contenido1.lower().count('cara') > 0:
            await message1.channel.send('Cuál de las dos?????¿')
        if contenido1.lower().count('norambuena') > 0:
            await message1.channel.send('Buen Provecho')
            await message1.channel.send(
                'h͘i҉̡p̨̛̕͝ǫ̛̀͝҉̀ç̷̀̀҉̧̀͞r͏̛̛́́̕͠͠í̷̶̶̢͠t̡̕͜͞à͜')
        if contenido1.lower().count('noram') > 0:
            await message1.channel.send('Buen provecho')
            await message1.channel.send(
                'h͘i҉̡p̨̛̕͝ǫ̛̀͝҉̀ç̷̀̀҉̧̀͞r͏̛̛́́̕͠͠í̷̶̶̢͠t̡̕͜͞à͜')
        if contenido1.lower().count('pyrso') > 0:
            await message1.channel.send('Buen provecho')
            await message1.channel.send(
                'h͘i҉̡p̨̛̕͝ǫ̛̀͝҉̀ç̷̀̀҉̧̀͞r͏̛̛́́̕͠͠í̷̶̶̢͠t̡̕͜͞à͜')
        if contenido1.lower().count('aplausos') > 0:
            await message1.channel.send('*Se va llorando*')
            await message1.channel.send(
                'h͘i҉̡p̨̛̕͝ǫ̛̀͝҉̀ç̷̀̀҉̧̀͞r͏̛̛́́̕͠͠í̷̶̶̢͠t̡̕͜͞à͜')
            await message1.channel.send(
                'https://www.youtube.com/watch?v=iczeg0E_ff4')
        if contenido1.lower().count('arredondo') > 0:
           await message1.add_reaction('<:god:667173824055214142>')
        if contenido1.lower().count('arrund') > 0:
           await message1.add_reaction('<:god:667173824055214142>')
        if contenido1.lower().count('arund') > 0:
           await message1.add_reaction('<:god:667173824055214142>')
        if contenido1.lower().count('arrebot') > 0:
           await message1.add_reaction('<:god:667173824055214142>')
        if contenido1.lower().count('esquizofrénico') > 0:
           await message1.add_reaction('<:god:667173824055214142>')
		
    await bot.process_commands(message1)

  
    
bot.run(TOKEN)
