from datetime import timedelta
from random import choice, randint

DAYS_OF_WEEK = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
CITIES = ("Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt", "Stuttgart", "Dusseldorf", "Dortmund", "Essen")
MATCH_TYPES = ("yes", "no")


def generate_traffic_data_file(filename):
    with open(filename, "w") as file:
        for day_idx in range(len(DAYS_OF_WEEK)):
            for time_idx in range(288):
                hours = time_idx // 12
                minutes = (time_idx % 12) * 5
                city = choice(CITIES)
                match = choice(MATCH_TYPES)
                vehicles_count = randint(0, 60)
                string = f"{DAYS_OF_WEEK[day_idx]},{hours:02d}:{minutes:02d},{city},{match},{vehicles_count}\n"
                file.write(string)


if __name__ == "__main__":
    generate_traffic_data_file("traffic_data.txt")
