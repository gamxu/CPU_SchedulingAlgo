def fcfs(processes):
    '''
    Note: This algo is non-preemptive, let arrival_time be 0
    Input: Processes array = [(processID, burstTime)]
    '''
    wait_time = 0
    turnaround_time = []
    waiting_time = []
    gantt_chart = []

    for process in processes:
        gantt_chart.append((process[0], wait_time))
        wait_time += process[1]                     # completion_time = waiting_time + burst_time
        turnaround_time.append(wait_time)           # turnaround_time = completion_time
        waiting_time.append(wait_time - process[1])

    print("FCFS: ")
    print("Gantt Chart:", gantt_chart)
    print("Completion Time:", wait_time)
    print("Turnaround Time:", turnaround_time, "Avg:", sum(turnaround_time)/len(turnaround_time))
    print("Waiting Time:", waiting_time, "Avg:", sum(waiting_time)/len(waiting_time))

