$(".btn_menu").click(function () {
    $(".wrap").toggleClass("openMenu"); 
});

$(".offcanvas_item").click(function () {
    $(".wrap").removeClass("openMenu"); 
});