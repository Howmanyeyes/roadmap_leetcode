"""
134. Gas Station
https://leetcode.com/problems/gas-station/description/?envType=study-plan-v2&envId=top-interview-150
"""

"""
There are n gas stations along a circular route, where the amount of gas at the ith station is
gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith
station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas
stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel
around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution,
it is guaranteed to be unique.

По идее, можно решить за О(n^2) если в каждой точке начала пути проверять путь до конца, но
наверняка можно улететь в тайм еррор. С другой стороны, за O(n) мы сразу можем понять, возможен ли 
круг или нет, сравнив сумму в бензе и в стоимости. Пока других решений не вижу - значит попробуем.

Тесткейс с нулями показал что надо делать решение за О(n) и тут варианта 2: либо все нули удалять
потому что они не несут пользы, более того, можно удалять просто все одинаковые числа. Если и это
не поможет, то можно группировать все подряд идущие положительные и подряд идущие отрицательные
числа чтобы еще уменьшить длину списака, однако в таком подходе не ясно когда останавливаться.

Посмотрев на решение, понял что надо было пользоваться условием того что нет смысла проверять все 
т.к. решение точно существует. Таким образом можно за 1 проход смотреть все становки и если бенз
падает ниже 0 то этот определенный отрезок он не будет содержать решения. А если дойдет до конца то
это точно решение. 
"""
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
                
        curernt_gas = 0
        start = 0
        for i in range(len(gas)):
            curernt_gas += gas[i] - cost[i]
            if curernt_gas < 0:
                curernt_gas = 0
                start = i + 1

        return start