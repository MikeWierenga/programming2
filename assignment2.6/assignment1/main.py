from Programming2_week1_3.Reader import Reader
from Programming2_week1_3.Consumer import AverageYear, AverageMonth


def main():
    prod = Reader('dSST.csv')
    cons1 = AverageYear()
    cons2 = AverageMonth()
    prod.add_observer(cons1)
    prod.add_observer(cons2)
    prod.start_reading()


if __name__ == "__main__":
    main()
