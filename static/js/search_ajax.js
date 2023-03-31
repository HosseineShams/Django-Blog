$(function(){
    $('#searchInput').keyup(function(){
        $.ajax({
            type: "GET",
            url: '/search/',   
            data: {
                'search_text': $('#searchInput').val()
            },
            success: searchSuccess,
            error: searchError,
            dataType: 'html'
        });
    });
});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search_results').html(data);
    console.log("Ajax Done!");
}     

function searchError(data, textStatus, jqXHR)
{
    console.log("Ajax Failed!");
}     