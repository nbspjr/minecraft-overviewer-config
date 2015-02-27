# This is a sample config file, meant to give you an idea of how to format your
# config file and what's possible.

# Define the path to your world here. 'My World' in this case will show up as
# the world name on the map interface. If you change it, be sure to also change
# the referenced world names in the render definitions below.
worlds['Flo'] = "/home/minecraft/minecraft-server/Flo"

# Define where to put the output here.
outputdir = "/var/www/minecraft-overviewer"

# This is an item usually specified in a renders dictionary below, but if you
# set it here like this, it becomes the default for all renders that don't
# define it.
# Try "smooth_lighting" for even better looking maps!
rendermode = "smooth_lighting"

# user-defined markers
static_markers = [
	{'id':'p_home', 'x':-168, 'y':64, 'z':198, 'name':'Hedgehog\'s Residence'},
	{'id':'p_home', 'x':251, 'y':65, 'z':363, 'name':'WTF\'s Landingfield'},
	{'id':'p_home', 'x':-1020, 'y':65, 'z':442, 'name':'Jezzy\'s Cottage'},
	{'id':'p_home', 'x':-345, 'y':65, 'z':-135, 'name':'Thief\'s Vov4eg Hideout'},

	{'id':'p_portal', 'x':59306, 'y':67, 'z':13450},
	{'id':'p_portal', 'x':7657, 'y':67, 'z':16323},
	{'id':'p_portal', 'x':-9305, 'y':67, 'z':384},
	{'id':'p_portal', 'x':-979, 'y':67, 'z':481, 'name':'Deep underground portal'},
	]

# a trick to recognize names for players without legit Minecraft
global players
players = {
	'id1': 'hedgehog',
	'id2': 'WTF',
	'id3': 'vovan4eg',
	'id4': 'Jezzebel',
	'id5': 'Calcelmo',
}

# icons for markers
global icons
icons = {
	'portal': '/custom_icons/regroup.png',
	'home': '/custom_icons/home-2.png',
	'steve': 'http://overviewer.org/avatar/none',
}

def playerIcons(poi):
	if poi['id'] == 'Player':
		poi['icon'] = icons['steve']
		if poi['EntityId'] in players:
			return "Last known location for %s" % players[poi['EntityId']]
		else:
			return "Last known location for... Err... Someone?"


def playerHomes(poi):
	if poi['id'] == 'p_home':
		if 'icon' not in poi:
			poi['icon'] = icons['home']
		return poi['name']


def filterPortals(poi):
	if poi['id'] == 'p_portal':
		if 'icon' not in poi:
			poi['icon'] = icons['portal']
		if 'name' in poi:
			return poi['name']
		else:
			return 'Portal'


# let the overview tool know what to render
renders["default"] = {
	'world': 'Flo',
	'title': 'A place like no other',
	'manualpois': static_markers,
	'markers': [
		dict(name="Players", filterFunction=playerIcons),
		dict(name='Homes', filterFunction=playerHomes),
		dict(name='Portals', filterFunction=filterPortals),
	],
}

#renders["default_nether"] = {
#        'world': 'Flo',
#        'title': 'Hell',
#	"rendermode": nether_smooth_lighting,
#	"dimension": "nether",
#	'markers': [dict(name="Players", filterFunction=playerIcons),],
#}


# This example is the same as above, but rotated
#renders["render2"] = {
#        'world': 'My World',
#        'northdirection': 'upper-right',
#        'title': 'Upper-right north direction',
#}

# Here's how to do a nighttime render. Also try "smooth_night" instead of "night"
#renders["render3"] = {
#        'world': 'My World',
#        'title': 'Nighttime',
#        # Notice how this overrides the rendermode default specified above
#        'rendermode': 'night',
#}

