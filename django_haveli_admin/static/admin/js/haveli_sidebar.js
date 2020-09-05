(function ($) {

    // Show sidebar on menu clicked
    $.fn.haveli_show_side_bar = function (){
        $(this).click(function (){
            $('#nav-sidebar').css('left',0)
        });
    }

    // Hide sidebar on menu clicked
    $.fn.haveli_hide_side_bar = function (){
        $(this).click(function (){
            $('#nav-sidebar').css('left',-300)
        });
    }


    $.fn.toggle_menu = function (){
        $(this).click(function () {
            var $menu = $(this);
            var $menu_container = $menu.parent().parent();
            var $sub_menu = $menu_container.find('.nav_models');

            // var $sub_menu_clone = $sub_menu.clone().toggleClass('collapse').appendTo($menu_container);
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

        $('#nav-menu').haveli_show_side_bar();

        $('#nav_back').haveli_hide_side_bar();

        $('.nav_drop_down').toggle_menu();

    });

}(haveli.jQuery));