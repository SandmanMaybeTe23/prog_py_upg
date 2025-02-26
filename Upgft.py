todo=["eat","sleep","rep"]
in_progress=["","",""]
done=["","",""]

in_progress.insert(1,todo[1]) 
in_progress.pop()

print(in_progress)
todo.remove("sleep")
todo.insert(1,"")

done.insert(0,in_progress[1])
in_progress.remove("sleep")
in_progress.insert(1,"")
done.pop()

print(todo)
print(in_progress)
print(done)