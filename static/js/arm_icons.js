$('img').bind('mousedown', function(e) {
    $.post('http://localhost:5000/move_arm', '{"servo" : "' + e.currentTarget.id + '", "startEvent" : true}')
});
$('img').bind('mouseup', function(e) {
    $.post('http://localhost:5000/move_arm', '{"servo" : "' + e.currentTarget.id + '", "startEvent" : false}')
});
console.log('hello')