var ip_address = '192.168.1.194'
$('img').bind('mousedown', function(e) {
    $.post('http://' + ip_address + ':5000/move_arm', '{"servo" : "' + e.currentTarget.id + '", "startEvent" : true}')
});
$('img').bind('mouseup', function(e) {
    $.post('http://' + ip_address + ':5000/move_arm', '{"servo" : "' + e.currentTarget.id + '", "startEvent" : false}')
});