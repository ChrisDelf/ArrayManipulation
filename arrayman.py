

def arrayManipulation(n, queries):

    list = [0] * (n+1);

    basline = 0

    for commands in queries:

        # we only want to concern ourselves with the edges of the commands
        list[commands[0]-1] += commands[2]


        if (commands[1] <= len(list)):
            # print ("y", commands[1], "lenght", len(list))

            list[commands[1]] -= commands[2]


        # print(list)


        maxi = 0

        x = 0

        for v in list:
            #print(x)
            x = v+x
            # if (x < baseline):
            #baseline = x

            if (maxi < x):
                #print(x, "setting maxi")
                maxi = x

        #print(maxi)
        #print(maxi+basline)

        return(maxi)
