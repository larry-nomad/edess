/**
 * 模版解析
 */
var TemplateRender = function(template, data) {
    for(var i in data) {
        if(!data.hasOwnProperty(i)) {
            continue;
        }
        var reg = new RegExp('\\$\\{' + i + '\\}', 'g');
        template = template.replace(reg, data[i]);
    }
    return template;
};
/**
 * 返回顶部按钮
 */
$(window).on('scrollstop', function(e) {
    var el = $('.go-top'),
        win = $(window);
    if(win.scrollTop() > win.height() / 2) {
        el.show();
    }
    else {
        el.hide();
    }
});
/**
 * 滑动菜单
 */
$(document).on("swiperight", function( e ) {
    if ( $.mobile.activePage.jqmData( "panel" ) !== "open" ) {
        if ( e.type === "swiperight" ) {
            $( "#left-panel" ).panel( "open" );
        }
    }
});
/**
 * profile页面
 */
$(document).on('pageinit', '#profile', function(e) {
    $('#J_profile_form').on('submit', function(e) {
        if($('#J_login').val() === '') {
            window.scrollTo(0, 0);
            alert('登录名称，不能为空！');
            e.preventDefault();
            return false;
        }
    });
});
/**
 * list页面
 */
$(document).on('pageinit', '#hot, #travel', function(e) {
    /**
     * 获取数据，填充列表
     */
    var page = $(this).attr('id'),
        hot_arr = [2, 3, 6, 7, 13, 14],
        //hot_arr = [2, 3, 6, 7, 9, 11, 12, 13, 14],
        travel_arr = [1, 4, 5],
        //travel_arr = [1, 4, 5, 8, 10],
        urls = {
            'hot': '/v1/products?id=' + hot_arr.join('&id='),
            'travel': '/v1/products?id=' + travel_arr.join('&id='),
            'other': '/v1/products'
        },
        url = urls[(page in urls) ? page : 'other'];

    $.get(url, function(res, status, xhr) {
        if(status !== 'success' || res.data.length === 0) {
            return;
        }
        var template = $('#J_template_list').html(),
            data = res.data,
            html = '';
        for(var i = 0, len = data.length; i < len; i++) {
            html += TemplateRender(template, {
                id: data[i].id,
                name: data[i].name,
                brief: data[i].brief
            });
        }
        $('#' + page + ' ul').html(html).trigger('create').listview('refresh');
        $('#' + page + ' ul' + ' .swipe').each(function(idx) {
            Swipe(this, {
                continuous: true,
                stopPropagation: true
            });
        });
    });
});