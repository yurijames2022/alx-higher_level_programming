exports.esrever = function (list) {
  const dupList = [];
  for (let i = 0; i < list.length; i++) {
    dupList.unshift(list[i]);
  }
  return dupList;
};
