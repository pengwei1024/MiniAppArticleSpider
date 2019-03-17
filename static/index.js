$(function () {
    'use strict';
    //无限滚动
    $(document).on("pageInit", "#page-infinite-scroll-bottom", function (e, id, page) {
        var loading = false;
        var pageNum = 1;
        function addItem(array) {
            var html = '';
            array.forEach(function (item) {
                html += `
                <div class="card" onclick="location.href='${item.href }'"><div class="card-header color-white no-border">${item.title }
                        </div>
                        <div class="card-content">
                            <div class="card-content-inner">
                                <p>${ item.desc }</p>
                                <small>${ item.time }</small>
                            </div>
                        </div>
                    </div>
                `;
            });
            $('.page-index').append(html);
        }
        $(page).on('infinite', function () {
            // 如果正在加载，则退出
            if (loading) {
                return;
            }
            loading = true;
            $.ajax({
                url: 'post/' + pageNum,
                success: function (data) {
                    if (!data || data.length === 0) {
                        $.toast("没有更新的了~");
                        return;
                    }
                    pageNum++;
                    addItem(data);
                },
                fail: function (e) {
                    console.error(e)
                },
                complete:function () {
                    loading = false;
                    $.refreshScroller();
                }
            });
        });
    });
    $.init()
});
// // 加载flag
// var loading = false;
// // 每次加载添加多少条目
// var page = 0;
//
// function addItems(number, lastIndex) {
//     // 生成新条目的HTML
//     var html = '';
//     for (var i = lastIndex + 1; i <= lastIndex + number; i++) {
//         html += '<li class="item-content"><div class="item-inner"><div class="item-title">Item ' + i + '</div></div></li>';
//     }
//     // 添加新条目
//     $('.infinite-scroll-bottom .list-container').append(html);
// }
//
// // 注册'infinite'事件处理函数
// $(document).on('infinite', '.infinite-scroll-bottom', function () {
//     console.log('infinite!!!');
//     // 如果正在加载，则退出
//     if (loading) return;
//     loading = true;
//     page++;
//     $.ajax({
//         url: 'post/' + page,
//         success: function (data) {
//             console.log(data);
//             $.refreshScroller();
//         }
//     });
//     // // 模拟1s的加载过程
//     // setTimeout(function () {
//     //     // 重置加载flag
//     //     loading = false;
//     //
//     //     if (lastIndex >= maxItems) {
//     //         // 加载完毕，则注销无限加载事件，以防不必要的加载
//     //         $.detachInfiniteScroll($('.infinite-scroll'));
//     //         // 删除加载提示符
//     //         $('.infinite-scroll-preloader').remove();
//     //         return;
//     //     }
//     //
//     //     // 添加新条目
//     //     addItems(itemsPerLoad, lastIndex);
//     //     // 更新最后加载的序号
//     //     lastIndex = $('.list-container li').length;
//     //     //容器发生改变,如果是js滚动，需要刷新滚动
//     //     $.refreshScroller();
//     // }, 1000);
// });