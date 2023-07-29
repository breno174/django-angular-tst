class ConsumerUrlSerializer:
    @staticmethod
    def create_path_by_body(data):
        construtor = "from={}&to={}&width={}&weight={}&height={}&length={}&insurance_value={}&services=1,2,17,28,29,30,31,3,4,27,10,12,15,16,19,20,12,22".format(
            data["from"],
            data["to"],
            data["width"],
            data["weight"],
            data["height"],
            data["length"],
            data["insurance_value"],
        )

        return construtor
