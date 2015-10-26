$('document').ready(function(){
    var myRequests = [
        {
            method: 'GET',
            path: '/hello/middleware/',
            time: '16 Jul 2015 08:14:45',
            response_code: '200'
        },
        {
            method: 'GET',
            path: '/hello/contact/',
            time: '16 Jul 2015 08:12:35',
            response_code: '200'
        }
    ];

    var userOnline = true;
    var newInfoCount = 0;
    var defaultTitle = document.title;
    var last_id = 0;

    $(document).on('mousemove', function(){
        userOnline = true;
        document.title = defaultTitle;
        newInfoCount = 0;
    });

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

    function ajaxCall(){
        $.ajax({
            url: '',
            type: 'POST',
            data: {
                'last_id': last_id.toString()
            },
            dataType: 'json',
            success: function(response){
                var requests = response.requests;
                newInfoCount += requests.length;
                last_id = response.last_id;


                var newRequests = $.map(requests, function(info, i){
                    var singleInfo = $('<tr></tr>');
                    var date = new Date(Date.parse(info.time));

                    singleInfo.append($("<td>" + date.toLocaleTimeString() + "</td>"));
                    singleInfo.append($("<td>" + info.method + "</td>"));
                    singleInfo.append($("<td>" + info.path + "</td>"));
                    singleInfo.append($("<td>" + info.is_ajax + "</td>"));
                    singleInfo.append($("<td>" + info.status_code + "</td>"));
                    singleInfo.addClass('single_request');
                    return singleInfo;
                });

                $('.requests').find('table').append(newRequests).fadeIn();

                $($('.single_request').get().reverse()).each(function(index){
                    if(index >= 10) $(this).remove();
                });

                if (userOnline == false && newInfoCount !== 0) {
                    document.title = '[' + newInfoCount + ']' + defaultTitle;
                }

            }

        })
    }

    ajaxCall();
    window.setInterval(function(){userOnline = false; ajaxCall();}, 5000)

});