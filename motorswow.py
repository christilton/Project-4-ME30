import RPistepper as stp
M1_pins = [17, 27, 10, 9]
with stp.Motor(M1_pins) as M1:
    for i in range(10):               # moves 20 steps,release and wait
        print M1
        M1.move(20)
        M1.release()
        raw_input('enter to execute next step')
