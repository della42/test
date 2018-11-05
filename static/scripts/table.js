$(document).ready(function() {
  getPerformanceData();
});

function getPerformanceData() {

    $.ajax({
        url: "/table_data"
    }).done(function(response) {

        $('#redification-table').bootstrapTable({
            data: response.result
        });
    });
};
