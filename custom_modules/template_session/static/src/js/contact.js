odoo.define("contacts", function (require) {
    "use strict";

  $(document).ready(function(){
        $(".partners_list").on('click', '.container', function(e){
            let href = $(this).attr("data-href");
            window.location.href = href;
        });

    });

});
