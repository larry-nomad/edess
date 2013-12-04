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
    $('#J_profile_btn_save').on('click', function(e) {
        if($('#J_profile_name').val() === '') {
            window.scrollTo(0, 0);
            alert('登录名称，不能为空！');
            return;
        }
        var url = '/v1/guest';
        $.ajax(url, {
            type: 'put',
            data: $('#J_profile_form').serialize(),
            error: function(xhr, status, err) {
                var res = JSON.parse(xhr.responseText);
                alert(res.msg);
            },
            success: function(res, status, xhr) {
                alert('用户信息修改成功');
            }
        });
    });
});
$(document).on('pagebeforeshow', '#profile', function(e) {
    var url = '/v1/guest';
    $.get(url, function(res, status, xhr) {
        if(status !== 'success') {
            return;
        }
        var keys = ['name', 'gender', 'birthday', 'email', 'telephone', 'qq', 'wechat', 'weibo'],
            data = res.data;
        for(var i = 0; i < keys.length; i++) {
            var key = keys[i];
            if(data[key]) {
                if(key === 'gender') {
                    $('#J_profile_form input:radio[value=' + data[key]+ ']').prop('checked', true);
                    $('#J_profile_form input:radio').checkboxradio('refresh');
                }
                else {
                    $('#J_profile_form input[name=' + key + ']').val(data[key]);
                }
            }
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
        hot_arr = [2, 3, 6, 7, 12, 13, 14],
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
                brief: data[i].brief,
                tmall_link: data[i].tmall_link
            });
        }
        $('#' + page + ' .list-container ul').html(html).listview('refresh').trigger('create');
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
        brief_url = '/v1/product/' + param.id,
        comment_url = '/v1/reviews?is_approved=false&product_id=' + param.id;
    $.get(brief_url, function(res, status, xhr) {
        if(status !== 'success') {
            return;
        }
        var data = res.data;
        $('.J-detail-title').html(data.name);
        $('.J-detail-brief').html(data.brief);
        $('.J-detail-like').html(data.likes_count);
    });
    $.get(comment_url, function(res, status, xhr) {
        if(status !== 'success') {
            return;
        }
        var data = res.data,
            el = $('#J_detail_comment'),
            template = $('#J_template_comment').html();
        el.html('');
        for(var i = 0; i < data.length; i++) {
            el.append(renderTemplate(template, {comment: data[i].comment}));
        }
        el.listview('refresh').trigger('create');
    });
});
