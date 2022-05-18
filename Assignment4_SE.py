
from matplotlib import pyplot as plt

def showComparison(textfile1, textfile2):
    with open(textfile1) as f:
        lines = f.readlines()
        rain10YrAgo = [round(float(line.split()[1]),2) for line in lines]

    with open(textfile2) as g:
        lines = g.readlines()
        rainNow = [round(float(line.split()[1]),2) for line in lines]

    with open(textfile1) as f:
        lines = f.readlines()
        cityName = [line.split()[0] for line in lines]

    plt.figure(figsize = (10,8))
    plt.gcf().subplots_adjust(bottom=0.25)
    plt.plot(cityName, rainNow,label = "Current Year")
    plt.plot(cityName, rain10YrAgo,label = "10 Years Ago")

    plt.title("Rainfall in " + str(len(cityName)) + " Cities")
    plt.ylabel("Inches of Rain")
    plt.xlabel("City Name")
    plt.xticks(rotation = 90)
    plt.legend()
    plt.savefig('Comparison Plot.png',dpi=300, bbox_inches='tight')
    plt.show()

def sepPlots(textfile1, textfile2):
    with open(textfile1) as f:
        lines = f.readlines()
        rain10YrAgo = [round(float(line.split()[1]),2) for line in lines]
        indexCity = rain10YrAgo.index(min(rain10YrAgo))
        indexMax = rain10YrAgo.index(max(rain10YrAgo))
        
    with open(textfile2) as g:
        lines = g.readlines()
        rainNow = [round(float(line.split()[1]),2) for line in lines]
        minNowIndex = rainNow.index(min(rainNow))
        maxNowIndex = rainNow.index(max(rainNow))

    with open(textfile1) as f:
        lines = f.readlines()
        cityName = [line.split()[0] for line in lines]

    fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(16,7))
    plt.gcf().subplots_adjust(bottom=0.25)
    ax[0].bar(cityName, rain10YrAgo, color = "pink")
    ax[0].scatter(indexCity, min(rain10YrAgo),c='blue')
    ax[0].scatter(indexMax, max(rain10YrAgo),c='blue')
    ax[0].annotate('Min = %.1f in, in %s' %(min(rain10YrAgo),cityName[indexCity]),
         xy = (indexCity+1, min(rain10YrAgo)), xytext = (.5,.5),
         textcoords = 'offset points',
        bbox = dict(boxstyle = "larrow, pad = .4", fc = "cyan", ec = "b", lw = .5))
    ax[0].annotate('Max = %.1f in, in %s' %(max(rain10YrAgo),cityName[indexMax]),
         xy = (indexMax+1, max(rain10YrAgo)), xytext = (.5,.5),
         textcoords = 'offset points',
         bbox = dict(boxstyle = "larrow, pad = .4", fc = "cyan", ec = "b", lw = .5)
                   )
    ax[0].set_xlabel('City Name')
    ax[0].set_ylabel('Inches of Rain')
    ax[0].xaxis.set_ticks(cityName)
    ax[0].set_xticklabels(cityName, rotation = 65, ha = 'right')
    ax[0].set_title("Rainfall in " + str(len(cityName)) + " Cities 10 Years Ago")

    ax[1].bar(cityName, rainNow)
    ax[1].scatter(minNowIndex, min(rainNow),c='r')
    ax[1].scatter(maxNowIndex, max(rainNow),c='r')
    ax[1].annotate('Min = %.1f in, in %s' %(min(rainNow),cityName[minNowIndex]),
       xy = (minNowIndex+1, min(rainNow)), xytext = (.5,.5),
       textcoords = 'offset points',
       bbox = dict(boxstyle = "larrow, pad = .4", fc = "cyan", ec = "b", lw = .5))
    ax[1].annotate('Max = %.1f in, in %s' %(max(rainNow),cityName[maxNowIndex]),
       xy = (maxNowIndex+1, max(rainNow)), xytext = (.5,.5),
        textcoords = 'offset points',
         bbox = dict(boxstyle = "larrow, pad = .4", fc = "cyan", ec = "b", lw = .5))
    
    ax[1].set_xlabel('City Name')
    ax[1].set_ylabel('Inches of Rain')
    ax[1].set_ylim(0,100)
    ax[1].xaxis.set_ticks(cityName)
    ax[1].set_xticklabels(cityName, rotation=65, ha = 'right')
    ax[1].set_title("Rainfall in " + str(len(cityName)) + " Cities This Year")
    plt.savefig('Two Bar Plots.png',dpi=300, bbox_inches='tight')
    plt.show()


def stackedBar(textfile1, textfile2):
    with open(textfile1) as f:
        lines = f.readlines()
        rain10YrAgo = [round(float(line.split()[1]),2) for line in lines]

    with open(textfile2) as g:
        lines = g.readlines()
        rainNow = [round(float(line.split()[1]),2) for line in lines]
    with open(textfile1) as f:
        lines = f.readlines()
        cityName = [line.split()[0] for line in lines]

    plt.subplots(figsize = (10,8))
    plt.subplots_adjust(bottom = .2)
    plt.bar(cityName, rain10YrAgo, yerr = 1, label = "10 Years Ago")
    plt.bar(cityName, rainNow,yerr = 1, label = "Current Year", bottom = rain10YrAgo)

    plt.title("Rainfall in " + str(len(cityName)) + " Cities")
    plt.ylabel("Inches of Rain")
    plt.xlabel("City Name")
    plt.xticks(rotation = 90)
    plt.legend(bbox_to_anchor= (.25,1.15))
    plt.grid(color = 'gray', linestyle = '--', axis = 'y')
    plt.savefig('Stacked Bar Chart.png',dpi=300, bbox_inches='tight')
    #bbox_inches='tight'
    plt.show()

def main():
    showComparison("rainfallISet1.txt", "rainfallSet2.txt")
    sepPlots("rainfallISet1.txt", "rainfallSet2.txt")
    #stacked Bar shows stacked bar chart (another visualization of the data)
    stackedBar("rainfallISet1.txt", "rainfallSet2.txt")

main()

