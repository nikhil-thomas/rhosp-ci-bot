from datetime import datetime
import yaml

def countDays(d):
    # print(d)
    dObj = datetime.strptime(d, '%Y-%m-%d')
    todayObj = datetime.now()
    todayObj = todayObj.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = dObj - todayObj
    return delta.days

def readConfig(filename):
    with open(filename, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
            return config
        except yaml.YAMLError as exc:
            print(exc)

def generateMessage(config, outputPath):
    with open(outputPath, 'w') as f:
        f.write( ":redhatnew::openshift::pipelines: *RED HAT OPENSHFIT PIPELINES - RELEASE " + c["version"] + '* :redhatnew::openshift::pipelines:\n\n')

        f.write( "*Milestones*\n\n")
        milestones = c["milestones"]
        for key in milestones:
            daysRemaining = countDays(str(milestones[key]))
            f.write(key.title() + ' : ' + str(milestones[key]) + '\n')
            f.write(str(daysRemaining) + ' days left \n\n')

configPath = './next-release.yaml'
outputPath = './release-milestones'

c = readConfig('./next-release.yaml')
generateMessage(c, outputPath)
