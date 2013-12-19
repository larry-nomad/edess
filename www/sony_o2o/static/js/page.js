var CONST = {
    stars: ['☆', '★'],
    btn_weibo: '<wb:share-button data-role="none" type="button" addition="simple" picture_search="false" pic="${pic}" default_text="${text}" language="zh_cn"></wb:share-button>',
    js_weibo: '<script class="J-js-weibo" src="http://tjs.sjs.sinajs.cn/open/api/js/wb.js" charset="utf-8"></script>',
    btn_qzone: '<a version="1.0" class="qzOpenerDiv" href="http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?${query}" target="_blank"><span>分享到Qzone</span></a>',
    js_qzone: '<script class="J-js-qzone" src="http://qzonestyle.gtimg.cn/qzone/app/qzlike/qzopensl.js#jsdate=20111201" charset="utf-8"></script>'
};
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

var rankStar = function(n) {
    var n = parseInt(n) || 0;
    n = n < 0 ? 0 : n;
    n = n > 5 ? 5 : n;
    var star = [];
    for(var i = 0; i < 5; i++) {
        if(i < n) {
            star.push(CONST.stars[1]);
        }
        else {
            star.push(CONST.stars[0]);
        }
    }
    return star.join('');
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
$(document).on("swiperight swipeleft", '#hot, #travel, #likes, #detail, #profile, #store', function( e ) {
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
$(document).on('pagebeforecreate', '#hot, #travel, #likes, #detail, #profile, #store', function(e) {
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
$(document).on('pagebeforeshow', '#hot, #travel', function(e) {
    /**
     * 获取数据，填充列表
     */
    var page = $(this).attr('id'),
        hot_arr = [1, 2, 3, 15, 16, 17, 18],
        travel_arr = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
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
                product_id: data[i].id,
                name: data[i].name,
                brief: data[i].brief,
                buy_link: data[i].tmall_link || data[i].jd_link || '#'
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
 * 我的收藏
 */
$(document).on('pageinit', '#likes', function(e) {
    $(this).on('click', '.J-likes-unlike', function(e) {
        var id = $(this).attr('data-product_id'),
            url = '/v1/like?product_id=' + id;
        $.ajax(url, {
            type: 'delete',
            error: function(xhr, status, err) {
                var res = JSON.parse(xhr.responseText);
                alert(res.msg);
            },
            success: function(res, status, xhr) {
                window.location.reload();
            }
        });
    });
});

$(document).on('pagebeforeshow', '#likes', function(e) {
    var page = $(this).attr('id'),
        url = '/v1/likes';
    $.get(url, function(res, status, xhr) {
        if(status !== 'success' || res.data.length === 0) {
            return;
        }
        var template = $('#J_template_list_likes').html(),
            data = res.data,
            html = '';
        for(var i = 0, len = data.length; i < len; i++) {
            html += renderTemplate(template, {
                product_id: data[i].id,
                name: data[i].name,
                brief: data[i].brief,
                buy_link: data[i].tmall_link || data[i].jd_link || '#'
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
$(document).on('pageinit', '#detail', function(e) {
    /**
     * 喜欢按钮
     */
    $('#J_detail_like').on('click', function(e) {
        var hash = window.location.hash,
            param = getParam(hash.replace('#detail?', '')),
            like_url = '/v1/like';
        $.ajax(like_url, {
            type: 'post',
            data: 'product_id='+param.id,
            error: function(xhr, status, err) {
                var res = JSON.parse(xhr.responseText);
                alert(res.msg);
            },
            success: function(res, status, xhr) {
                window.location.reload();
            }
        });
    });
    /**
     * 提交评论
     */
    $('#J_detail_stars').on('click', 'span', function(e) {
        var els = $('span', e.delegateTarget),
            idx = 0;
        for(var i = 0; i < els.length; i++) {
            if(this === els[i]) {
                idx = i+1;
                break;
            }
        }
        for(var i = 0; i < els.length; i++) {
            if(i < idx) {
                $(els[i]).html(CONST.stars[1]);
            }
            else {
                $(els[i]).html(CONST.stars[0]);
            }
        }
        $(e.delegateTarget).attr('data-ranked_stars', idx);
    });
    $('#J_detail_send_comment').on('click', function(e) {
        var hash = window.location.hash,
            param = getParam(hash.replace('#detail?', '')),
            comment = $.trim($('#J_detail_write_comment').val()),
            ranked_stars = $('#J_detail_stars').attr('data-ranked_stars'),
            url = '/v1/review';
        if(comment === '') {
            alert('评论内容不能为空！')
            return;
        }
        $.ajax(url, {
            type: 'post',
            data: {
                product_id: param.id,
                comment: comment,
                ranked_stars: ranked_stars
            },
            error: function(xhr, status, err) {
                var res = JSON.parse(xhr.responseText);
                alert(res.msg);
            },
            success: function(res, status, xhr) {
                $('#detail_comment').dialog('close');
            }
        });
    });
});

$(document).on('pagebeforeshow', '#detail', function(e) {
    var hash = window.location.hash,
        param = getParam(hash.replace('#detail?', '')),
        brief_url = '/v1/product/' + param.id,
        comment_url = '/v1/reviews?is_approved=true&product_id=' + param.id;
    $.get(brief_url, function(res, status, xhr) {
        if(status !== 'success') {
            return;
        }
        var template = $('#J_template_video').html(),
            data = res.data,
            v_url = '';
        for(var i = 0; i < data.videos.length; i++) {
            v_url = data.videos[i].video_url;
        }
        $('#J_detail_video').html(renderTemplate(template, {
            product_id: data.id,
            video_url: v_url
        }));
        $('.J-detail-title').html(data.name);
        $('#J_detail_brief').html(data.brief);
        $('#J_detail_like').html(data.likes_count+'喜欢').button('refresh');
        $('#J_detail_buy_link').attr('href', data.jd_link || data.tmall_link || '#');

        /**
         * weibo按钮
         */
        $('.J-js-weibo').remove();
        $('#J_detail_share_weibo').html(renderTemplate(CONST.btn_weibo, {
            text: data.name,
            pic: encodeURIComponent('http://touch.xperia.qunar.com/static/product_img/'+data.id+'/a.jpg')
        }));
        $(CONST.js_weibo).appendTo(document.body);

        /**
         * qzone按钮
         */
        var p = {
            url: location.href,
            showcount: '0',/*是否显示分享总数,显示：'1'，不显示：'0' */
            desc: data.name,/*默认分享理由(可选)*/
            summary: data.brief,/*分享摘要(可选)*/
            title: data.name,/*分享标题(可选)*/
            site: '去哪儿网',/*分享来源 如：腾讯网(可选)*/
            pics: 'http://touch.xperia.qunar.com/static/product_img/'+data.id+'/a.jpg', /*分享图片的路径(可选)*/
            style:'102',
            width: 88,
            height: 30
        };
        var s = [];
        for(var i in p){
            s.push(i + '=' + encodeURIComponent(p[i]||''));
        }
        $('#J_detail_share_qzone').html(renderTemplate(CONST.btn_qzone, {
            query: s.join('&')
        }));
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
            var guest_name = '游客';
            if(!!data[i].guest && !!data[i].guest.name) {
                guest_name = data[i].guest.name;
            }
            el.append(renderTemplate(template, {
                comment: data[i].comment,
                review_date: data[i].review_date,
                ranked_stars: rankStar(data[i].ranked_stars),
                guest_id: data[i].guest_id,
                guest_name: guest_name,
                product_id: data[i].product_id
            }));
        }
        el.listview('refresh').trigger('create');
    });

    $('#J_detail_stars span').html(CONST.stars[0]);
    $('#J_detail_write_comment').val('');
});

$(document).on('pagebeforehide', '#detail', function(e) {
    $('#J_detail_video').html('');
});
