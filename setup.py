Token = Input("Please Enter Your Token: \t")
File = open("bot.py", 'r')
Contents = File.read()
File.close()
Contents = Contents.replace("**TOKEN**", Token)
File = open("bot.py", 'r')
File.write(Contents)
File.close
