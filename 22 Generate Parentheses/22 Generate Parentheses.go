func generateParenthesis(n int) []string {

    //output at each stage
    op := ""

    //final output
    var s []string

    //passing by reference
    solve(n,n,&s,op)
    return s
}

//taking pointer to *[]string because it needs update
func solve(o,c int,s *[]string, op string){

    //base case
    if o == 0 && c == 0 {
        //update the pointer for base case, just add whatever is the output
        *s = append(*s,op)
        return
    }

    // ( case, when we have opening backet we add '(' to output
    if o != 0 {
        op1 := op + "("
        solve(o-1,c,s,op1)
    }

    // ) case , when we have opening backet we add ')' to output only if closing count is greater
    if c > o {
        op2 := op + ")"
        solve(o,c-1,s,op2)
    }
    return
}
