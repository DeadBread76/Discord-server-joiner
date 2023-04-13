import requests

# Prompt user for Discord invite link
invite_link = input('Discord Invite Link: ')

# Extract code from invite link
if len(invite_link) > 6:
    invite_code = invite_link[19:]
else:
    raise ValueError('Invalid invite link')

# Construct API link using invite code
api_link = f'https://discordapp.com/api/v6/invite/{invite_code}'

# Read tokens from file
try:
    with open('tokens.txt') as f:
        tokens = f.read().splitlines()
except FileNotFoundError:
    print('Error: tokens.txt file not found')
    exit()

# Join server with valid tokens
valid_tokens = 0
for token in tokens:
    headers = {'Authorization': token}
    response = requests.post(api_link, headers=headers)
    if response.status_code == 200:
        valid_tokens += 1

# Print number of valid tokens that joined
print(f'{valid_tokens} valid tokens have joined the server')
