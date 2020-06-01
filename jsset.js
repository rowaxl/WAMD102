const duplicated = [3,2,3,2,3,4,3,5];
const uniq = [];

for (const e of duplicated) {
  if (!uniq.includes(e)) {
    uniq.push(e)
  }
}

console.log(uniq)