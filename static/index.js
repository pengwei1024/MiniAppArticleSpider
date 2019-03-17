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