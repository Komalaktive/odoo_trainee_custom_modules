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

// For changing image when input is given
        $("#partner_image_input").on('change', function(e)){
            console.log("this.................",this)
            console.log("$(this).........",$(this))
            var partner_img = $('#partner_image');
            var default_img = "/template_session/static/image/placeholder.png";
            var input = this
            if (input.files && input.files[0]) {
                $("delete_image").val("False");
                var reader = new FileReader();
                reader.onload = function(e){
                    partner_img.attr("src", e.target.result)
                    };
                    reader.readAsDataURL(input.files[0]);
                    }
            }
            else
            {
                if($("#delete_image").val() == "False")
                {
                    console.log("hello")
                    var partner_id = $("#partner_id").val()
                    if (partner_id)
                    {
                        default_image = "/web/image/res.partner/" + partner_id + "/image_1920";
                    }
                      partner_img.attr("src", default_image)

                }
            });
            $(".delete_image").on('click', function(e){
              $("#partner_image_input").val("");
              $("#delete_image").val("True");
              $("#partner_image_input").trigger("change");
        });



    });

});