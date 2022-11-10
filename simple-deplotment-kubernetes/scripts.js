function redButtonClicked(){
    var sw = screen.width;
    var sh = screen.height;
    var ww = 400;
    var wh = 400;
    window.open("./bruh.html", "bruhWindow", "width="+ww+"px,height="+wh+"px,resizable=no,top="+((parseInt(sh)/2)-(parseInt(wh)/2))+",left="+((parseInt(sw/2))-(parseInt(ww)/2))+"");
}