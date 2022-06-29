const solution = (A) => {
    let right_pass = new Array(A.length).fill(0);
    let left_pass = new Array(A.length).fill(0);

    let current_idx = 0;
    let right_idx = current_idx + 1;
    while (current_idx < A.length) {
        if (right_idx == A.length) break;
        if (A[right_idx] > A[current_idx]) {
            right_pass[current_idx] = Math.abs(right_idx - current_idx);
            current_idx++;
            right_idx = current_idx + 1
            continue;
        }
        right_idx++;
    }

    current_idx = A.length - 1;
    let left_idx = A.length - 2;
    while (current_idx > 0) {
        if (left_idx == -1) {
            current_idx--;
            left_idx = current_idx - 1;
            continue
        };
        if (A[left_idx] > A[current_idx]) {
            left_pass[current_idx] = Math.abs(left_idx - current_idx);
            current_idx--;
            left_idx = current_idx - 1
            continue;
        }
        left_idx--;
    }

    const getMin = (a, b)=> a === 0 && b || b === 0 && a || Math.min(a,b);
    let R = right_pass.map((val, idx) => getMin(val, left_pass[idx]));

    return R
}
A = [4, 3, 1, 4, -1, 2, 1, 0, 1, -3, -4, 2, 1, 0, 3, 5, 7];
ans = solution(A);
console.log(ans);