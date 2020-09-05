(function ($) {

    /**
     * Search filters - submit only changed fields
     */
    $.fn.haveli_search_filters = function () {
        $(this).change(function () {
            var $field = $(this);
            var $option = $field.find('option:selected');
            var select_name = $option.data('name');
            // if (select_name) {
            //     $field.attr('name', select_name);
            // } else {
            //     $field.removeAttr('name');
            // }
            // Handle additional values for date filters
            var additional = $option.data('additional');
            if (additional) {
                var hidden_id = $field.data('name') + '_add';
                var $hidden = $('#' + hidden_id);
                console.log($hidden.length);
                if (!$hidden.length) {
                    $hidden = $('<input/>').attr('type', 'hidden').attr('id', hidden_id);
                    $field.after($hidden);
                }
                additional = additional.split('=');
                $hidden.attr('name', additional[0]).val(additional[1])
            }
        });
        $(this).trigger('change');
    };

    $(function () {

        $('.search-filter').haveli_search_filters();

    });

}(haveli.jQuery));