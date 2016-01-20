# Walter Meyer (wgm2110)
# COMS W4111 HW0

import re

data = open("iowa-liquor-sample.csv", "r")
counter = 0

records = data.readlines()
for record in records:
    if re.search('single malt scotch', record, re.IGNORECASE):
        counter += 1
print 'Matches: %d' % counter
data.close()
