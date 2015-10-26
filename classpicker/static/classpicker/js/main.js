$(document).ready(function(){
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var pick_form = $('#pick_form');

    pick_form.on('submit', ajaxCall);
    function ajaxCall(event){
        event.preventDefault();
        var result = [];
        $(this).find('input:checked').each(function(){
            result.push($(this).prop('name'));
        });
        result = JSON.stringify(result);
        $.ajax({
            url: '',
            type: 'POST',
            data: {
                ping: false,
                result: result
            },
            dataType: 'json',
            success: function(response){
                var redirect = response['redirect'];
                $('input:submit').prop('disabled', true);

                if (redirect) {
                    window.location.replace(window.location.pathname + "/result");
                }
                else{
                    function ajaxPing(){
                        $.ajax({
                            url: '',
                            type: 'POST',
                            data:{
                                ping: true
                            },
                            dataType: 'json',
                            success: function(response){
                                if (response['redirect']){
                                    window.location.replace(window.location.pathname + "/result");
                                }
                            }
                        })
                    }

                    window.setInterval(ajaxPing, 5000)

                }

            }

        })
    }

//    ajaxCall();
//    window.setInterval(function(){ajaxCall();}, 5000)

});