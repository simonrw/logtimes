from dataclasses import dataclass
from datetime import datetime, timedelta
from dateutil.parser import ParserError, parse as parse_date
import argparse

@dataclass(frozen=True)
class State:
    start: datetime
    last: datetime


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile", type=argparse.FileType("r"), default="-")
    args = parser.parse_args()

    state: State | None = None
    for line in args.infile:
        line = line.strip()

        def no_time_log():
            print(f"? ? {line}")

        try:
            d = line.split()[0]
        except IndexError:
            no_time_log()
            continue

        try:
            dt = parse_date(d)
        except ParserError:
            no_time_log()
            continue
        if not dt:
            no_time_log()
            continue

        if state is None:
            state = State(start=dt, last=dt)

        delta_from_last = (dt - state.last).total_seconds()
        delta_from_start = (dt - state.start).total_seconds()
        print(f"{delta_from_last:.2f}\t{delta_from_start:.2f}\t{line}")

        # update persisted state
        state = State(start=state.start, last=dt)
