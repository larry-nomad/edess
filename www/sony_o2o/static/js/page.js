/**
 * 模版解析
 */
var renderTemplate = function(template, data) {
    for(var i in data) {
        if(!data.hasOwnProperty(i)) {
            continue;
        }
        var reg = new RegExp('\\$\\{' + i + '\\}', 'g');
        template = template.replace(reg, data[i]);
    }
    return template;
};
var getParam = function(str) {
    var p_arr = str.split('&'),
        param = {};
    for(var len = p_arr.length; len > 0; len--) {
        var obj = p_arr[len - 1].split('=');
        param[obj[0]] = obj[1];
    }
    return param;
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
$(document).on("swiperight swipeleft", '#hot, #travel, #detail, #profile, #store', function( e ) {
    var pageId = $(this).attr('id');
    if($.mobile.activePage.jqmData("panel") !== "open" ) {
        if ( e.type === "swiperight" ) {
            $('#panel-left-' + pageId).panel('open');
        }
        if ( e.type === "swipeleft" ) {
            $('#panel-right-' + pageId).panel('open');
        }
    }
});
$(document).on('pagebeforecreate', '#hot, #travel, #detail, #profile, #store', function(e) {
    var pageId = $(this).attr('id'),
        panel_template = renderTemplate($('#J_template_panel').html(), {
            pageId: pageId
        });
    $(this).prepend(panel_template);
});
/**
 * profile页面
 */
$(document).on('pageinit', '#profile', function(e) {
    $('#J_profile_form').on('submit', function(e) {
        if($('#J_profile_login').val() === '') {
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
            html += renderTemplate(template, {
                id: data[i].id,
                name: data[i].name,
                brief: data[i].brief
            });
        }
        $('#' + page + ' .list-container ul').html(html).trigger('create').listview('refresh');
        $('#' + page + ' .list-container ul' + ' .swipe').each(function(idx) {
            Swipe(this, {
                continuous: true,
                stopPropagation: true
            });
        });
    });
});
/**
 * detail页面
 */
$(document).on('pagebeforeshow', '#detail', function(e) {
    var hash = window.location.hash,
        param = getParam(hash.replace('#detail?', '')),
        url = '/v1/product/' + param.id;
    $.get(url, function(res, status, xhr) {
        if(status !== 'success') {
            return;
        }
        var data = res.data;
        $('.J-detail-title').html(data.name);
        $('.J-detail-brief').html(data.brief);
        $('.J-detail-like').html(data.likes_count);
    });
});