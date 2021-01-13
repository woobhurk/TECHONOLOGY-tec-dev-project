# encoding: utf-8

from random import Random
from collections import OrderedDict
from typing import *

class WeightRandom():
    """- 按照权重来生成随机数。
    """
    # 需要使用有序的 dict 来保存
    valueWeightMap: OrderedDict[Any, float] = OrderedDict()
    random: Random = Random()

    def __init__(self) -> None:
        super().__init__()
        pass

    def addWeight(self, value: Any, weight: float) -> Any:
        """- 添加数值对应的权重。

        - param
            - `value`：数值。
            - `weight`：权重。
        - return：对象自身。
        """
        lastWeight: float = self.__getLastWeight()
        newWeight: float = lastWeight + weight
        self.valueWeightMap[value] = newWeight
        return self

    def addWeightList(self, weightList: List[tuple]) -> Any:
        """- 添加多个权重。

        - param
            - `weightList`：存放 `tuple` 的 `List`，`tuple` 是一个二元组，存的分别是值、权重。
        - return：对象自身。
        - 示例：
        ```python
        weightList: List[tuple] = [(1, 0.2), (2, 0.5), (3, 0.3)]
        WeightRandom().addWeightList(weightList)
        ```
        """
        for valueWeight in weightList:
            if len(valueWeight) < 2:
                continue
            value: Any = valueWeight[0]
            weight: float = valueWeight[1]
            lastWeight: float = self.__getLastWeight()
            newWeight: float = lastWeight + weight
            self.valueWeightMap[value] = newWeight
        return self

    def nextValue(self) -> Any:
        """- 获取下一个随机值。

        - return：按照权重取的随机值。
        """
        lastWeight: float = self.__getLastWeight()
        randWeight: float = self.random.random() * lastWeight
        fetchedValue: Any = None
        for (value, weight) in self.valueWeightMap.items():
            if randWeight < weight:
                fetchedValue = value
                break
        return fetchedValue

    def __getValueList(self) -> List[Any]:
        """- 获取值列表。

        - return：已添加的所有值的 `List`。
        """
        return list(self.valueWeightMap.keys())

    def __getWeightList(self) -> List[float]:
        """- 获取权重列表。

        - return：已添加的所有经过累加的权重的 `List`。
        """
        return list(self.valueWeightMap.values())

    def __getLastWeight(self) -> float:
        """- 获取最后一个权重。

        - return：最后一个添加进去的经过累加的权重值。
        """
        weightList: List[float] = self.__getWeightList()
        return (0.0 if len(weightList) == 0 else weightList[-1])


class ModuleTest():
    def __init__(self) -> None:
        super().__init__()

    def main(self) -> None:
        w: WeightRandom = WeightRandom()
        w.addWeight(1, 0.1).addWeight(2, 0.2) \
            .addWeight(3, 0.2).addWeight(4, 0.15) \
            .addWeight(5, 0.15).addWeight(6, 0.05) \
            .addWeightList([(7, 0.05), (8, 0.1)])
        countMap: Dict[int, int] = {}
        for i in range(10000):
            value: int = w.nextValue()
            countMap[value] = countMap.get(value, 0) + 1
        print(countMap)


if __name__ == "__main__":
    ModuleTest().main()
