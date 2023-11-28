document.addEventListener("DOMContentLoaded", function () {
    $('#parkingform').on('submit', (e) => {
        e.preventDefault();
        var formData = new FormData();
        formData.append('jsoninput', $('#jsoninput')[0].files[0]);
        $.ajax({
            url: '/parking',
            type: 'POST',
            data: formData,
            contentType: false,
            processData: false,
            success: function (data) {
                console.log(data);
            },
        });
    });
});
