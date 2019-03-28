$.ajax({
    url: 'http://localhost:8000/book/4/',
    type: 'post',
    success: function(data) {
        alert(data);
    },
    failure: function(data) {
        alert('error');
    }
});