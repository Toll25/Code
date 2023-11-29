err = open("./dicttest.txt").readlines()[2]
open("./error.txt", "a").write(err)