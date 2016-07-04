while True:
    try:
        n = raw_input()
        print int(n)
    except EOFError:
        break
