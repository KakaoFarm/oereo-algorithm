let dx = [1, 0, -1, 0]
let dy = [0, 1, 0, -1]

function bfsFunction(arr, start) {
    let queue = []; // queue를 쓰진 않았으나 queue처럼 사용하겠다.

    let check = Array.from(Array(arr.length), () => Array(arr[0].length).fill(false))
    // console.log(check)

    queue.push(start);
    check[start[0]][start[1]] = 1
    let length = 0;

    while(queue.length > 0){
        let x = queue.shift()
        length++;
        for (let i = 0; i<4; i++) {
            let nx = x[0] + dx[i]
            let ny = x[1] + dy[i]
            if (nx<0 || ny<0 || nx>=arr.length || ny>arr[0].length) continue
            if (!check[nx][ny] & arr[nx][ny] === 1){
                queue.push([nx, ny])
                arr[nx][ny] = arr[x[0]][x[1]] +1
                check[nx][ny] = true
            }

        }
    }
    // console.log(arr)
    return arr;
}

function solution(maps) {
    var answer = 0;
    let a = 0;
    a = bfsFunction(maps, [0, 0])
    answer = a[maps.length-1][maps[0].length-1]
    if (answer === 1) {
        answer = -1
    }
    return answer;
}