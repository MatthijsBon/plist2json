# Import json & plistlib
try:
    import json
    print("running with json...")
except ImportError:
    print 'Import of json not successful'

try:
    import plistlib as pl
    print("running with plistlib...")
except ImportError:
    print 'Import of plistlib not successful'

# Specify input file
infile = raw_input("Specifiy name of .plist file:\n")
infile = infile.split(".")[0]
plist = pl.readPlist('{}.plist'.format(infile))

# Create dictionary
jsondict = {}
for dct in plist:
    jsondict[dct['shortcut']] = dct['phrase']

# Write to .json file
try:
    with open("{}.json".format(infile), 'w') as outfile:
        json.dump(jsondict, outfile, indent=4)
    print "{}.plist succesfully written to {}.json".format(infile, infile)
except:
    print 'Failed, check if plist if formatted correctly'
