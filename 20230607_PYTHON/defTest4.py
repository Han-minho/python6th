def disp():
    def show():
        return "Show Function"
    print("Disp Function")
    return show

r_sh = disp()

print(r_sh(),type(r_sh))