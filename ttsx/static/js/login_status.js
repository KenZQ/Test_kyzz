/**
 * Created by python on 17-9-11.
 */
$(function () {
    $.get('/user/top_area/', function (data) {
        if (data.name != '') {
            var str1 = '<a href="/user/exit/" style="text-decoration:none; color:#666">&nbsp;&nbsp;退出</a>';
            $('.login_info').prepend('欢迎您：<em>' + data.uname + '</em>' +str1);
            $('.login_btn').css('display', 'none');
            $('.login_info').css('display', 'block');
        }
        else {
            $('.login_btn').css('display', 'block');
            $('.login_info').css('display', 'none');
        }
    });
})
