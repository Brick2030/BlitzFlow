class task:
    def __init__(self, cycles, name, status, result):
        self.PlannedCycles = cycles
        self.Name = name
        self.ChangeStatus(status)
        self.Result = result 

# new status system
# 0 - Ongoing.
# 1 - Finished
# -1 - Failed (delayed).
# Object will store only number status. And table itself will translate it words
# Or maybe it's better to use dictionary. But why to complicate such simple things.

    def ChangeStatus(self, input):
        match input:
            case 0: self.Status = "Failed"
            case 1: self.Status = "Nothing"
            case 2: self.Status = "Ongoing"
            case 3: self.Status = "Completed"
        return self.Status

    def ChangeResult(self, input):
        self.Result = input
        return self.Result

    def ReturnTask(self):
        #return [PlannedCycles, Name, Status, Result]
        return [self.PlannedCycles, self.Name, self.Status, self.Result]

