from homunculus import world as hmc
# ----------------------------------------------------------------

def find_current_location(world, pid):
  if "passages" in world:
    for passage in world["passages"]:
      if pid == passage["pid"]:
        return passage
  return {}

# ----------------------------------------------------------------

def render(world, current_location):
  if "name" in current_location and "cleanText" in current_location and "links" in current_location:
    print(current_location["cleanText"])
    print()
    for link in current_location["links"]:
      print("({}) {}".format(link["selection"], link["label"]))
    print("\n")
        
def get_input():
  response = input("What do you want to do? (type quit to quit)? ")
  return response.upper().strip()

def update(world, current_location, current_pid, response):
  if response == "":
    return current_pid
  if "links" in current_location:
    for link in current_location["links"]:
      if response == link["selection"]:
        return link["pid"]
      if response == link["label"].upper().strip():
        return link["pid"]
  print("I don't know what you are trying to do.")
  return current_pid

def count_moves(count):
  if "tags" not in current_location or current_location["tags"] == "" or not current_location["tags"].isnumeric():
    return count 
  if int(current_location["tags"]) > 0:
    count += int(current_location["tags"])
  return count

# ----------------------------------------------------------------

pid = 0
if "startnode" in hmc:
  pid = hmc["startnode"]
current_location = {}
response = ""
gl_count = 0


while True:
  if response == "QUIT":
    break
  if gl_count >= 10:
    break
  pid = update(hmc, current_location, pid, response)
  current_location = find_current_location(hmc, pid)
  render(hmc, current_location)
  gl_count = count_moves(gl_count)
  print(gl_count)
  response = get_input()
print("Thanks for playing!")
print("Your total action count was: {}".format(str(gl_count)))