import random
import discord
from discord.ext import commands
import asyncio


client = commands.Bot(command_prefix='-', intents = discord.Intents.all())


@client.command('game',  aliases=['Game'])
async def game(context):
    


    i = 1
    your_points = 0
    computer_points = 0

    list1 =  ["stone", "paper", "scissors"]



    embed = discord.Embed(title="Stone paper scissor game", description="Timeout is of 25 seconds" ,color=discord.Color.teal())

    embed.add_field(name="Rules", value="**__Input should be in lowercase__**", inline=False)

    embed.add_field(name="Input your choice", value="Snake / Water/  Gun", inline=True)

    embed.add_field(name="Your points", value="0", inline=True)

    embed.add_field(name="Bot's points", value="0", inline=True)

    embed.add_field(name="Number of chances", value="5", inline=True)        #Loop runs 5 times

    sent = await context.send(embed=embed)


    try:

        while (i <= 5):


            msg = await client.wait_for("message", timeout=25 , check=lambda message: message.author == context.author and message.channel == context.channel and message.content in  ["stone", "paper", "scissors"] )

            choice = random.choice(list1)



            if msg.content == choice:


                embed = discord.Embed(color=discord.Color.teal())



                embed.add_field(name="Score", value=f"You chose {msg.content} and Falcon chose {choice}", inline=False)
                embed.add_field(name="Points", value="No one gets the point", inline=False)
                await context.send(embed=embed)

            elif msg.content == 'stone' and choice == 'scissor':
                your_points = your_points + 1

                embed = discord.Embed(color=discord.Color.teal())


                embed.add_field(name="Score", value=f"You chose {msg.content} and Bot chose {choice}", inline=False)

                embed.add_field(name="Points", value="You get 1 point", inline=False)

                await context.send(embed=embed)

            elif msg.content == 'scissor' and choice == 'stone':
                computer_points = computer_points + 1

                embed = discord.Embed(color=discord.Color.teal())


                embed.add_field(name="Score", value=f"You chose {msg.content} and Bot chose {choice}", inline=False)

                embed.add_field(name="Points", value= "Bot gets 1 point", inline=False)


                await context.send(embed=embed)

            elif msg.content == 'paper' and choice == 'stone':
                
                your_points = your_points + 1

                embed = discord.Embed(color=discord.Color.teal())


                embed.add_field(name="Score", value=f"You chose {msg.content} and Bot chose {choice}", inline=False)

                embed.add_field(name="Points", value="You get 1 point", inline=False)

                await context.send(embed=embed)

            elif msg.content == 'stone' and choice == 'paper':
                computer_points = computer_points + 1


                embed = discord.Embed(color=discord.Color.teal())



                embed.add_field(name="Score", value=f"You chose {msg.content} and Falcon chose {choice}", inline=False)

                embed.add_field(name="Points", value="Bot gets 1 point", inline=False)

                await context.send(embed=embed)

            elif msg.content == 'scissor' and choice == 'paper':
                your_points = your_points + 1


                embed = discord.Embed(color=discord.Color.teal())


                embed.add_field(name="Score", value=f"You chose {msg.content} and Falcon chose {choice}", inline=False)

                embed.add_field(name="Points", value="You get 1 point", inline=False)

                await context.send(embed=embed)

            elif msg.content == 'paper' and choice == 'scissor':
                computer_points = computer_points + 1



                embed = discord.Embed(color=discord.Color.teal())


                embed.add_field(name="Score", value=f"You chose {msg.content} and Falcon chose {choice}", inline=False)

                embed.add_field(name="Points", value="Bot gets 1 point", inline=False)


                await context.send(embed=embed)



            else:
                embed = discord.Embed(title="Invalid input",description="Try again! Input snake \ water \ gun", color=discord.Color.teal())

                await context.send(embed=embed)


                continue


            embed = discord.Embed(color=discord.Color.teal())
            if 5 - i == 0:
                embed.add_field(name="Chances left", value="0", inline=False)
            else:
                embed.add_field(name="Chances Left", value=f"{5-i}, Please input your choice again", inline=False)
            await context.send(embed=embed)

            i = i + 1

        if i > 5:
            # print("Game over""\n")
            embed = discord.Embed(title="**__GAME OVER __**", color=discord.Color.teal())
            # await context.send("Game over")
            await context.send(embed=embed)

            embed = discord.Embed(title="Scorecard", color=discord.Color.teal())
            embed.add_field(name="Players Score", value=f"Your score:{your_points}\nBot's score:{computer_points}\n", inline=False)
            if computer_points > your_points:
                # print("The computer has won and you have lost")
                embed.add_field(name="Final result", value=f"Bot has won and {context.author.mention} has lost", inline=False)
                await context.send(embed=embed)
            elif your_points > computer_points:
                # print("You have won the round and the computer has lost ")
                embed.add_field(name="Final result", value=f" {context.author.mention} has won and Bot has lost", inline=False)
                await context.send(embed=embed)
            else:
                # print("It was a TIE")
                embed.add_field(name="Final result", value="It was a TIE", inline=False)

                await context.send(embed=embed)


    #  Bot will terminate the process if no input is received from the user
    except asyncio.TimeoutError:
        await sent.delete()
        await context.send("Terminating the game due to timeout ")

client.run(TOKEN)