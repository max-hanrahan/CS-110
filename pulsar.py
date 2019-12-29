"""
 *****************************************************************************
   FILE:        pulsar.py

   AUTHOR:      Max Hanrahan

   ASSIGNMENT:  Pulsar

   DATE:        11/12/2019 (I AM USING MY EXTENSION)

   DESCRIPTION: Given a list of pulsar data, parse the data appropriately and
   run experiments that print superlatives (such as oldest, closest, and most
   recently discovered) to the console as well as all of the data associated 
   with that pulsar. Testing is accomlished in the file testing_pulsar.py

 *****************************************************************************
"""
#introuduce some global constants necessary for dimensional analysis
LY_PER_PARSEC = 3.26156 # obtained via google calculator
SPEED_CAMRY = 120 # assumed for the project
C_IN_MILES = 186282.397 # obtained by google calculator
MILES_PER_LY = 5878625373183.6 # obtained via google calculator
DAYS_PER_YEAR = 365.25 # common knowledge

class Pulsar:
    def __init__(self, name, parameters):
        '''The Pulsar construct, name is a string, param is a 15-element list'''

        self._name = name
        self._px = parameters[0]
        self._elong = parameters[1]
        self._elat = parameters[2]
        self._pmelong = parameters[3]
        self._pmelat = parameters[4]
        self._Gl = parameters[5]
        self._Gb = parameters[6]
        self._ZZ = parameters[7]
        self._XX = parameters[8]
        self._YY = parameters[9]
        self._assoc = parameters[10]
        self._disc = parameters[11]
        self._type = parameters[12]
        self._nglt = parameters[13]
        self._age = parameters[14]

        # introduce attributes for distance that return * when / is impossible
        if self._px != '*':
            self._distance_parsec = 1000 / float(self._px)
        else:
            self._distance_parsec = '*' # a nonsense placeholder
        if self._distance_parsec != '*':
            self._distance_ly = self._distance_parsec * LY_PER_PARSEC
        else:
            self._distance_ly = '*' # a nonsense placeholder
    
    def __str__(self):
        '''String method for when a pulsar is printed'''

        return 'name: ' + str(self._name) + '\n' + \
        'parallax: ' + str(self._px) + '\n' + \
        'ecliptic_longitude: ' + str(self._elong) + '\n' + \
        'ecliptic_latitude: ' + str(self._elat) + '\n' + \
        'motion_longitude: ' + str(self._pmelong) + '\n' + \
        'motion_latitude: ' + str(self._pmelat) + '\n' + \
        'galactic_longitude: ' + str(self._Gl) + '\n' + \
        'galactic_latitude: ' + str(self._Gb) + '\n' + \
        'galactic_ZZ: ' + str(self._ZZ) + '\n' + \
        'galactic_XX: ' + str(self._XX) + '\n' + \
        'galactic_YY: ' + str(self._YY) + '\n' + \
        'associations: ' +str(self._assoc) + '\n' + \
        'discovery_date: ' + str(self._disc)+ '\n' + \
        'pulsar_type: ' + str(self._type) + '\n' + \
        'glitches_num: ' + str(self._nglt) + '\n' + \
        'age: ' + str(self._age)

    # introduce getter for every attribute passed above
    def get_name(self):
        return self._name

    def get_px(self):
        return self._px

    def get_elong(self):
        return self._elong

    def get_elat(self):
        return self._elat

    def get_pmelong(self):
        return self._pmelong

    def get_pmelat(self):
        return self._pmelat

    def get_Gl(self):
        return self._Gl

    def get_Gb(self):
        return self._Gb

    def get_ZZ(self):
        return self._ZZ

    def get_XX(self):
        return self._XX

    def get_YY(self):
        return self._YY

    def get_assoc(self):
        return self._assoc

    def get_disc(self):
        return self._disc

    def get_type(self):
        return self._type

    def get_nglt(self):
        return(self._nglt)

    def get_age(self):
        if self._age != '*':
            return self._age
        return 0 # a silly placeholder value that won't mess with experiments

    def get_distance_parsec(self):
        if self._distance_parsec != '*':
            return float(self._distance_parsec)
        return 9999999 # a silly placeholder value that won't mess w/ exper's

    def get_distance_ly(self):
        if self._distance_ly != '*':
            return float(self._distance_ly)
        return 9999999 # a silly placeholder value that won't mess with exper's

def main():
    '''method to run the main sequence of the program'''

    #make a list and dictionary of pulsars
    pulsar_data = []
    pulsar_dictionary = {}

    # open the file data.csv
    file = 'data.csv'
    with open(file) as datafile:
        # skip file header
        # skip file 2nd header
        datafile.readline()
        datafile.readline()

        #line is called 'placeholder' so as not to be referenced pre-assignment
        line = "placeholder"
        counter = 0

        while line:
            line = datafile.readline()
            counter += 1

            # skips the special 512th pulsar and parses every non-blank line
            if counter == 512:
                line = datafile.readline()
            if line != '':
                pulsar = parse_line(line)

                # add the pulsar object to the list pulsar_data
                pulsar_data.append(pulsar)

                # add the pulsar object to the dictionary pulsar_dictionary
                pulsar_dictionary[pulsar.get_name()] = pulsar

    datafile.close()

    # print the number of Pulsar objects created 
    print('Number of pulsars:', len(pulsar_data))

    # find oldest pulsar (print data)
    oldest_star = pulsar_data[0]
    for star in pulsar_data:
        if float(star.get_age()) > float(oldest_star.get_age()):
            oldest_star = star
    print('Data for the oldest star:', '\n', oldest_star, '\n')

    # find most recently discovered pulsar (print data)
    newest_disc = pulsar_data[0]
    for star in pulsar_data:
        if star.get_disc() > newest_disc.get_disc():
            newest_disc = star
    print('Data for most recently-discovered pulsar:', '\n', newest_disc, '\n')
    
    # find closest pulsar to us (print data)
    closest_star = pulsar_data[0]
    for star in pulsar_data:
        if star.get_distance_parsec() < closest_star.get_distance_parsec():
            closest_star = star
    print('Data for closest star:', '\n', closest_star, '\n')

    # find distance to closest pulsar in PC
    print('This closest star is', closest_star.get_distance_parsec(), 
        'parsec from us')

    # find distance closest pulsar in ly
    print('or', closest_star.get_distance_ly(), 'ly from us')

    # find how much time it would take to travel to the nearest
    # pulsar in a Toyota Camry ~120 miles/hour (print data in days)
    print("It would take a Toyota Camry traveling 120MPH", 
        int(closest_star.get_distance_ly() * MILES_PER_LY / SPEED_CAMRY / 24), 
        "days to get there")

    # and then in the speed of light ~300000 kmph (print data in days)
    # I converted light-years to light days, but light days does technically
    # represent a unit of time
    print('At the speed of light, that would take', 
        int(closest_star.get_distance_ly() * DAYS_PER_YEAR), 'days')

    # find the number of pulsars that are within 1 light-years
    num_within_1_ly = 0
    for star in pulsar_data:
        if star.get_distance_parsec() != -1 and star.get_distance_parsec() < 1:
            num_within_1_ly += 1
    print("Pulsars within 1 ly:", num_within_1_ly)

    # count the number of pulsars that are of type RRAT
    rrat_num = 0
    for star in pulsar_data:
        if star.get_type() == 'RRAT':
            rrat_num += 1
    print('There are ' + str(rrat_num) + ' pulsars of type RRAT')

def parse_line(line):
    '''takes a line from the file and creates a Pulsar object
    and returns the Pulsar object'''

    tokens = line.split(',')    #tokenize the line

    # Jack Dilligent suggested creating the Pulsar object this way
    name = tokens[1]
    parameters = tokens[2:]
    return Pulsar(name, parameters)    

# calls the main method
if __name__ == '__main__':
    main()
