import csv

def file_reader(filename):
    trades = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            trades.append({
                'Date': row['Date'],
                'PNL': int(row['PNL']),
                'Psychology': row['Psychology'],
                'Trades taken': int(row['Trades taken']),
                'Setup': row['Setup'],
                'Side': row['Side']
            })
    return trades


def file_analyzer(trades):
    user_filter = input('Which filter do you want? ')

    # Good Psych
    results_integer_good_psychology = 0
    final_pnl_good = 0
    trades_good = 0

    # Bad Psych
    results_integer_bad_psychology = 0
    final_pnl_bad = 0
    trades_bad = 0

    # Breakout Setup
    results_integer_breakout = 0
    final_pnl_breakout = 0
    trades_breakout = 0

    # Reversal Setup
    results_integer_reversal = 0
    final_pnl_reversal = 0
    trades_reversal = 0

    for row in trades:
        if user_filter == 'Psychology':
            if row['Psychology'] == 'Good':
                results_integer_good_psychology += 1
                final_pnl_good += row['PNL']
                trades_good += row['Trades taken']

            elif row['Psychology'] == 'Bad':
                results_integer_bad_psychology += 1
                final_pnl_bad += row['PNL']
                trades_bad += row['Trades taken']

        elif user_filter == 'Setup':
            if row['Setup'] == 'Breakout':
                results_integer_breakout += 1
                final_pnl_breakout += row['PNL']
                trades_breakout += row['Trades taken']

            elif row['Setup'] == 'Reversal':
                results_integer_reversal += 1
                final_pnl_reversal += row['PNL']
                trades_reversal += row['Trades taken']

    if user_filter == 'Psychology':
        avg_pnl_good = 0
        avg_pnl_bad = 0

        if trades_good > 0:
            avg_pnl_good = final_pnl_good / trades_good

        if trades_bad > 0:
            avg_pnl_bad = final_pnl_bad / trades_bad

        reading_psychology = {
            'Good --> Count': results_integer_good_psychology,
            'Total PNL of good': final_pnl_good,
            'Average PNL of good': avg_pnl_good,
            'Bad --> Count': results_integer_bad_psychology,
            'Total PNL of bad': final_pnl_bad,
            'Average PNL of bad': avg_pnl_bad
        }

        return reading_psychology

    elif user_filter == 'Setup':
        avg_pnl_breakout = 0
        avg_pnl_reversal = 0

        if trades_breakout > 0:
            avg_pnl_breakout = final_pnl_breakout / trades_breakout

        if trades_reversal > 0:
            avg_pnl_reversal = final_pnl_reversal / trades_reversal

        reading_setup = {
            'Breakout --> Count': results_integer_breakout,
            'Total PNL of Breakout': final_pnl_breakout,
            'Average PNL of Breakout': avg_pnl_breakout,
            'Reversal --> Count': results_integer_reversal,
            'Total PNL of Reversal': final_pnl_reversal,
            'Average PNL of Reversal': avg_pnl_reversal
        }

        return reading_setup

    else:
        return {'Error': 'Invalid filter choice'}


def main():
    reading_file = file_reader('filename.csv')
    analyzed = file_analyzer(reading_file)
    print(analyzed)


main()
