function countChar(val) {
    var len = val.value.length;
    if (len >= 400) {
        val.value = val.value.substring(0, 400);
    } else {
          $('#charNum').text(400 - len);
        }
};