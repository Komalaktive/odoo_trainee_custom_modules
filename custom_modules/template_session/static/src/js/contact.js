odoo.define("contacts", function (require) {
    "use strict";

// for making the list row click event(click event)
    $(document).ready(function(){
        $("#partners_list").on('click', '.contact_row', function(e){
            let href = $(this).attr("data-href");
            window.location.href = href;
            console.log("href",href);
        });

 // For Searching name In the contact list.........
        $("#filter_table").on("keypress", function(e) {
                console.log("e.keyCode----", e.keyCode)
                if (e.keyCode == 13 || e.keyCode == 8)
                {
                    var value = $(this).val().toLowerCase();
                    $("#partners_list tbody tr").filter(function() {
                        $(this).toggle($(this).find(".contact_name_col").text().toLowerCase().indexOf(value) > -1)
                        console.log("search end")
                    });
                }
        });


        $("")



    });

});