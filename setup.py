Token = input("Please enter the Bot account's Token: \t")
ChannelID = input("Please enter the Channel ID you wish to monitor: \t").replace(" ", "").split("|")
File = open("bot.py", 'r')
Contents = File.read()
File.close()
Contents = Contents.replace("**TOKEN**", Token)
Contents = Contents.replace("**START IF**", "**SEGMENT IF**")
Contents = Contents.replace("**END IF**", "**SEGMENT IF**")
Contents = Contents.split("**SEGMENT IF**")

SEGMENT = Contents[1]
Contents[1] = Contents[1].replace(r"**CHANNEL_ID**", ChannelID[0])

for i in range(1, len(ChannelID)):
    Contents[1] = Contents[1]+SEGMENT.replace("**CHANNEL_ID**",ChannelID[i])

Contents = Contents[0]+Contents[1]+Contents[2]
File = open("bot.py", 'w')
File.write(Contents)
File.close()
