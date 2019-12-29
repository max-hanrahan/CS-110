"""
 *****************************************************************************
   FILE:        pulsar.py

   AUTHOR:      Max Hanrahan

   ASSIGNMENT:  Pulsar Tests

   DATE:        11/12/2019 (I AM USING MY EXTENSION)

   DESCRIPTION: All the tests associated with the project pulsar.py.
   I am currently shooting for an A-, as some but not all test files are created
 *****************************************************************************
"""
#get the object class and necessary fundtions from our test file
from pulsar import Pulsar
from pulsar import parse_line

#create a special list of test_pulsar_data that we can iterate through
test_pulsar_data = []

def main():
    '''moves all the data to an accessible list and performs all the tests'''

    pulsar_data = []
    # open the file data.csv
    file = 'pulsar_test_data.csv'
    with open(file) as datafile:
        # skip file header
        # skip file 2nd header
        datafile.readline()
        datafile.readline()

        line = "placeholder"
        counter = 0

        while line:
            line = datafile.readline()
            counter += 1

            if counter == 512:
                line = datafile.readline()
            if line != '':
                pulsar = parse_line(line)

                # add the pulsar object to the list pulsar_data
                test_pulsar_data.append(pulsar)

    # setup 1: the getters of the first object in our list    
    p0 = test_pulsar_data[0]
    name = p0.get_name()
    px = p0.get_px()
    elong = p0.get_elong()

    # we shall then proceed to test a handful of attributes, starting w/get_name
    assert name == 'J0002+6216', "problem with the name getter"
    assert px == '*', 'problem with parallax attribute'
    assert elong == '37.547', 'problem with pme_long attribute'
    print('test 1: passed') 

    #let's choose three more attributes to test, similar to above
    assert p0.get_type() == 'NRAD', 'problem with the type attribute'
    assert p0.get_nglt() == '*', 'problem with nglt attribute'
    assert p0.get_age() == '3.06E+05'
    print('test 2: passed')
    
if __name__ == "__main__":
    main()