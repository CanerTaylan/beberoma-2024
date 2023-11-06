


// template

'use strict';
$(document).ready(function () {

    // Accordion
    var all_panels = $('.templatemo-accordion > li > ul').hide();

    $('.templatemo-accordion > li > a').click(function () {
        console.log('Hello world!');
        var target = $(this).next();
        if (!target.hasClass('active')) {
            all_panels.removeClass('active').slideUp();
            target.addClass('active').slideDown();
        }
        return false;
    });
    // End accordion
    // Product detail
    $('.product-links-wap a').click(function () {
        var this_src = $(this).children('img').attr('src');
        $('#product-detail').attr('src', this_src);
        return false;
    });
    $('#btn-minus').click(function () {
        var val = $("#var-value").html();
        val = (val == '1') ? val : val - 1;
        $("#var-value").html(val);
        $("#product-quanity").val(val);
        return false;
    });
    $('#btn-plus').click(function () {
        var val = $("#var-value").html();
        val++;
        $("#var-value").html(val);
        $("#product-quanity").val(val);
        return false;
    });
    $('.btn-size').click(function () {
        var this_val = $(this).html();
        $("#product-size").val(this_val);
        $(".btn-size").removeClass('btn-secondary');
        $(".btn-size").addClass('btn-success');
        $(this).removeClass('btn-success');
        $(this).addClass('btn-secondary');
        return false;
    });
    // End roduct detail

});


// alert-message

document.addEventListener("DOMContentLoaded", function () {
    new mdb.Alert(document.getElementById("alert-mess"), {
        position: "top-right",
        delay: 2000,
        autohide: false,
        width: "500px",
        offset: 20,

    });
});



// $(function () {

//     function toggleChevron(e) {
//         $(e.target)
//             .prev('.panel-heading')
//             .find("i")
//             .toggleClass('rotate-icon');
//         $('.panel-body.animated').toggleClass('zoomIn zoomOut');
//     }

//     $('#accordion').on('hide.bs.collapse', toggleChevron);
//     $('#accordion').on('show.bs.collapse', toggleChevron);
// })


// sss panel animasyonu - start

$(function () {
    $('.panel-body.animated').toggleClass('zoomIn zoomOut');
});
// sss panel animasyonu - end




const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const formContainer = document.getElementById('form-container');

signUpButton.addEventListener('click', () => {
    formContainer.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
    formContainer.classList.remove("right-panel-active");
});
