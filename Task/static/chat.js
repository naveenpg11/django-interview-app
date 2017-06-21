$(function() {
    // When we're using HTTPS, use WSS too.
    
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "" + window.location.pathname);
    
    chatsock.onmessage = function(message) {
                        

        var data = JSON.parse(message.data);
        id_name=data.u_name;

        var stat=data.state;
        if(stat=="online")
        {  
            var online = $("#online")
             var ale = $('<tr id='+id_name+'></tr>')
             ale.append(
            $("<td></td>").text(data.u_name)
        )
             online.append(ale)
        }
        else if (stat=="offline")
        {           
            $("#"+id_name).remove();
        }
        else{
        var chat = $("#chat")
        var tab = $('<tr></tr>')

        tab.append(
            $("<td></td>").text(data.uname)
        )
        tab.append(
            $("<td></td>").text(data.message)
        )
        tab.append(
            $("<td></td>").text(data.timestamp)
        )
        
        chat.append(tab)
    }
    };
    $("#chatform").on("submit", function(event) {
        var message = {          
            uname: $('#new').val(),
            message: $('#message').val(),
        }
        chatsock.send(JSON.stringify(message));
        $("#message").val('').focus();
        return false;
    });
 
});