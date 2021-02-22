#calculations
def timer(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    f2 = '{:.3f}'.format(sec)

    #print code laps
    print(f'[Finished in {f2}s]')
