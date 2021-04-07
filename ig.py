import instaloader

L = instaloader.Instaloader()

username = input("Please enter username: ")
password = input("Please enter password: ")

def check_followers(username, password):
  
  L.login(username, password)

  profile = instaloader.Profile.from_username(L.context, username)

  followers = []
  following = []

  print("Loading.....")

  for follower in profile.get_followers():
    followers.append(follower)

  for f in profile.get_followees():
    following.append(f)


  for f in following:
    if f not in followers:
      print(f)

check_followers(username,password)
