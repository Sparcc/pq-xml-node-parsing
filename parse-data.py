import xml.etree.ElementTree as ET

tree = ET.parse('Organisational Structure As At Date.yxwz')
root = tree.getroot()

#nodes = root.findall(".//*[@ToolID='1']")
#nodes = root.findall(".//Node")
#allConnections = connections = root.findall(".//*Connection/")
#i = 1
#for c in allConnections:
#    connections = root.findall(".//Connection/*[@ToolID='"+str(i)+"']")
#    i+=1
#conOrig = root.findall(".//*Connection/Origin")
#conDest = root.findall(".//*Connection/Destination")
#cons = root.findall(".//Connections/Connection")

nodesDone = []
'''
node = {}
for o in root.iter('Connection'):
    con = list(o)
    origin=con[0]
    destination=con[1]
    currentNodeString = str(origin.get('ToolID'))
    if currentNodeString in nodesDone:
        #amend existing node
        node[currentNodeString]['destination'] += ", " +str(destination.get('ToolID'))
    else:
        #build new node
        node[currentNodeString] = {}
        node[currentNodeString]['origin'] = currentNodeString
        node[currentNodeString]['destination'] = str(destination.get('ToolID'))
        nodesDone.append(currentNodeString)
'''
#annotation = root.findall(".//Node/[@ToolID='1']/Properties/Annotation/DefaultAnnotationText")
#print(annotation[0].text)
    

class node:
    origin = ""
    destination = ""
    annotation = ""

nodes = {}
for o in root.iter('Connection'):
    con = list(o)
    origin=con[0]
    destination=con[1]
    currentNodeString = str(origin.get('ToolID'))
    if currentNodeString in nodesDone:
        #amend existing node
        nodes[currentNodeString].destination += ", " +str(destination.get('ToolID'))
    else:
        #build new node
        nodes[currentNodeString] = node()
        nodes[currentNodeString].origin = currentNodeString
        nodes[currentNodeString].destination = str(destination.get('ToolID'))
        annotation = root.findall(".//Node/[@ToolID='"+currentNodeString+"']/Properties/Annotation/DefaultAnnotationText")
        nodes[currentNodeString].annotation = annotation[0].text
        nodesDone.append(currentNodeString)

#print(nodesDone)


for n, v in nodes.items():
    print("ORIGIN NODE: "+v.origin)
    try:
        print("ANNOTATION: "+str(v.annotation[:50]))
    except:
        pass
    print("\tDESTINATION NODES: "+v.destination)
