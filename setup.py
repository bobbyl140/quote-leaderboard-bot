# Variables
Token = ""
Channels = []
yes_no = 'y'

# Get Token For API Use
Token = input("Please enter the Bot account's Token: \t")

# Loop through all channels and add them to a configuration file
while yes_no == 'y':
    # Get the Channel ID
    ChannelID = str(input("Please enter the Channel ID you wish to monitor: \t"))

    # Loop through the question so it can be asked again if needed
    while True:
        # Ask if they have more channels and use a buffer variable for better security and bug protection
        Cont = str(input("Do you have more Channels you want to monitor? (Y/N) \t"))

        # Process the buffer variable and repeat the question incase of malformatting
        if Cont == 'Y' or Cont == 'y' or Cont == "Yes":
            yes_no = 'y'
            break
        elif Cont == 'N' or Cont == 'n' or Cont == "No":
            yes_no = 'n'
            break
        else:
            print("Please respond with \"Yes\" or \"No\" to indicate your answer \t")
            pass
    
    # Add the current channel to the list of channels
    Channels.append(ChannelID)

# Open the Configuration File for the channels as a Writable file
ChannelCFG = open("ChannelID.cfg", 'w+')
TokenCFG = open("Token.cfg", 'w+')

# Convert the List of Channels to a string and remove the list indicators for easier use
ChannelCFG.write(str(Channels).replace('[', '').replace(']','').replace('\'', ''))
TokenCFG.write(str(Token))

# Close Associated Files
ChannelCFG.close()
TokenCFG.close()