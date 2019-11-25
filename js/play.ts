/** @format */

export interface Abc {
  x: number;
}

type AbcOpt = Abc | null;

export async function main() {
  console.log('hello world');

  let v: AbcOpt = { x: 1 };
  if (v === null) {
    return;
  }
  console.log(v.x);
}

main();
