import xml.etree.ElementTree as ET

tree = ET.parse('Organisational Structure As At Date.yxwz')
root = tree.getroot()

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
        currentNode = str(origin.get('ToolID'))
        if currentNode in self.nodesDone:
            self.updateNode(currentNode, destination)
        else:
            self.newNode(currentNode, destination)
            
    def newNode(self, currentNode, destination):
        #build new node
        self.nodes[currentNode] = node()
        self.nodes[currentNode].origin = currentNode
        self.nodes[currentNode].destination = []
        self.nodes[currentNode].destination.append(destination)
        
        for o in root.iter('Connection'):
            self.parseConnection(o)
        
        annotation = root.findall(".//Node/[@ToolID='1']/Properties/Annotation/DefaultAnnotationText")
        self.nodes[currentNode].annotation = annotation[0].text
        self.nodesDone.append(currentNode)
    def updateNode(self, currentNode, destination):
        #amend existing node
        self.nodes[currentNode].destination.destination.append(destination)

for n, v in nodes.items():
    print("ORIGIN NODE: "+v.origin)
    #print("ANNOTATION: "+str(v.annotation[:50]))
    print("\tDESTINATION NODES: "+v.destination)