$(document).ready(function(){
    var picks_first = $('#id_picks_first');
    /* TODO: add if statement */
    picks_first.parent().hide();

    $('#id_no_bans').on('change', function(){
        picks_first.parent().fadeToggle();
    })
});