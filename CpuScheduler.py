"""
CPU Scheduler

Given a current CPU schedule and a list of incoming processes, return
whether each incoming process can be scheduled without overlapping the
existing workload. If a process fits, it is added to the schedule.

Time: O(N * M)
Space: O(M)
"""

def jobsThatCanBeScheduled(currentSchedule, incomingProcesses):
    normalizedSchedule = [convertToMinutes(job) for job in currentSchedule]
    results = []

    for process in incomingProcesses:
        incoming = convertToMinutes(process)

        if hasOverlap(incoming, normalizedSchedule):
            results.append(False)
        else:
            results.append(True)
            normalizedSchedule.append(incoming)

    return results


def convertToMinutes(scheduleItem):
    start = toMinutes(scheduleItem[0])
    end = toMinutes(scheduleItem[1])
    return [start, end]


def toMinutes(timeString):
    hours, minutes = map(int, timeString.split(":"))
    return hours * 60 + minutes


def hasOverlap(process, currentSchedule):
    start, end = process

    for existingStart, existingEnd in currentSchedule:
        if start < existingEnd and end > existingStart:
            return True

    return False


if __name__ == "__main__":
    currentSchedule = [["10:00", "11:00"], ["14:00", "16:00"], ["23:00", "23:30"]]
    incomingProcesses = [["11:00", "11:30"], ["12:00", "15:00"], ["11:15", "13:43"], ["17:00", "18:40"]]
    print(jobsThatCanBeScheduled(currentSchedule, incomingProcesses))
