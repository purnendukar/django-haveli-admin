(function ($) {

    // to epand and collapse the user drop down options
    $.fn.toggle_drop_down = function (){
        $(this).click(function () {
            var $menu = $(this);
            var $menu_container = $menu.parent().parent();
            var $sub_menu = $menu_container.find('.user_menu');

            var $sub_menu_clone = $sub_menu.clone().css('height','auto').appendTo($menu_container);
            var height = $sub_menu_clone.height();
            console.log(height);
            $sub_menu_clone.remove();
            // console.log(height)
            
            $sub_menu.toggleClass('collapse');

            if($sub_menu.hasClass('collapse')){
                $sub_menu.css({"height":0});
            }else{
                $sub_menu.css({"height":height});
            }
        });
    }

    $(function () {

        $('.user_drop_down').toggle_drop_down();

    });

}(haveli.jQuery));