from linkedin import Linkedin

# Authenticate using any Linkedin account credentials
api = Linkedin(USERNAME, PASSWORD)

# GET list of profiles
results = api.search_people(keywords='Tomas Cano')

# GET a first profile
profile = api.get_profile(results[0]['public_id'])
print(profile)
image_url = profile.get('displayPictureUrl') + profile.get('img_100_100')
print(image_url)
