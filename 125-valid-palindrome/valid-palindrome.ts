function isPalindrome(s: string): boolean {
    let str: string = "";
    for (let i = 0; i < s.length; i++) {
        if (
            (s[i] >= "A" && s[i] <= "Z") ||
            (s[i] >= "a" && s[i] <= "z") ||
            (s[i] >= "0" && s[i] <= "9")
        ) {
            str += s[i];
        }
    }
    console.log(str);
    str = str.toLowerCase(); // Corrected line

    console.log(str);
    let reversedStr: string = str.split("").reverse().join("");
    console.log(reversedStr);
    if (reversedStr === str) {
        return true;
    } else {
        return false;
    };
}

console.log(isPalindrome("race a car"));
console.log("jkhuchvjh");
