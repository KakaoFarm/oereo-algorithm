function solution(s)
{
    var answer = -1;
    let result = ""
    // console.log(s)
    temp = []
    temp.push(s[0])
    for (let i = 1; i<s.length; i++) {

        // console.log(result.substr(-1), s[i])
        if (s[i] !== temp[(temp.length)-1]) {
            temp.push(s[i])
        } else {
            temp.pop()
        }
       // console.log("step: ", result)
    }
    // console.log("result: ", result)
    console.log(temp)
    if (temp.length >= 1) {
        answer = 0
    } else {
        answer = 1
    }
    return answer;
}