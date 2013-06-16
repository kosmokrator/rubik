import rubik, config, random, time, sys, math

if __name__=="__main__":
    ani_class = None
    if len(sys.argv) > 1:
        try:
            ani_class = config.__dict__[sys.argv[1]]
        except:
            ani_class = None
    if not ani_object:
        ani_class = config.Solver
    rubik.Cube(ani_class().loop)

