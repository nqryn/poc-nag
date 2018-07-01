$.fn.exists = function () {
    return this.length !== 0;
}

$(document).ready(function() {

    $('.more').click(function() {
        var p = $(this).parents('.content.visible');
        var sibling = p.siblings('.content.hidden');
        // Set height, so that it doesn't flickr
        sibling.css('height', p.css('height'));
        p.hide();
        sibling.fadeIn(600);
    }); 

    $('.less').click(function() {
        var p = $(this).parents('.content.hidden');
        var sibling = p.siblings('.content.visible');
        p.hide();
        sibling.fadeIn(600);

    })

});