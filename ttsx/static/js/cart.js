/**
 * Created by python on 17-9-14.
 */

$(function () {
    total();
    checkbox();
    count();
    $('.col08').children('a').click(function () {
        var id = $(this).parent().siblings('.col01').children('input').val();
        var dul = $(this).parent()
        cart_del(id,dul);
    });
});

// 数量变化
function count() {
    $('.num_show').each(function () {
        $(this).bind('input', 'propertychange', function () {
            var count = parseInt($(this).val());
            if (isNaN(count) || count != $(this).val() || (count < 1)) {
                $(this).val(1);
            }
            else if (count > 99) {
                $(this).val(99);
            }
            edit($(this));
            total();
        });
        // 增加
        $(this).prev().click(function () {
            var num = $(this).next().val();
            if (num >= 99) {

                return false
            }
            else {

                $(this).next().val(parseInt(num) + 1);
            }
            edit($(this).next());
            total();
        });
        //           减少
        $(this).next().click(function () {
            var num = $(this).prev().val();
            if (num < 2) {
                return false
            }
            else {
                $(this).prev().val(parseInt(num) - 1);
            }
            edit($(this).prev());
            total();
        });

    });

}
//                 修改数据
function edit(i) {


    var cid = i.parent().parent().siblings('.col01').children('input').val();
    var ccount = i.val();
    $.get('/cart/edit' + (cid) + '_' + ccount + '/')
}

function total() {
    var total_1 = 0;
    var total_count = 0;

    $('.col06:gt(0)').each(function () {
        var count = 0;
        var price = 0;
        var total_2 = 0;
        if ($(this).siblings('.col01').children().prop('checked')) {
            count = parseInt($(this).children().eq(0).children('.num_show').eq(0).val());
            price = parseFloat($(this).prev().text());
            total_2 = (count) * price;
            $(this).next().text(total_2.toFixed(2) + '元');
            total_1 += total_2;
            total_count ++;

        }
        else {
            count = parseInt($(this).children().eq(0).children('.num_show').eq(0).val());
            price = parseFloat($(this).prev().text());
            total_2 = (count) * price;
            $(this).next().text(total_2.toFixed(2));
        }


    });
    $('#total').text(total_1.toFixed(2));
    $('.total_count1').text(total_count);


};

function checkbox() {


    //        设置全选
    $('#check_all').click(function () {
        var state = $(this).prop('checked');
        $(':checkbox:not(#check_all)').prop('checked', state);

        total();
    });
    //    设置单选
    $(':checkbox:not(#check_all)').click(function () {
        var len1 = $(':checked:not(#check_all)').length;
        var len2 = $(':checkbox:not(#check_all)').length;
        $('#check_all').prop('checked', len1 == len2);

        total();
    })

}
function cart_del(cart_id,dul) {

    var del = confirm('确定删除商品么？');
    if (del) {
        $.get('/cart/delete' + cart_id + '/', function (data) {
            if (data.ok == 1) {
                // $('ul').remove('#' + cart_id);
                dul.remove();
                total();
            }
        });
    }
}

