import time

class TrafficLight:
    __color: dict = dict(красный=4, желтый=2, зеленый=3)

    def running(self):
        for key, value in self.__color.items():
            print(f'{key} {value} сек')
            time.sleep(self.__color[key])



if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()