# -*- coding: utf-8 -*-
# function to draw the pitch

import matplotlib.pyplot as plt
import numpy as np

# sie of the pitch in yards
pitchLengethX=120
pitchWidthY=80

match_id_required = 69301

file_name=str(match_id_required)+'.json'

import json
with open('../StatsBomb/data/events/'+file_name) as data_file:
    data = json.load(data_file)
    

from pandas.io.json import json_normalize
df = json_normalize(data, sep="_").assign(match_id=file_name[:-5])

shots = df.loc[df['type_name'] == 'Shot'].set_index('id')

from FCPython import createPitch
(fig, ax) = createPitch(pitchLengethX,pitchWidthY,'yards', 'gray')


for i, shot in shots.iterrows():
    x=shot['location'][0]
    y=shot['location'][1]
    
    goal=shot['shot_outcome_name'] == 'Goal'
    team_name=shot['team_name']
    
    circleSize=2
    circleSize=np.sqrt(shot['shot_statsbomb_xg']*15)
    
    if (team_name==home_team_required):
        if goal:
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")
            plt.text((x+1),pitchWidthY-y+1,shot['player_name']) 
        else:
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")     
            shotCircle.set_alpha(.2)
    elif (team_name==away_team_required):
        if goal:
            shotCircle=plt.Circle((pitchLengthX-x,y),circleSize,color="blue") 
            plt.text((pitchLengthX-x+1),y+1,shot['player_name']) 
        else:
            shotCircle=plt.Circle((pitchLengthX-x,y),circleSize,color="blue")      
            shotCircle.set_alpha(.2)
    ax.add_patch(shotCircle)
    
    
plt.text(5,75,away_team_required + ' shots') 
plt.text(80,75,home_team_required + ' shots') 
     
fig.set_size_inches(10, 7)
fig.savefig('Output/shots.pdf', dpi=100) 
plt.show()