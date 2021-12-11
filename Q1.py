
print("Welcome to TODO APP")

total=int(input("enter no of tasks you want to do"))

incomplete=[]
complete=[]
inprogress=[]

for a in range(1,total+1):

    task=input("enter the task")
    status=int(input("enter no according to status of task"))

    if status==1:
        incomplete.append(task)
    elif status==2:
        complete.append(task)
    elif status==3:
        inprogress.append(task)
    else:
        print("invalid option")

change=int(input("enter option no according to task you want to perform"))


if change==1:
    show=int(input("enter option no according to task you want to see"))
    if show==1:
        for b in incomplete:
            print(b)
    elif show==2:
        for c  in complete:
            print(c)
    elif show==3:
        for d in inprogress:
            print(d)
    else:
        print("invalid option")

elif change==2:
    current_status=int(input("enter current status of task you want to change "))
    updated_status=int(input("enter updated status"))

    if current_status==1:
        for e in range(1,len(incomplete)+1):
            print(e,incomplete[e-1])
        task_to_change=int(input("enter option no of task u want to change"))
        for n in incomplete:
            if incomplete.index(n) == task_to_change-1:
                incomplete.remove(n)
                if updated_status==3:
                    complete.append(n)
                elif updated_status==2:
                    inprogress.append(n)

    elif current_status==2:
        for o in range(1,len(inprogress)+1):
            print(o,incomplete[o-1])
        task_to_change=int(input("enter option no of task u want to see"))
        for p in inprogress:
            if inprogress.index(p)==task_to_change-1:
                incomplete.remove(p)
                if updated_status==1:
                    incomplete.append(p)
                elif updated_status==3:
                    complete.append(p)

    elif current_status==3:
        for q in range(1,len(complete)+1):
            print(q,complete[q-1])
        task_to_change=int(input("enter option no of task u want to see"))
        for r in complete:
            if complete.index(r)==task_to_change-1:
                incomplete.remove(r)
                if updated_status==1:
                    incomplete.append(r)
                elif updated_status==2:
                    inprogress.append(r)


# elif change==3:
#     current_status=int(input("enter current status of task u want to change"))
#     if current_status==1:
#         for s in range(1,len(incomplete)+1):
#             print(s,incomplete[s-1])
#         task_to_delete=int(input("enter no of task u want to delete"))
#         for t in incomplete:
#             # if incomplete.index(t)==task_to_delete-1: