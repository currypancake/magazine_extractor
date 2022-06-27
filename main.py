import os
import requests
from bs4 import BeautifulSoup


# set info
f = open('login_cookie.txt', 'r')
login_cookie = f.read()

user_agent = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
headers = {'User-Agent': user_agent}
dummy_cookies = {'SP_LOGIN_SESSION' : login_cookie}

def setDirPath(dir_path):
	if os.path.isdir(dir_path) == False:
		os.mkdir(dir_path)

def extract_magazines():
	f = open('magazine_list_url.txt', 'r')
	url = f.read()

	req = requests.get(url, cookies=dummy_cookies, headers=headers)
	soup = BeautifulSoup(req.content, 'html.parser')
	target = soup.select('div.ui-button-sub4>a')

	num = 0
	for i in target:
		dir_path = f"{num}"
		setDirPath(dir_path)
		magazine_url = "http://g12017647.sp.pf.mbga.jp/" + i['href']
		extract_url(magazine_url, dir_path)
		num += 1

def extract_url(url, dir_path):
	req = requests.get(url, cookies=dummy_cookies, headers=headers)
	soup = BeautifulSoup(req.content, 'html.parser')
	target = soup.find_all('script')[5].string.split(';')[8]
	target = target.split('\"')

	save_images(target, dir_path)


def save_images(target, dir_path):
	num = 0;
	for i in target:
		if i.endswith('.png') == True :
			img_url = "http:" + i
			img_req = requests.get(img_url, cookies=dummy_cookies, headers=headers, stream=True)

			img_name = dir_path + f'/{num}.png'
			with open(img_name, 'wb') as f:
				f.write(img_req.content)

			num += 1


if __name__ == "__main__":
	extract_magazines()