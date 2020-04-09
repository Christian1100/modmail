from discord import Embed, Guild, Member, Role
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, Greedy, group
from discord.utils import get

levels = {};
def setup(maxLevel):
  for i in range(1, maxLevel+1):
    levels[i] = " [:zap:" + str(i) + "]";

# Setup
setup(140)

class PowerLevel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command()
    async def powerlevel(self, ctx, *, content:str):
        # Vars
        guild   = ctx.message.guild;
        author  = ctx.message.author;
        user_id = author.id;
        channel = ctx.channel;
        # Check
        if channel.id == 454274882688122880 or channel.id == 454274841047072768:
          if content.isdigit():
              # Vars
              index  = int(content);
              member  = guild.get_member(user_id)
              # New Nickname
              if index > 0 and index <= 140:
                  tag = levels[index];
                  # New Nickname
                  await member.edit(nick=author.name + ' ' + tag)
                  # Reaction
                  await ctx.message.add_reaction(':white_check_mark:')
              else:
                  # Error Message
                  error   = '**<@' + str(user_id) + '>, per favore inserisci un power level valido.**';
                  # Send Message
                  await ctx.send(error)
          elif content == 'reset':
              member  = guild.get_member(user_id)
              # New Nickname
              await member.edit(nick=author.name)
              # Reaction
              await ctx.message.add_reaction(':white_check_mark:')
          else:
            await ctx.send(error)
        
def setup(bot):
    bot.add_cog(PowerLevel(bot))
