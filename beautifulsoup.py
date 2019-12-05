import soup as soup
from bs4 import BeautifulSoup
import urllib.request

# Prints a list of story links on a given page
def getLinks(source):
    links_list = []
    content = urllib.request.urlopen(source)
    url = content.read()
    content.close()
    soup = BeautifulSoup(url, features="html.parser")
    for link in soup.find_all('a'):
        if "premchand-stories" in str(link):
            link_url = str(link.get('href'))
            links_list.append(link_url)
    return links_list


def getStory(link):
    soup_story = BeautifulSoup(urllib.request.urlopen(link).read(), features="html.parser")
    return soup_story.get_text()


# Setup Hindi stories
url_hi = "https://www.rekhta.org/Authors/premchand/stories?lang=hi"
content_hi = urllib.request.urlopen(url_hi).read()
soup_hi = BeautifulSoup(content_hi, features='html.parser')

# Setup Urdu stories
url_ur = "https://www.rekhta.org/Authors/premchand/stories?lang=ur"
content_ur = urllib.request.urlopen(url_ur).read()
soup_ur = BeautifulSoup(content_ur, features='html.parser')

# Prints names of all Hindi stories
# premchand_hindi = soup_hi.find_all("h3", {'class': 'noPoetSubTtl'})
# for story in premchand_hindi:
#     print(story.get_text())
#
# # # Prints names of all Urdu stories
# premchand_urdu = soup_ur.find_all("h3",{'class':'noPoetSubTtl'})
# for story in premchand_urdu:
#     print(story.get_text())

# Creates new file and write Urdu stories to it
urdu_links = getLinks(url_ur)
f = open("premchand_urdu.txt","w+")
for link in urdu_links:
    f.write(getStory(link))
f.close()

#Creates new file and writes Hindi stories to it
# hindi_links = getLinks(url_hi)
# f = open("premchand_hindi.txt","w+")
# for link in hindi_links:
#     f.write(getStory(link))
# f.close()