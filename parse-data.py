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
    
class nodeParser:
    nodes = {}
    nodesDone = []
    def processData(self):
        for o in root.iter('Connection'):
            self.parseConnection(o)
    def parseConnection(self,o):
        con = list(o)
        origin=str(con[0].get('ToolID'))
        destination=str(con[1].get('ToolID'))
        currentNodeString = str(origin.get('ToolID'))
        
        self.paseNode()
        if currentNodeString in self.nodesDone:
            self.updateNode()
        else:
            self.newNode()
        
    def parseNode(self, 
        
    def newNode(self):
        #build new node
        self.nodes[currentNodeString] = node()
        self.nodes[currentNodeString].origin = currentNodeString
        self.nodes[currentNodeString].destination = destination
        annotation = root.findall(".//Node/[@ToolID='1']/Properties/Annotation/DefaultAnnotationText")
        self.nodes[currentNodeString].annotation = annotation[0].text
        self.nodesDone.append(currentNodeString)
    def updateNode(self):
        #amend existing node
        self.nodes[currentNodeString].destination += ", " + destination


    
#print(nodesDone)


for n, v in nodes.items():
    print("ORIGIN NODE: "+v.origin)
    #print("ANNOTATION: "+str(v.annotation[:50]))
    print("\tDESTINATION NODES: "+v.destination)
