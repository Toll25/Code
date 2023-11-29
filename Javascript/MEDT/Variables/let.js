function printMyVar() {
    let Var = 1234;
    if (true) {
        let Var = 4321;
    }
    console.log(Var)
}

printMyVar()