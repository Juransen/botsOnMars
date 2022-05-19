# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import asyncio
import discord
import random
import keys_tokens

try:
    with open("users.txt", "r") as users_file:  # r = read
        users = users_file.readlines()
        print(str(users))
except FileNotFoundError:
    users = []
f = open("users.txt", "a")  # a = append


def add_user(user):
    if not str(user) in users:
        f.writelines(str(user) + "\n")
        users.append(str(user))
        print(str(user) + " added")
        f.flush()
    else:
        print(str(user) + " already exists")


class MyClient(discord.Client):

    # ----------------------------einlogen------------------------------------------------------------------------------
    async def on_ready(self):
        print("Ready!! Let's do some shit!")

    # ----------------------------Bei Nachrichten-----------------------------------------------------------------------
    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith("blib") or message.content.startswith("blob"):
            if message.channel.id == keys_tokens.botChannel:
                return
            else:
                async with message.channel.typing():
                    await asyncio.sleep(2)
                await message.channel.send(':rage: Humans....', delete_after=5)
                await message.delete()
            data = await message.channel.history(limit=50).flatten()
            for i in data:
                if i.author.bot and not i.author == client.user:
                    await i.delete()

        if message.content.startswith("gang"):
            if str(message.channel.type) != "private":
                await message.author.send("Willst du in die Gang? Dann antworte mit GANG")

        if message.content.lower() == "gang" and str(message.channel.type) == "private":
            add_user(message.author)

        if message.content == "!":
            async with message.channel.typing():
                await asyncio.sleep(2)
            await message.channel.send("https://tenor.com/view/running-cat-gif-20552615")

        if message.content == "dab!":
            await message.channel.send("https://media.giphy.com/media/d4blihcFNkwE3fEI/giphy.gif")

        if message.content.startswith("martian"):
            await message.channel.send('waaas geht?')
            await message.author.send('du hast mich erwähnt, jetzt spam ich mal kurz')

        # ----------------Löschen von Nachrichten-----------------------------------------------------------------------
        if message.content.startswith("delete") or message.content.startswith("Delete"):
            if type(message.channel) == discord.DMChannel:
                await message.channel.send("Sorry, diese Funktion ist in DM's nicht verfügbar")

            kindofdelete = message.content.split(' ')[1]
            if kindofdelete.lower() == "all":
                if message.author.top_role.id == keys_tokens.adminRole:
                    data = await message.channel.history().flatten()
                else:
                    await message.channel.send(":face_with_monocle: das kannst du nicht tun!", delete_after=20)
                    print("versuchte Massenlöschung ohne Recht!! von " + str(message.author))
            else:
                if int(kindofdelete) > 3 and message.author.top_role.id != keys_tokens.adminRole:
                    await message.channel.send(
                        "das kannst du nicht tun! Du kannst maximal 5 Nachrichten löschen :wink:", delete_after=20)
                else:
                    data = await message.channel.history(limit=int(kindofdelete) + 1).flatten()

            index = 0
            for i in data:
                await i.delete()
                index += 1
            embed = discord.Embed(title="Work done!", colour=0xff0000)
            embed.add_field(name="Count of deleted Messages:", value=str(index - 1), )
            embed.set_image(url="https://cdn.discordapp.com/emojis/805369138318671872.png?v=1")
            print("Löschender User: " + str(message.author))
            await message.channel.send(embed=embed, delete_after=30)

        # -----------------------Roulette-------------------------------------------------------------------------------
        # todo: coinsystem implementieren bzw in klasse outsourcen

        if message.content.startswith("$$$"):
            bid = message.content.split(' ')[1]
            if bid.lower() == "black":
                bid_param = -1
            elif bid.lower() == "red":
                bid_param = -2
            else:
                try:
                    bid_param = int(bid)
                except:
                    bid_param = -3

            if bid_param == -3:
                await message.channel.send('Ungültige Eingabe')
                return
            result = random.randint(0, 36)
            if bid_param == -1:
                won = result % 2 == 0 and not result == 0
            elif bid_param == -2:
                won = result % 2 == 0 and not result == 1
            else:
                won = result == bid_param
            if won:
                await message.channel.send('$$Gewonnen!!$$')
            else:
                await message.channel.send('Loose')

    # -----------------------------Zusätzliche Funktionen---------------------------------------------------------------

    async def on_message_delete(self, message):
        print("Gelöschte Nachricht: " + message.content)


client = MyClient()
client.run(keys_tokens.token)
