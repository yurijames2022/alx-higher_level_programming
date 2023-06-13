exports.esrever = function (list) {
  const dupList = [];
  for (let i = list.length - 1; i > -1; i--) {
    dupList.push(list[i]);
  }
  return dupList;
};
