function printMyVar() {
    var Var = 1234;
    if (true) {
        var Var = 4321;
    }
    console.log(Var)
}

printMyVar()