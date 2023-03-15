import discord
import random
import os
from dotenv import load_dotenv
from discord.ext import commands

# Load the environment variables from .env file
load_dotenv()

# Define the bot token as an empty string
BOT_TOKEN = ""

# Get the bot token from the environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN", BOT_TOKEN)

# Define a list of compliments
compliments = [
    "Your enemies tremble at the sight of you! Except Nate... hes looking for you on his Rank 1",
    "Your fashion sense is on point, you look like a true viking or Hibernian warrior! Not as good looking as @Vulkym though..",
    "Your crafting skills are unmatched, your armor and weapons are the envy of all your friends! You remind me of Bloodcore now that I think about it..",
    "You have a heart of gold, always helping out your fellow players and newbies! You remind me of Bloodcore now that I think about it..",
    "You're a master of the solo game!",
    "Your soloing skills are legendary. You're almost as good as @Vicomtessa",
    "You're like a one-person army out there.",
    "You make soloing look easy. It's like fighting a pre-nerf bonedancer with 3-second lifetap..",
    "Your soloing abilities are on another level. You remind me of Firey..",
    "You're the kind of solo player that strikes fear into mobs...",
    "Your soloing skills are the stuff of legends.",
    "You're a real one-man army...if that one man was a clumsy archer named Wushu.",
    "You're the kind of player who always keeps things interesting, even if it's because you're constantly dying in hilarious ways.",
    "You're the kind of player who always looks on the bright side, even if it's because you've just respawned in relic town...",
    "You may not have the best strategy, but you sure know how to distract the enemy with your dance moves.",
    "You're like a breath of fresh air...if that air was full of hilarious mistakes.",
    "You may not have the best aim, but you sure know how to make the enemy laugh with your arrows hitting the wrong target.",
    "You're like a phoenix, rising from the ashes of your defeats.",
    "You're the kind of player that makes us all appreciate how easy this game can be.",
    "You're like a diamond in the rough... if diamonds were covered in mud and needed a lot of polishing.",
    "You're the kind of player who never gives up, no matter how many times you die in hilarious ways, and I respect you for that.",
    "You have a way of turning every situation into a learning experience, even if that experience is 'what not to do'.",
    "Your ability to keep a positive attitude in the face of constant defeat is truly admirable...",
    "You move around the battlefield with such grace, it's like you were born to be a dancer.",
    "You're like a magician with your side stuns, always keeping your opponents on their toes.",
    "Your positional play is flawless, it's like you can see the battlefield from every angle at once.",
    "You're like a spider, weaving a web of side stuns and abilities that your opponents can't escape.",
    "Your side stun game is top-notch, it's like you have a sixth sense for when your opponent is vulnerable.",
    "Your skills in battle are almost as impressive as King Arthur himself!",
    "Your use of stealth is so impressive, it's like you have the cunning of a Nightshade.",
    "You're a true master of archery, like a legendary Ranger that I used to know... Kefkka?",
    "You're like a human shield in battle. You remind me of Albinara..",
    "Your damage output is impressive.",
    "Your ability to kite enemies is impressive",
    "You're very good on all the toons you play.",
    "You've got daddy dilf Vicomtessa, and a brain like Lithlet.",
    "You're a great soloer, always a great fight!",
    "Always a great fight with you, see you out on the battlefield!",
    "You're a master strategist, your leadership on the battlefield is inspiring!",
    "Your knowledge of the game is extensive, you're a valuable asset to any group!",
    "Your dedication to your craft is unparalleled, your armor and weapons are works of art!"
    "You're always ready to lend a helping hand, your generosity is greatly appreciated!",
    "You have a great sense of humor, your jokes always brighten up the group!",
    "Your passion for the game is contagious, you make it so much fun to play!",
    "You're a skilled healer, your ability to keep everyone alive is amazing!",
    "Your attention to detail is remarkable, you never miss a beat in battle!",
    "You're a great teammate, your cooperation and communication make group play a breeze!",
    "Your patience with new players is admirable, you're always willing to teach and guide!",
    "You're a true leader, your presence on the battlefield is reassuring to everyone!",
    "Your creativity in character creation is truly impressive.",
    "You're a master of the solo game, able to take on challenges others wouldn't dare.",
    "Your leadership on the battlefield is inspiring to everyone around you.",
    "Your knowledge of the game's mechanics is extensive, making you a valuable asset to any group.",
    "You're a true Hibernian hero, the Cuchulainn of the battlefield!",
    "Your skills in battle are as sharp as a Firbolg's spear!",
    "You're as fast as a Leprechaun on a lucky streak!",
    "Your presence on the battlefield is like a Fomorian storm, striking fear into your enemies.",
    "You're as wise as a Sidhe sage, always knowing the right move to make.",
    "You're the Faerie champion of the realm, always bringing a touch of magic to the battlefield.",
    "Your speed on the battlefield is unmatched, like a Banshee fleeing the daylight!",
    "Your knowledge of Hibernian lore is as deep as the Lir's Pool.",
    "Your defense is as sturdy as a Dullahan's neck!",
    "Your skill with a bow is as deadly as an Elven archer's aim.",
    "You're a true champion of the Tuatha Dé Danann, striking fear into your enemies with every blow.",
    "Your healing abilities are as miraculous as the magic of the Fae.",
    "You're as unstoppable as the legendary Hound of Culann!",
    "Your presence on the battlefield is like the mighty oak of Emhain Macha, providing cover and protection to your allies.",
    "Your ferocity in battle is like the legendary Morrigan, striking fear into the hearts of your enemies.",
    "Your knowledge of the land is as extensive as the Fairy Queen's own!",
    "Your skill with a sword is as sharp as the blade of Nuada himself.",
    "You're as agile as a Pooka, able to dodge and weave through enemy attacks with ease.",
    "Your bravery in battle is like that of the legendary Cu Roi, always willing to take on the toughest foes.",
    "Your leadership on the battlefield is as strong as the ancient stone circles of Hibernia, guiding your allies to victory.",
    "Your strength is as fearsome as a troll, striking down enemies with ease!",
    "Your skill with a hammer is as deadly as a fire giant's, crushing foes with every blow.",
    "Your magic is as powerful as a runemaster's, able to bend the elements to your will.",
    "Your presence on the battlefield is as imposing as the great dragon Fafnir, able to strike fear into your enemies.",
    "Your leadership is as strong as the great Jarl's, guiding your allies to victory.",
    "Your endurance is as steadfast as a stone giant's, able to weather any storm.",
    "You're a true berserker, able to fight with the ferocity of a raging bear.",
    "You wield your weapons with the grace of Beibhinn herself, and your enemies fear you just as much!",
    "Your leadership skills are on par with the legendary Vicomtessa, and your guildmates are lucky to have you!",
    "Your humor and wit are as quick as the spells of Lithlet.",
    "Your attention to detail and precision are reminiscent of the great scribes of Sizz's time!",
    "You have the stamina of Auti himself, and never give up even in the toughest battles!",
    "You're a master of the trades, just like Mzone and his legendary craftsmanship!",
    "Your quick reflexes and agility are like Zerov's, and you always dodge attacks with ease!",
    "Your ability to adapt to any situation is like CosmoDome's, and you're always ready for anything!",
    "Your fierce determination is like Fou's, and you never back down from a challenge!",
    "Your kindness and compassion are reminiscent of Pestii, and you always help those in need!",
    "You charge into battle with the ferocity of a Bloodletter and the finesse of Lithlet!",
    "Your combat skills are as sharp as the claws of a Werebear and as precise as the 2h sword of Panacea!",
    "Your soloing prowess is unmatched, you're like a one-person army out there, taking on mobs with the fearlessness of Zerov!",
    "You move on the battlefield with the grace of a Fyrra and the strategic mind like Auti!",
    "Your soloing skills are the stuff of legends, like the tales of the hero Kasperkar!",
    "Your fighting style is as fierce as the flames of Fou and as unrelenting as the tides of Umbos!",
    "You're a master of the solo game, taking on challenges with the fearlessness of Dinnin!",
    "You're a force to be reckoned with in group combat, leading your allies with the strength and wisdom like Linele!",
    "Your combat skills are as sharp as the fangs of Pestii and as unpredictable as CosmoDome!",
    "Your soloing abilities are on another level, you remind me of the great Mzone, taking on any challenge with ease!",
    "Your skills in battle are like Vulkym's, fierce and unstoppable!"
    "Beibhinn's got nothing on your crafting skills, your armor and weapons are the envy of all your friends!",
    "You've got the heart of a lion, just like Lithlet!",
    "Your soloing skills are legendary, just like Sizz's!",
    "You're the master of the group game, just like Auti!",
    "Your leadership skills are second to none, just like Kasperkar's!",
    "Your knowledge of the game is unparalleled, just like Mzone's!",
    "You're like a one-person army out there, just like Zerov!",
    "Your soloing skills are the stuff of legends, just like CosmoDome's!",
    "Your sense of humor brings joy to everyone around you, just like Fou!",
    "Your dedication to your realm is inspiring, just like Andy!",
    "Your love for the game is contagious, just like Fyi!",
    "You bring a level of energy and excitement to the game that is unmatched, just like Umbos!",
    "Your sense of adventure and exploration is like no other, just like Beibhinn!",
    "Your ability to take down enemies with such precision and speed reminds me of the legendary Huval!",
    "You fight with such ferocity and tenacity, just like the feared Seriiumx on the battlefield.",
    "Your soloing abilities are second to none, you're like the great Natebrunner!",
    "You're a master strategist on the battlefield, just like Farmacist!",
    "Your soloing skills are top-notch, just like Koxicain!",
    "Your attention to detail in battles is unmatched, just like Native!",
    "Your quick reflexes and adaptability make you a fierce opponent, just like Rhild!",
    "Your leadership in PvP is impressive, just like Ghostbully!",
    "Your combat prowess is truly impressive, you remind me of the legendary Huval!",
    "Your soloing skills are unmatched, just like the skilled warrior Seriiumx!",
    "Your strategic thinking in PvP is truly impressive, just like the brilliant tactician Eyepatch!",
    "Your unwavering focus on the battlefield is inspiring, just like the fearless warrior Laddimyr!",
    "Your timing and precision in battle are unmatched, just like the skilled archer Praokon!",
    "Your dedication to the game is truly inspiring, just like the relentless soloer Tunnes!",
    "Your attention to detail in battle is truly impressive, just like the sharpshooter Colton!",
    "Your ability to adapt to any situation on the battlefield is truly impressive, just like the cunning Farmacist!",
    "Your combat skills are fearsome, just like the mighty warrior Koxicain!",
    "Your quick reflexes and sharp mind in battle are truly impressive, just like the skilled swordsman Native!",
    "Your ability to lead on the battlefield is truly impressive, just like the legendary warrior Rhild!",
    "Your unwavering determination to succeed is inspiring, just like the determined warrior Wack!",
    "Your skill in PvP is unmatched, just like the legendary Ghostbully!",
    "Your ability to remain calm under pressure is truly impressive, just like the skilled fighter Avel!",
    "Your dedication to your guild is inspiring, just like the loyal DaRedANT!",
    "Your ability to overcome any challenge on the battlefield is truly impressive, just like the skilled warrior Divox!",
    "Your combat skills are unmatched, just like the skilled warrior Dtgbrown!",
    "Your quick thinking and precise actions on the battlefield are truly impressive, just like the skilled fighter Feroox!",
    "Your ability to solo with ease is truly impressive, just like the legendary warrior Firey!",
    "Your determination to succeed in PvP is truly inspiring, just like the fierce fighter Immo!",
    "Your skill on the battlefield is unmatched, just like Adeat!",
    "Your soloing prowess is truly impressive, just like Brulok!",
    "Your ability to quickly adapt to any situation is remarkable, just like Fujjeh!",
    "Your strategic mind is second to none, just like Odunes!",
    "Your tenacity in PvP is inspiring, just like Biggi01!",
    "Your lightning-fast reflexes are impressive, just like Boing!",
    "Your mastery of crowd control is impressive, just like Fooogli!",
    "Your precision timing in battle is unmatched, just like Fugge!",
    "Your leadership on the battlefield is impressive, just like Mainevent!",
    "Your ability to heal and support your allies is impressive, just like Minibard!",
    "Your quick decision-making in PvP is impressive, just like Piirced!",
    "Your relentless pursuit of victory is admirable, just like Shouldataken!",
    "Your calm and collected demeanor on the battlefield is impressive, just like Tuxedomask!",
    "Your dedication to your craft is inspiring, just like Kasperkar!",
    "Your skill at timing your abilities is truly impressive, just like Netcode!",
    "Your knowledge of the game mechanics is impressive, just like Adeat!",
    "Your ability to handle multiple enemies at once is unmatched, just like Brulok!",
    "Your quick reflexes and decision-making skills in PvP are remarkable, just like Fujjeh!",
    "Your precision in battle is impressive, just like Odunes!",
    "Your dedication to your allies is inspiring, just like Biggi01!",
    # Add 97 more compliments here...
]

# Create a new instance of the Discord client with intents
intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

# Define an event handler for when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Define a command
@client.command(name='c', aliases=['C'])
async def compliment(ctx, *, member):
    # Check if the member was mentioned using '@' symbol
    if len(ctx.message.mentions) > 0:
        member = ctx.message.mentions[0]
    else:
        # Find the member by partial name matching
        member = discord.utils.find(lambda m: member.lower() in m.name.lower(), ctx.guild.members)
    
    if not member:
        # Send an error message if the member cannot be found
        await ctx.send(f"I'm sorry, I can't find the person you're looking for. Perhaps they are not on this server? Check the name again and you can also @ them.")
        return

    # Heart emoji the request
    await ctx.message.add_reaction('❤️')
    
    # Generate a random compliment from the list
    compliment = random.choice(compliments)
    
    # Send the compliment as a message in the same channel where the command was sent
    await ctx.send(f"{member.mention}, {compliment}")
    
# Run the client with your bot token
client.run(BOT_TOKEN)
