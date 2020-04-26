function add_admin() {
    let data = $('#add_admin_form').serialize()
    $.ajax({
        url: "/add_admin/",
        data: data,
        type: "POST",
        success: function (res) {
            res = JSON.parse(res)
            if (res.code == 400) {
                $('#error_kuang').removeClass("hide")
                $('#error_text').html(res.error)

            } else if (res.code == 200) {
                location.href = "/admin/"
            }
        }
    });
}

function update_admin(user_id) {
    let data = $('#update_admin_form').serialize()
    $.ajax({
        url: "/update_admin/"+user_id+"/",
        data: data,
        type: "POST",
        success: function (res) {
            res = JSON.parse(res)
            if (res.code == 400) {
                $('#error_kuang').removeClass("hide")
                $('#error_text').html(res.error)

            } else if (res.code == 200) {
                location.href = "/admin/"
            }
        }
    });
}

$('#close').click(function () {
    $('#error_kuang').addClass("hide")
})