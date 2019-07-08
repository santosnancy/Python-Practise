phrase = ('carlos', 'Dos' 'Santos', 'nancy', 'Lopes','zulu', 'before', 'humberto', 'marieta')
for lop in phrase:
    print(f'\nIn the Word {lop} has ',end=' ')
    for let in lop:
        if let in 'aeiou':
            print(let,end=' ')
