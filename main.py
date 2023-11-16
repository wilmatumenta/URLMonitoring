import requests
def handle_failed_sites(failed_sites):
    print('The following sites failed:')
    for site in failed_sites:
        print(site)
websites = ['https://google.co.uk', 'https://wwebdesign.co.uk', 'https://google.com/nothere']
text_to_match = 'W Web Design'
failed_sites = []
for website in websites:
    try:
        response = requests.get(website)
    except Exception as e:
        failed_sites.append(website + " - " + str(e))
        continue
    if response.status_code != 200:
        failed_sites.append(website + " - " + str(response.status_code))
        continue
    if text_to_match not in response.text:
        failed_sites.append(website + " - " + "Text not found")
if len(failed_sites) > 0:
    handle_failed_sites(failed_sites)
else:
    print('All sites passed')

