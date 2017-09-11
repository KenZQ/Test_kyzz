/**
 * Created by python on 17-9-11.
 */
 $(function () {
            $.get('/user/get_user_msg/', function (data) {
                if (data == '') {
                    $('#ulist').empty().append('<li><span>用户名：</span>无</li> ' +
                        '<li><span>联系方式：</span>无</li> ' +
                        '<li><span>联系地址：</span>无</li>')
                }
                else {
                    $('#ulist').empty().append('<li><span>用户名：</span>'+data.name+'</li> <li><span>联系方式：</span>' + data.phone + '</li><li><span>联系地址：</span>'+data.addr+'</li>')
                        }
                    })
                    })