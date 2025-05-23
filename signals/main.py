import ast

def decode_signals(days):
    code_poss = {}
    event_poss = {}

    for codes, events in days:
        for code in codes:
            if code not in code_poss:
                code_poss[code] = set(events)
            else:
                code_poss[code] &= set(events)
        for event in events:
            if event not in event_poss:
                event_poss[event] = set(codes)
            else:
                event_poss[event] &= set(codes)

    solved = {}
    while len(solved) < len(code_poss):
        progress = False

        for code, poss in code_poss.items():
            if code in solved:
                continue
            if len(poss) == 1:
                event = next(iter(poss))
                solved[code] = event
                for other_code in code_poss:
                    if other_code != code:
                        code_poss[other_code] -= {event}
                progress = True
        if not progress:
            for event, poss_codes in event_poss.items():
                unsolved_codes = [c for c in poss_codes if c not in solved]
                if len(unsolved_codes) == 1:
                    code = unsolved_codes[0]
                    solved[code] = event
                    for other_code in code_poss:
                        if other_code != code:
                            code_poss[other_code] -= {event}
                    progress = True
        if not progress:
            break

    return solved

def main():
    with open("input.txt") as f:
        days = ast.literal_eval(f.read())
    decoded = decode_signals(days)
    print("{")
    for code, event in sorted(decoded.items()):
        print(f'    "{code}": "{event}",')
    print("}")

if __name__ == "__main__":
    main()