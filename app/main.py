class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        if 1 <= comfort_class <= 7:
            self.comfort_class = comfort_class
        else:
            raise ValueError("comfort_class should be between 1 and 7")
        if 1 <= clean_mark <= 10:
            self.clean_mark = clean_mark
        else:
            raise ValueError("clean_mark should be between 1 and 10")
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        if 1.0 <= distance_from_city_center <= 10.0:
            self.distance_from_city_center = distance_from_city_center
        else:
            raise ValueError(
                "distance_from_city_center should be between 1.0 and 10.0"
            )
        self.clean_power = clean_power
        if 1.0 <= average_rating <= 5.0:
            self.average_rating = round(average_rating, 1)
        else:
            raise ValueError("average_rating should be between 1.0 and 5.0")
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list) -> float:
        income = 0
        for car in list_of_cars:
            if car.clean_mark < self.clean_power:
                income += round(self.calculate_washing_price(car), 1)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        difference_cleaning = self.clean_power - car.clean_mark
        return (car.comfort_class
                * difference_cleaning
                * self.average_rating
                / self.distance_from_city_center)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        self.average_rating = round(
            (self.average_rating
             * self.count_of_ratings
             + rate)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
