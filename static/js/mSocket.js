var net = require('net');

function sendReceive() {
    console.log('here')
    var client = new net.Socket();
    client.connect(65432, '127.0.0.1', function() {
        console.log('Connected');
        client.write('Hello, server! Love, Client.');
    });

    client.on('data', function(data) {
        console.log('Received: ' + data);
        client.destroy(); // kill client after server's response
    });
}
