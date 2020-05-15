document.onreadystatechange = function () {
  if (document.readyState === 'interactive') {
    document.querySelector('header').style.color = '#FF0000';
  }
};
