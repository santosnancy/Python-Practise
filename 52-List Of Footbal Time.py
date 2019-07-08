def line(text):
    print('=' * 60)
    print(text)
    print('=' * 60)


Soccer = ('Petro De Luanda', 'De Agosto', 'Sagrada Esperanca', 'Desportivo', 'Malanje','Inter Club', 'Benfica', 'Recreativo', 'Asa', 'Petro Do Huambo', 'Porcelana', 'Libolo','United', 'Quizanga', 'Katepa', 'Ritondo', 'Maxinde', 'Canambua')

line(f'The Clubs The Plays On Angolan Soccer First Division Are :\n{Soccer}')
line(f'The 5 Clubs on Top 5 Are\n{Soccer[:5]}')
line(f'The Last 4 Clubs are\n{Soccer[14:]}')
line(f'The All Clubs In Alphabetic Order is:\n{sorted(Soccer)}')
line(f'The Club Find  Asa is on {Soccer.index("Asa")+1}o Position')