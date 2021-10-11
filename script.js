(function() {
  function random(max) {
    return Math.floor(Math.random() * max);
  }
  
  function addStar(type) {
    var div = document.createElement("div");
    div.classList.add("star", type);
    div.style.top = random(window.innerHeight) + "px";
    document.body.appendChild(div);
  }
  
  for(var i = 0; i < 10; ++i) {
    var delay = i * 333;
    window.setTimeout(addStar, delay, "small");
    window.setTimeout(addStar, delay + 333, "medium");
    window.setTimeout(addStar, delay + 666, "big");
  }
})();
