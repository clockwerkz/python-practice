def commaCode(arr):
    if len(arr) == 0:
        return ''
    if len(arr) == 1:
        return str(arr[0])
    sentence = ''
    for i in range(0, len(arr)-1):
        sentence += str(arr[i]) + ', '
    sentence += 'and ' + str(arr[-1])
    return sentence

print(commaCode(['cats',4, 2.3,'fish']))
