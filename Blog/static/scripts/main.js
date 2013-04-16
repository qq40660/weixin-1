function addHander(ele, type, hander) {
    if (ele.addEventListener) {
        ele.addEventListener(type, hander, false);
    } else if (ele.attachEvent) {
        ele.attachEvent("on" + type, hander);
    } else {
        ele["on" + type] = hander;
    }
}

var backtop = document.getElementById("backtop");
backtop.style.display = "none";

addHander(window, "scroll", function(event) {
    var scroll_top = document.body.scrollTop || document.documentElement.scrollTop;
    if (scroll_top > 100) {
        backtop.style.display = "block";
    } else {
        backtop.style.display = "none";
    }
});

addHander(backtop, "click", function(event) {
    window.scroll(0,0);
});