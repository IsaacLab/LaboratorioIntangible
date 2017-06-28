<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
   <head><title>Vodafone</title>
      <!--meta HTTP-EQUIV='Pragma' CONTENT='no-cache'-->
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
     
	<script type="text/javascript">
	var ipaddr = '192.168.0.1';
	var language = 'es_ES';
	var ienbpinresult = '500';
	var sHspaStatus = '1';
	
	//added by w00159377 http intercept flow
	var ispinneeded = '-1';
	var DeviceHspaget = '1';
    var SimHspaget = '1';
	
	//var loc = 'http://'+ ipaddr + '/' + language + '/hspa/HspaFirstPage.html';
	if(DeviceHspaget != '0')
	{
		var loc = 'http://'+ ipaddr + '/' + language + '/hspa/noHspaFirstPage.html';
	}
	else if(SimHspaget != '0')
	{
		var loc = 'http://'+ ipaddr + '/' + language + '/hspa/noSimfirst.html';
	}
	else if('1' == ispinneeded)
	{
		var loc = 'http://'+ ipaddr + '/' + language + '/hspa/pincfgfirst.html';	
	}
	else
	{
		var loc = 'http://'+ ipaddr + '/' + language + '/hspa/hspacfgfirst.html';
	}
	window.location = loc;
	
	</script>
   </head>
   <body>
     
   </body>
</html>
