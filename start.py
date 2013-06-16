import rubik, config, random, time, sys, math

if __name__=="__main__":
    ani_object = None
    if len(sys.argv) > 1:
        try:
            ani_object = config.__dict__[sys.argv[1]]
        except:
            ani_object = None
    if not ani_object:
        ani_object = config.Solver
    rubik.Cube(ani_object().loop)

