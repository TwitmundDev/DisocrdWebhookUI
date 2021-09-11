from tkinter import *
from functools import partial
import requests #dependency

def validateLogin(title, body, username, url, desc):


	username = username

	url = url.get()  # webhook url, from here: https://i.imgur.com/f9XnAew.png

	# for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
	data = {
		"username": username.get()
	}

	# leave this out if you dont want an embed
	# for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
	data["embeds"] = [
		{
			"description": desc.get(),
			"title": title.get(),
			"icon_url": "https://avatars0.githubusercontent.com/u/14542790"
		}
	]

	result = requests.post(url, json=data)

	try:
		result.raise_for_status()
	except requests.exceptions.HTTPError as err:
		print(err)
	else:
		print("Payload delivered successfully, code {}.".format(result.status_code))

	#print("username entered :", username.get())
	#print("password entered :", password.get())
	return

#window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Discord webhook send')

#Title of webhhok message
titleLabel = Label(tkWindow, text="Title").grid(row=0, column=0)
title = StringVar()
TtitleEntry = Entry(tkWindow, textvariable=title).grid(row=0, column=1)

#Body of webhhok message
bodyLabel = Label(tkWindow, text="body").grid(row=3, column=0)
body = StringVar()
bodyEntry = Entry(tkWindow, textvariable=body).grid(row=3, column=1)


#username of webhhok bot
usernameLabel = Label(tkWindow, text="Username").grid(row=3, column=2)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=3, column=3)


#url of webhhok bot
urlLabel = Label(tkWindow, text="url du webhook").grid(row=4, column=0)
url = StringVar()
urlEntry = Entry(tkWindow, textvariable=url).grid(row=4, column=1)




#desc of webhhok message
descLabel = Label(tkWindow, text="desc du webhook").grid(row=5, column=0)
desc = StringVar()
descEntry = Entry(tkWindow, textvariable=desc).grid(row=5, column=1)






validateLogin = partial(validateLogin, title, body, username, url, desc)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=10, column=1)


tkWindow.mainloop()