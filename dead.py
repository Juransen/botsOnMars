import discord
import asyncio


user = await client.fetch_user("insert UserID")  # Nachricht für Katja---------------------------------------
initiator = await client.fetch_user("insert UserID")
if message.content.startswith("demo"):
    if message.author == initiator:
        print(user)
        print("initiator ist: " + str(initiator))
        await user.send('Hallo ' + user.name + '\ndu kennst mich hoffentlich noch vom Mars. :innocent:')
        await asyncio.sleep(10)
        await user.send('In erster Linie möchte ich dir zum Geburtstag gratulieren!!:heart:\n'
                        '\nIch wünsche dir alles Gute und hoffe du hast einen schönen Tag trotz dieser merkwürdigen'
                        ' Situation. Ich bekomme das Ganze ja nicht wirklich mit, da ich unter einem Schuhschrank '
                        'lebe. Aber ist Alles nicht so einfach, hab ich mir sagen lassen :confused:')
        await asyncio.sleep(15)
        embed = discord.Embed(title="Tipp:", colour=0xff0000)
        embed.add_field(name="Ja", value="ist hierbei die richtige Antwort :yum:", inline=False)
        await user.send('Aber lass den Kopf nicht hängen!\n`das_Sofa_Alex` und `Juransen` haben sich Gedanken gemacht'
                        ', wie sie dir diese Zeit besser machen können. Und da komme ich ins Spiel :partying_face: ich hab'
                        ' dir nämlich was mitgebracht...\nWillst'
                        ' du wissen was ich für dich habe?\n')
        await asyncio.sleep(10)
        await user.send(embed=embed)
        print("phase 1 abgeschlossen")
    else:
        await message.author.send("kek das ist kein Befehl für dich!")

if type(message.channel) == discord.DMChannel:
    print(message.content, message.author)
    if message.content.startswith("Ja") or message.content.startswith("ja") and message.author == user:
        await user.send("https://cdn.discordapp.com/attachments/767605508928307202/794581887074959370/LCFireworks.gif")
        async with message.channel.typing():
            await asyncio.sleep(5)
        embed = discord.Embed(title="Geschenkkarte:", colour=0xffA500)
        embed.add_field(name="Origin", value="du hast ein Spiel auf Origin bekommen:partying_face:", inline=False)
        embed.set_image(url="https://game2gether.de/wp-content/uploads/2017/10/Die-Sims-4-Hunde-Katzen.jpg")
        embed.add_field(name="Dein Zugang:", value="**Account:**\ndein Gmail-Konto mit dem du aktuell in Google ange"
                                                   "meldet bist\n**Passwort:** geht dich n scheiss an")
        embed.set_footer(text="Origin ist bereits auf deinem PC installiert\ndu musst nur noch das Spiel"
                              " runterladen und kannst loslegen")
        await user.send(embed=embed)
        async with message.channel.typing():
            await asyncio.sleep(15)
        await user.send(
            "Wir hoffen, dass du viel Spaß mit dem Spiel haben wirst!\nWir haben dich sehr Lieb! :gift_heart:")
        await user.send("Übrigens: Schau doch mal in Minecraft auf eurem Server vorbei! Da Steht noch eine"
                        " kleine Überraschung für an deinem Häuschen am Strand :kissing:")
        async with message.channel.typing():
            await asyncio.sleep(5)
        await user.send("https://media.giphy.com/media/mcJohbfGPATW8/giphy.gif")
    else:
        await message.channel.send('lel, ich versteh das nicht.')
    print("Gruß abgeschlossen")
    # ------------------------------------------------------------------------------------------------------------------

    if message.content.startswith("!stats"):
        messages = await message.channel.history(limit=50).flatten()
        for i in messages:
            print(i.content)
        counter = 0
        async for m in message.channel.history():
            if m.author == client.user:
                counter = counter + 1
        print(counter)  # zählt seine eigenen Nachrichten
