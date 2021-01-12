# encoding: utf-8

from collections import OrderedDict
from typing import *
import random as Random

class RandomUtil():
    def __init__(self) -> None:
        super().__init__()


class WeightRandomUtil():
    # 需要使用有序的 dict 来保存
    valueWeightMap: OrderedDict[Any, float] = OrderedDict()

    def __init__(self) -> None:
        super().__init__()
        pass

    def addWeight(self, value: Any, weight: float) -> Any:
        lastWeight: float = self.__getLastWeight()
        newWeight: float = lastWeight + weight
        self.valueWeightMap[value] = newWeight
        return self

    def nextValue(self) -> Any:
        lastWeight: float = self.__getLastWeight()
        randWeight: float = Random.random() * lastWeight
        fetchedValue: Any = None
        for (value, weight) in self.valueWeightMap.items():
            if randWeight < weight:
                fetchedValue = value
                break
        return fetchedValue

    def __getValueList(self) -> List[Any]:
        """获取值列表。
        """
        return list(self.valueWeightMap.keys())

    def __getWeightList(self) -> List[float]:
        """获取权重列表。
        """
        return list(self.valueWeightMap.values())

    def __getLastWeight(self) -> float:
        """获取最后一个权重。
        """
        weightList: List[float] = self.__getWeightList()
        return (0.0 if len(weightList) == 0 else weightList[-1])


class App():
    def __init__(self) -> None:
        super().__init__()

    def main(self) -> None:
        w: WeightRandomUtil = WeightRandomUtil()
        w.addWeight(10, 0.1).addWeight(20, 0.2) \
            .addWeight(30, 0.3).addWeight(40, 0.2) \
            .addWeight(50, 0.15).addWeight(60, 0.05)
        countMap: Dict[int, int] = {}
        for i in range(10000):
            value: int = w.nextValue()
            countMap[value] = countMap.get(value, 0) + 1
        print(countMap)


if __name__ == "__main__":
    App().main()
