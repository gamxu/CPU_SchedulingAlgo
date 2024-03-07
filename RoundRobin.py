def rr(processes, time_quantum):
    wait_time = 0
    turnaround_time = []
    completed_order = []
    gantt_chart = []
    ready_queue = []
    waiting_time = []

    for process in processes:
        ready_queue.append((process[0], process[1]))

    while ready_queue:
        current_process = ready_queue.pop(0)
        gantt_chart.append((current_process[0], wait_time))

        if current_process[1] > time_quantum:
            current_process = list(current_process)
            current_process[1] -= time_quantum
            current_process = tuple(current_process)
            wait_time += time_quantum
            ready_queue.append(current_process)
        else:
            wait_time += current_process[1]
            turnaround_time.append(wait_time)
            completed_order.append(current_process[0])

    for i in range(len(processes)):
      waiting_time.append(turnaround_time[i] - processes[completed_order[i] - 1][1])

    print("Round Robin:")
    print("Gantt Chart:", gantt_chart)
    print("Completion Time:", wait_time)
    print("Turnaround Time:", turnaround_time, "Avg:", sum(turnaround_time)/len(turnaround_time))
    print("Waiting Time:", waiting_time, "Avg:", sum(waiting_time)/len(waiting_time))

