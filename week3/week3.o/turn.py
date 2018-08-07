def greetAgent(first_name, last_name):
    print "%s. %s %s" % (last_name, first_name,last_name)\

def createAgentGreeting(first_name, last_name):
    return "%s. %s %s." %(last_name, first_name, last_name)\

print"Calling greetAgent() function with arguments JaMes, BoNd"
greetAgent("JaMes","BoNd")

print"Calling createAgentGreeting() function with arguments JaMes, BoNd"
p = createAgentGreeting("JaMes","BoNd")
print p.upper()
