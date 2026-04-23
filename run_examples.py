from BinarySearch import binarySearch
from QuickSort import quickSort
from DijkstrasAlgorithm import dijkstrasAlgorithm
from CpuScheduler import jobsThatCanBeScheduled

print("Binary Search:", binarySearch([1, 3, 5, 7, 9], 7))
print("Quick Sort:", quickSort([5, 1, 9, 2, 7]))
print("Dijkstra:", dijkstrasAlgorithm(0, [
    [[1, 7]],
    [[2, 6], [3, 20], [4, 3]],
    [[3, 14]],
    [[4, 2]],
    [],
    []
]))
print("CPU Scheduler:", jobsThatCanBeScheduled(
    [["10:00", "11:00"], ["14:00", "16:00"], ["23:00", "23:30"]],
    [["11:00", "11:30"], ["12:00", "15:00"], ["11:15", "13:43"], ["17:00", "18:40"]]
))
