import requests

link = input('Discord Invite Link: https://discord.gg/3g5vDrQ7')
if len(link) > 6:
    link = link[19:]
apilink = "https://discordapp.com/api/v6/invite/" + str(link)

print (link)

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip(ODE2MjEwNzM5MzQ5OTQ2Mzk4.YFcpbQ.tM4r6NHEn95l-Y_kc6987kzqrok)
            headers={
                'Authorization': token
                }
            requests.post(apilink, headers=headers)
        print ("All valid tokens have joined!")
