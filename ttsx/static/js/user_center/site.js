/**
 * Created by python on 17-9-11.
 */

$(function () {
    $.get('/user/getmsg/', function (data) {
        if (data == '') {
            $('#addr').empty().append('无')
        }
        $('#addr').empty().append(data.addr + ' （' + data.name + '收） ' + data.phone);
    });
});
