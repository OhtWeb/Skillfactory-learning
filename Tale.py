coworkers = ['Cat', 'Dog', 'Goose', 'Mouse', 'Cow']
print(f'There was a little farm, on which were living {", ". join(coworkers[0: -1])}, and {coworkers[-1]}')
coworkers.append('Sheep')
print('One day came also Sheep')
coworkers.insert(1, 'Duck')
print('And later came Duck')
if 'Goose' in coworkers:
    print('Goose and others were working hard')
else:
    print('Goose not works')
if 'Cat' in coworkers:
    print(f'So they were living all {len(coworkers)} together until Cat ate Mouse')
    coworkers.remove('Mouse')
else:
    print('Mouse sleeps well')
if 'Mouse' in coworkers:
    print('Mouse sleeps well')
else:
    coworkers.remove('Cat')
    print('Dog was angry because of Mouse and drove away Cat')
if 'Cat' not in coworkers:
    coworkers.insert(0, 'Rat')
    print('While Cat was away, came a rat')
else:
    print('Cat stays on guard')
while 'Rat' in coworkers:
    coworkers.append('Rat')
    print('And another rat')
    if coworkers.count('Rat') >= 12:
        break
coworkers.remove('Duck')
coworkers.remove('Goose')
coworkers.remove('Cow')
print('Rats were very arrogant, they scared Duck, Goose and Cow, so they moved out.')
coworkers.append('Cat')
print('Dog repented and called Cat back.')
coworkers = [x for x in coworkers if x != 'Rat']
print('Cat ate all rats.')
print(f'But after it on farm was left only {len(coworkers)} coworkers: {", ".join(coworkers)}')