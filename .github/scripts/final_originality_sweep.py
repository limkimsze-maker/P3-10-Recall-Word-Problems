from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')

# Remove unused remnants from earlier person/day/item stories.
s=re.sub(r"function makeRunQuestion\(\)\{const names=\[.*?\],dayPairs=\[.*?\],name=pick\(names\),\[day1,day2\]=pick\(dayPairs\),tue=", "function makeRunQuestion(){const tue=", s, count=1)
s=s.replace("function makeContainerQuestion(){const item=pick(['rice','flour','sugar']),content=", "function makeContainerQuestion(){const content=")

# Make the final comparison problem visibly different from a ribbon/textbook example.
s=s.replace('function ribbonSVG(', 'function markerStripSVG(')
s=s.replace('ribbonSVG(a,extra)', 'markerStripSVG(a,extra)')
s=s.replace('function makeRibbonQuestion()', 'function makeMarkerStripQuestion()')
s=s.replace('makeRibbonQuestion()', 'makeMarkerStripQuestion()')
s=s.replace('Streamer A', 'Marker strip A').replace('Streamer B', 'Marker strip B')
s=s.replace('How long are the Sports Fiesta streamers?', 'How long are the two lane-marker strips?')
s=s.replace('Streamer A is <b>${a} cm</b> long. Marker strip B is <b>${extra} cm</b> longer than Marker strip A.<br>(a) How long is Marker strip B?<br>(b) What is the total length of both streamers?', 'A blue lane-marker strip is <b>${a} cm</b> long. A yellow lane-marker strip is <b>${extra} cm</b> longer than the blue strip.<br>(a) How long is the yellow strip?<br>(b) What is the total length of both marker strips?')
s=s.replace('The total length of both streamers is', 'The total length of both marker strips is')
s=s.replace('Then ${a} + ${b} = ${total}.', 'The yellow strip is ${b} cm. Then ${a} + ${b} = ${total} cm altogether.')

p.write_text(s,encoding='utf-8')
