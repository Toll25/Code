function printMyVar() {
    const Var = 1234;
    if (true) {
        const Var = 4321;
    }
    console.log(Var)
}

printMyVar()