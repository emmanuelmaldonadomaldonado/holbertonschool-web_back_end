export default function cleanSet(set, startString) {
  let result = '';
  for (const element of set) {
    if (element.startsWith(startString)) {
      const remainingString = element.slice(startString.length);
      result += (result === '' ? '' : '-') + remainingString;
    }
  }
  return result;
}
